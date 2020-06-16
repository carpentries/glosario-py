from yaml import load, FullLoader
from textdistance import cosine
from pkg_resources import resource_stream
from collections import Counter

stream = resource_stream(__name__, 'data/glossary.yml')
raw = load(stream, Loader=FullLoader)
Terms = {term['slug']: term for term in raw}

__language__ = 'en'

def get_languages_available():
    """
    Get all languages available part of the dictionary.

    Parameters
    ----------

    Returns
    -------
    Counter({})
      A counter object with the number of instances each language is present as an entry.

    Examples
    --------
    >>> from glosario import glosario
    >>> glosario.get_languages_available()
    """
    lang_dict = Counter()

    for _, values in Terms.items():
        keys = list(values.keys())
        for key in keys:
            if key != 'slug' and key != 'ref':
                lang_dict.update({key: 1})

    return lang_dict

def set_language(language, verbose=False):
    """
    Get all languages available part of the dictionary.

    Parameters
    ----------
    language: str
        Language to return the definitions in
    verbose: bool
        Whether to print verbal confirnmation of the change
    Returns
    -------

    Examples
    --------
    >>> from glosario import glosario
    >>> glosario.set_language('es')
    """
    langs_available = get_languages_available()

    if language not in langs_available.keys():
        if verbose:
            print('Currently we don\'t support this language.\nFeel free to submit definitions to this language at https://github.com/gvwilson/glossary')
        return None
    else:
        global __language__
        if verbose:
            print(f'Current Language: {__language__}\nNew Language: {language}')
        __language__ = language

def __search_word__(slug):
    '''Look up a definition in a glossary by slug.'''
    definition = Terms.get(slug)
    return definition.get(__language__)

def __known_words__():
    '''Report all known definition slugs as a set.'''
    return Terms.keys()

def __search_similar_word__(slug):
    '''Match up to most similar word'''
    similarity_dict = {}

    for term in __known_words__():
        similarity_dict[term] = cosine.normalized_similarity(slug, term)
    
    return max(similarity_dict, key = similarity_dict.get)

def define(slug):
    """
    Define a given word

    Parameters
    ----------
    slug: str
        The word you want to search

    Returns
    -------
    str:
      The word definition

    Examples
    --------
    >>> from glosario import glosario
    >>> glosario.get_languages_available()
    """
    try:
        similar_word = __search_similar_word__(slug)
        word_definition = __search_word__(similar_word)
        
        return word_definition['def']
    except:
        print('We couldn\'t find this word in the dictionary')