from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

router = Router()
llm = ChatOllama(model="llama3.1", temperature=0.7)

@router.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Hello! I'm *KoroHelper*, ask me anything!\n\nType /help for help",
        parse_mode="Markdown")


@router.message(Command("help"))
async def help(message: Message):
    await message.answer(
        "Commands:\n<b>/start</b> - start bot\n/help - list of commands\n/about - about us",
        parse_mode="HTML")


@router.message(Command("about"))
async def about(message: Message):
    await message.answer(f"This is a command for bot. Your name: {message.from_user.first_name}")


@router.message()
async def any_message(message: Message):
    await message.answer("Thinking...")

    response = await llm.ainvoke([
        HumanMessage(content=message.text)
    ])

    await message.answer(response.content)