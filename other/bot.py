import telebot

bot = telebot.TeleBot('5596499660:AAGklOSndBl0ksCNsQZKECpi3ICWCk4WqDs')

#В этом участке кода мы объявили слушателя для принятия документа и текстовых сообщений и метод их обработки. Поле content_types может принимать разные значения
@bot.message_handler(content_types=['text', 'document'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет, чо надо?')
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Напиши: привет')
    else:
        bot.send_message(message.from_user.id, 'Что ты написал, напиши /help')


bot.polling(none_stop=True, interval=0)
#Теперь наш бот будет постоянно спрашивать у сервера Телеграмма «Мне кто-нибудь написал?»,
#и если мы напишем нашему боту, то Телеграмм передаст ему наше сообщение
