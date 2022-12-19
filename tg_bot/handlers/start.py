from aiogram import types, Dispatcher

from tg_bot.keyboards import inline_start


async def start(message: types.Message):
    # сообщение старт
    text = [
        f'🟢Привет, {message.from_user.full_name}🟢',
        'Я бот <strong>конвертер валют</strong> и я помогу тебе узнать '
        'текущий курс на интересующую тебя валюту к определенной валюте'
    ]
    await message.answer('\n'.join(text), reply_markup=inline_start.keyboard)


def register_start(dp: Dispatcher):
    dp.register_message_handler(start, state='*')
