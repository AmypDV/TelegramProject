from typing import NamedTuple

class LEXICON_RU(NamedTuple):
    start:str = 'Привет!\nМеня зовут Бот!\nНапиши мне что-нибудь'
    help: str = ''' Напиши мне что-нибудь и в ответ
я пришлю тебе твое сообщение.
К тому же я генерирую фотографии кошек, собак и лис
в ответ на сообщения: кот, собака, лиса'''
    stupid: str = 'Я пока глуп и отвечаю только на текстовые сообщения и стикеры 😁'