from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command
from aiogram.dispatcher.filters.builtin import CommandStart, CommandHelp, CommandSettings
from keyboards.default.text_buttons import settings_buttons

from loader import dp

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name} Я 🤖 бот, который 🔎 парсит twitter")

@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку",
            "/settings - Настройки парсинга")
    await message.answer("\n".join(text))

@dp.message_handler(CommandSettings())
async def bot_settings(message: types.Message):
    await message.answer(f'................', reply_markup=settings_buttons)



@dp.message_handler(lambda message: message.text and 'ты кто?' in message.text.lower())
async def bot_echo(message: types.Message):
    await message.answer(f"просто бот")




# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(f"Эхо без состояния."
                         f"Сообщение:\n"
                         f"{message.text}")


# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    state = await state.get_state()
    await message.answer(f"Эхо в состоянии <code>{state}</code>.\n"
                         f"\nСодержание сообщения:\n"
                         f"<code>{message}</code>")
