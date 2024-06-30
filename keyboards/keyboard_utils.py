from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


# Создаем объекты кнопок
button_cat = KeyboardButton(text='Кот')
button_dog = KeyboardButton(text='Собака')
button_fox = KeyboardButton(text='Лиса')


# Создаем объект клавиатуры, добавляя в него кнопки
keyboard_animal = ReplyKeyboardMarkup(keyboard=[[button_cat, button_dog, button_fox]],
                                      resize_keyboard=True,
                                      one_time_keyboard=True
                                     )