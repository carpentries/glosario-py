import requests

url = "https://raw.githubusercontent.com/carpentries/glosario/master/glossary.yml"

res = requests.get(url)

open('glosario/data/glossary.yml', 'wb').write(res.content)
