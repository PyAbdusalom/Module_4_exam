import smtplib

text1 = "ovbmixoksmpivxoy"
text2 = "abdusalomabduvaliyev07@gmail.com"

password = text1
sender = text2
server = "smtp.gmail.com"
port = 465
receiver = "absaitovdev@gmail.com"
message = """
From: {}
To: {}
subject:
    ============  topshiriq - 1  ==============
    import logging

    from aiogram import Bot, Dispatcher, executor, types
    from aiogram.contrib.fsm_storage.memory import MemoryStorage
    from aiogram.dispatcher import FSMContext
    
    API_TOKEN = '6173499684:AAEw3dsyo3YGpaJVTKdHU8xdZp-QmO59ick'
    
    logging.basicConfig(level=logging.INFO)
    
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher(bot=bot, storage=MemoryStorage())
    
    
    @dp.message_handler(commands=['start', 'help'])
    async def send_welcome(message: types.Message, state: FSMContext):
        await message.reply(f"Assalomu alaykum {message.from_user.full_name} 😊")
        await message.answer("Text Kiriting")
        await state.set_state("text")
    
    
    @dp.message_handler(state="text")
    async def echo(message: types.Message, state: FSMContext):
        All_vowels = "aeiouAEIOU"
        summa = sum([1 for i in message.text if i in All_vowels])
        if summa >= 5:
            await message.answer("Text unlilar soni 5 dan oshib ketti. Qayta kiriting")
            await state.set_state("text")
        else:
            await state.set_state("text")
    
    
    if __name__ == '__main__':
        executor.start_polling(dp, skip_updates=True)
        
    ================== topshiriq - 2 =====================
    
    pull qilish uchun:
        docker pull pyabdusalom/4_module_exam_img:alpine
    
    
    
    
""".format(sender, receiver)

with smtplib.SMTP_SSL(server, port) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, message)
    print("Sending email")
