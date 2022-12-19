from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='💵Узнать курс популярных валютных пар💵',
                callback_data='top_currency_pair'
            ),
        ],
        [
            InlineKeyboardButton(
                text='💶Узнать свою валютную пару💶',
                callback_data='self_currency_pair'
            )
        ]
    ],
    row_width=1,

)
