from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


# Создаем объекты кнопок
button_cat = KeyboardButton(text='Кот')
button_dog = KeyboardButton(text='Собака')
button_fox = KeyboardButton(text='Лиса')


# Инициализируем объект билдера
kb_builder_animal = ReplyKeyboardBuilder()
kb_builder_animal.row(button_cat, button_dog, button_fox, width=3)
keyboard_animal = kb_builder_animal.as_markup(
                                              resize_keyboard=True,
                                              one_time_keyboard=True
                                              )
