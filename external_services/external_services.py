import requests
import logging

URL_OF_SERVICES = {'кот':'https://api.thecatapi.com/v1/images/search',
                   'собака':'https://random.dog/woof.json',
                   'лиса':'https://randomfox.ca/floof/'}

logger = logging.getLogger(__name__)

def get_url_of_cat() -> str:
    url = URL_OF_SERVICES['кот']
    foto = requests.get(url)
    if foto.status_code == 200:
        foto = foto.json()[0]["url"]
        logger.info('parcer cat')
        return foto

def get_url_of_dog() -> str:
    url = URL_OF_SERVICES['собака']
    foto = requests.get(url)
    if foto.status_code == 200:
        foto = foto.json()["url"]
        logger.info('parcer dog')
        return foto

def get_url_of_fox() -> str:
    url = URL_OF_SERVICES['лиса']
    foto = requests.get(url)
    if foto.status_code == 200:
        foto = foto.json()["image"]
        logger.info('parcer fox')
        return foto

