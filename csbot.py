from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.utils.markdown import text
from aiogram.dispatcher import Dispatcher
from aiogram.types import Message, CallbackQuery
import random
from random import randint


from config import TOKEN
import keyboard as kb

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.callback_query_handler(lambda message: "buy_chit" == message.data)
async def but_a_chit(call: CallbackQuery):
    await call.message.reply(buy_message_month, reply_markup=kb.inline_kb2)
    #await call.message.reply(n, reply_markup=kb.inline_kb2)


@dp.callback_query_handler(lambda message: "buy_chit_ever" == message.data)
async def but_a_chit(call: CallbackQuery):
    await call.message.reply(buy_message_ever, reply_markup=kb.inline_kb2)
    #await call.message.reply(n, reply_markup=kb.inline_kb2)


@dp.callback_query_handler(lambda message: "pay_f" == message.data)
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, Buy_message_tt, reply_markup=kb.inline_kb3)


@dp.callback_query_handler(lambda message: "Che_stat" == message.data)
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, Buy_message_ts, reply_markup=kb.inline_kb3)


@dp.callback_query_handler(lambda message: "my_dick" == message.data)
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, help_message_s1)

#num = list(range(100000, 999999))
#code_pass = random.choice(num)

code_pass = randint(100000, 999999)

n = '22'


help_message_s1 = text(
    "Ох, друг нам очень жаль что у тебя возникли трудности. Мы постараемся помочь как можно быстрее!",
    sep="\n"
)

help_message = text(
    "Если у Вас возникли трудности — нажмите на кнопку ниже и с вами свяжется кто-нибудь из поддержки",
    sep="\n"
)

Buy_message_ts = text(
    "Еще не получил:( Придется еще подождать...",
    sep="\n"
)

Buy_message_tt = text(
    "Отлично! Как только я увижу оплату ты получишь ссылку",
    sep="\n"
)

start_message = text(
    "Привет! Я бот торговец читами для CSGO!",
    "И у меня есть кое-что интересное для тебя!:)",
    "Privat_wi_X:)ack - Это мультичит включающий в себя:\n",
    "Wallhack, Aimbot,BunnyHop,",
    "NoRecoil, Trigger + скрипт на динамический ник:)",
    sep="\n"
)
buy_message_ever = text(
    "Купить чит навсегда стоит 2000 рублей.",
    "https://qiwi.com/p/380988649025\n",
    "Когда я получу оплату, ты получишь ссылку на скачивание где будет:",
    "Сам чит + инструкция по установке и использованию.",
    "P.S. При оплате обязательно укажи в коментарии код твоей заявки -", code_pass,
    sep="\n"
)

buy_message_month = text(
    "Месяц пользования стоит 750 рублей.",
    "https://qiwi.com/p/380988649025\n",
    "Когда я получу оплату, ты получишь ссылку на скачивание где будет:",
    "Сам чит + инструкция по установке и использованию.",
    "P.S. При оплате обязательно укажи в коментарии код твоей заявки -", code_pass,
    sep="\n"
)


# @dp.message_handler(commands=['help'])
# async def process_help_command(message: types.Message):
#    await message.reply(help_message)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(start_message, reply_markup=kb.inline_kb1)

@dp.message_handler(commands=['help'])
async def process_start_command(message: types.Message):
    await message.reply(help_message, reply_markup=kb.inline_kb4)

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Я понимаю не все команды, используй пожалуйста кнопки!')


if __name__ == '__main__':
    executor.start_polling(dp)
