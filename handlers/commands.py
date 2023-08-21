from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart, ChatTypeFilter
from aiogram.dispatcher import FSMContext
from bot import bot, dp
from utils import states
from keyboards import inline_kb
from utils import states
from utils import config


#@dp.message_hanlder(ChatTypeFilter(chat_type=types.ChatType.PRIVATE), CommandStart())
async def start_bot(message: types.Message, state: FSMContext):
    memberID = message.from_user.id
    await message.answer(f"""Прежде чем попасть в чат, ответьте на три вопроса.\n
Первый вопрос - "{config.first_question}"
""")
    await state.set_state(states.QuestionsList.first_question_state)

#@dp.message_handler(ChatTypeFilter(chat_type = types.ChatType.PRIVATE), state = states.QuestionsList.first_question_state, content_types = ['text'])
async def check_first_answer(message: types.Message, state: FSMContext):
    if message.text.lower() == config.right_first_answer:
        await state.update_data(first_answer = message.text.lower())
        await message.answer(f'Второй вопрос - "{config.second_question}"')
        await state.set_state(states.QuestionsList.second_question_state)
    else:
        await message.answer("Вы неправильно ответили на вопрос! ❌")

#@dp.message_handler(ChatTypeFilter(chat_type = types.ChatType.PRIVATE), state = QuestionsList.second_question_state, content_types = ['text'])
async def check_second_answer(message: types.Message, state: FSMContext):
    if message.text.lower() == config.right_second_answer:
        await state.update_data(second_answer = message.text.lower())
        await message.answer(f'Третий вопрос - "{config.third_question}"')
        await state.set_state(states.QuestionsList.third_question_state)
    else:
        await message.answer("Вы неправильно ответили на вопрос! ❌")

#@dp.message_handler(ChatTypeFilter(chat_type = types.ChatType.PRIVATE), state = QuestionsList.third_question_state, content_types = ['text'])
async def check_third_answer(message: types.Message, state: FSMContext):
    if message.text.lower() == config.right_third_answer:
        await state.update_data(third_answer = message.text.lower())
        await message.answer("Ваша заявка подана, ждите ответ администрации.")
        request_data = await state.get_data()
        await state.finish()
        await bot.send_message(config.admin_id, text = f"""Пользователь с айди {message.from_user.id} подал заявку на вступление в чат.\n
Первый вопрос: {config.first_question}.\n
Ответ пользователя на первый вопрос: {request_data['first_answer']}.\n
Второй вопрос: {config.second_question}.\n
Ответ пользователя на второй вопрос: {request_data['second_answer']}.\n
Третий вопрос: {config.third_question}.\n
Ответ пользователя на третий вопрос: {request_data['third_answer']}.\n
""", reply_markup = inline_kb.request_keyboard(message.from_user.id, f"tg://user?id={message.from_user.id}",
                                               request_data['first_answer'], request_data['second_answer'], request_data['third_answer'])
                               )
    else:
        await message.answer("Вы неправильно ответили на вопрос! ❌")

def register_commands(dp: Dispatcher):
    dp.register_message_handler(start_bot, ChatTypeFilter(chat_type=types.ChatType.PRIVATE), CommandStart())
    dp.register_message_handler(check_first_answer, ChatTypeFilter(chat_type = types.ChatType.PRIVATE), state = states.QuestionsList.first_question_state, content_types = ['text'])
    dp.register_message_handler(check_second_answer, ChatTypeFilter(chat_type = types.ChatType.PRIVATE), state = states.QuestionsList.second_question_state, content_types = ['text'])
    dp.register_message_handler(check_third_answer, ChatTypeFilter(chat_type = types.ChatType.PRIVATE), state = states.QuestionsList.third_question_state, content_types = ['text'])
