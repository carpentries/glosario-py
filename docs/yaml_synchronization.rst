=====
Glosario YAML Synchronization
=====

This project uses the `glosario <https://github.com/carpentries/glosario>`_ `YAML file <https://github.com/carpentries/glosario/blob/master/glossary.yml>`_, which contains the glossary of technical terms. In order to keep an updated copy of that file within this project, a GitHub Action is used on a daily basis to schedule an import into the repository. The Action relies on the util script in ``utils/download_data.py``. Since the import is run once a day, you can expect that the file may be out of date for up to 24 hours when you first check out this project or this project is installed from pip.

However, currently once this project is installed there is no method for synchronization and the glossary will remain out of date unless ``utils/download_data.py`` is manually run once again. 

