from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from keyboards import inline_kb
from bot import bot
from utils import config

#@dp.callback_query_handler(startswith = 'accept_member')
async def accept_callback(call: types.CallbackQuery): 
   member_id = call.data.split('|')[1]
   
   await call.message.edit_text(f"""Пользователь с айди {member_id} подал заявку на вступление в чат.\n
Первый вопрос: {config.first_question}.\n
Ответ пользователя на первый вопрос: {call.data.split('|')[2]}.\n
Второй вопрос: {config.second_question}.\n
Ответ пользователя на второй вопрос: {call.data.split('|')[3]}.\n
Третий вопрос: {config.third_question}.\n
Ответ пользователя на третий вопрос: {call.data.split('|')[4]}.\n
""", reply_markup = inline_kb.answered_request_keyboard(f"tg://user?id={member_id}"))
   
   await bot.send_message(member_id, text = " ⬇ Администратор принял вашу заявку, свяжитесь с тимлидером. ⬇ ", reply_markup = inline_kb.chat_url_keyboard(config.chat_url))


#@dp.callback_query_handler(startswith = 'decline_member')
async def decline_callback(call: types.CallbackQuery):
   member_id = call.data.split('|')[1]
   
   await call.message.edit_text(f"""Пользователь с айди {member_id} подал заявку на вступление в чат.\n
Первый вопрос: {config.first_question}.\n
Ответ пользователя на первый вопрос: {call.data.split('|')[2]}.\n
Второй вопрос: {config.second_question}.\n
Ответ пользователя на второй вопрос: {call.data.split('|')[3]}.\n
Третий вопрос: {config.third_question}.\n
Ответ пользователя на третий вопрос: {call.data.split('|')[4]}.\n
""", reply_markup = inline_kb.answered_request_keyboard(f"tg://user?id={member_id}"))

   await bot.send_message(member_id, text = """Администратор отклонил вашу заявку.""")
   
def register_callbacks(dp: Dispatcher):
   dp.register_callback_query_handler(accept_callback, Text(startswith = 'accept_member'))
   dp.register_callback_query_handler(decline_callback, Text(startswith = 'decline_member'))
