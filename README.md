## glosario

[![Documentation Status](https://readthedocs.org/projects/glossary/badge/?version=latest)](https://glossary.readthedocs.io/en/latest/?badge=latest)

Package to define technical terms

### Installation:

```
pip install glosario
```

### Usage

```
>>> from glosario import glosario
>>> glosario.set_language('en')
>>> glosario.define('data frame')
```

### Features

- Defines technical terms in multiple languages
- Allows for setting multiple languages in one script (sequentially)
- Implements cosine similarity for matching words to closest slug

### Dependencies

- `PyYaml`
- `textdistance`

### Documentation

The official documentation is hosted on Read the Docs: <https://glosario.readthedocs.io/en/latest/>

### Credits
This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
