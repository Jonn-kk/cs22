from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from dataclasses import dataclass

inline_btn_5 = InlineKeyboardButton('Нужна помощь', callback_data='my_dick')
inline_btn_4 = InlineKeyboardButton('Купить Чит на навегда', callback_data='buy_chit_ever')
inline_btn_1 = InlineKeyboardButton('Купить Чит на месяц', callback_data='buy_chit')
inline_btn_2 = InlineKeyboardButton('Я оплатил!', callback_data='pay_f')
inline_btn_3 = InlineKeyboardButton('Проверить статус оплаты', callback_data='Che_stat')

inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_4)

inline_kb2 = InlineKeyboardMarkup().add(inline_btn_2)

inline_kb3 = InlineKeyboardMarkup().add(inline_btn_3)

inline_kb4 = InlineKeyboardMarkup().add(inline_btn_5)

#st = ('У меня есть кое что интересное для тебя! Privat_wiX:)ack. '
#                'Это мультичит включающий в сетя Wallhack,aimbot,'
#               'banyhope,norecoil,trigger + скрипт на динамический ник:)')



