from aiogram.dispatcher.filters.state import State, StatesGroup

class QuestionsList(StatesGroup):
    first_question_state = State()
    second_question_state = State()
    third_question_state = State()


    
