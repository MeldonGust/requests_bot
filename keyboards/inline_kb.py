from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def request_keyboard(member_id, member_url, answer_1, answer_2, answer_3):
    markup = InlineKeyboardMarkup(
        inline_keyboard = [
            [
                InlineKeyboardButton(
                    text = 'Одобрить✅',
                    callback_data = f'accept_member|{member_id}|{answer_1}|{answer_2}|{answer_3}'
                    )
            ],
            [
                InlineKeyboardButton(
                    text = 'Отклонить❌',
                    callback_data = f'decline_member|{member_id}|{answer_1}|{answer_2}|{answer_3}'
                    )
            ],
            [
                InlineKeyboardButton(
                    text = 'Ссылка на профиль👤',
                    url = member_url
                    )
            ]
    ]
    )
    return markup

def answered_request_keyboard(member_url):
    markup = InlineKeyboardMarkup(
        inline_keyboard = [
            [
                
                InlineKeyboardButton(
                    text = 'Ссылка на профиль👤',
                    url = member_url
                    )
            ]
        ]
    )
    return markup

def chat_url_keyboard(chat_url):
    markup = InlineKeyboardMarkup(
        inline_keyboard = [
            [
                
                InlineKeyboardButton(
                    text = 'Ссылка на чат📩',
                    url = chat_url
                    )
            ]
        ]
    )
    return markup
