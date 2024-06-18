import requests
import time
from pprint import pprint
import os


API_URL = 'https://api.telegram.org/bot'
URL_CAT = 'https://api.thecatapi.com/v1/images/search'

TEXT_1 = 'Все говорят:'
TEXT_2 = 'А ты купи слона!'
MAX_COUNTER = 20
BOT_TOKEN = os.getenv("Amyp_First_Bot_key", "00000000")

offset = -2
counter = 0
chat_id: int


while counter < MAX_COUNTER:

    print('attempt =', counter)  #Чтобы видеть в консоли, что код живет

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            pprint(result)
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            txt = result['message']['text']
            if txt.lower() == 'кот':
                foto = requests.get(URL_CAT)
                if foto.status_code == 200:
                    print(foto.json()[0])
                    foto = foto.json()[0]["url"]
                    requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={foto}')
                else:
                    text_cat = 'здесь должно быть фото кота, попробуй еще раз'
                    requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={text_cat}')
            else:
                text = TEXT_1 + '\n' + txt + '\n' + TEXT_2
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={text}')
        counter += 1
    time.sleep(1)
