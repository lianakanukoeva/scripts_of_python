#импортируем библиотеку
import telebot
import requests
import bs4

#токен
token = '726376465:AAH5NBFRlVJW0Hmhgt6O2UW8U3SnSM4yKuo'

# создаем бота
bot = telebot.TeleBot(token)

#здрасте
@bot.message_handler(content_types=["text"])
def start(msg):
    if msg.text == "Olaf, wake up":
        bot.send_message(msg.chat.id, 'Привет! Меня зовут Олаф. Если вам интересно когда выйдет серия вашего любимого зарубежного сериала, то введите его название')

#ищем сериал и дату
@bot.message_handler(content_types=["text"])
def series(msg):
    html=requests.get('http://www.ulitka.tv/countdown.html')
    parsed = bs4.BeautifulSoup(html.text, 'html.parser')
    for elem in parsed.find('table', id='genre-table').find_all('tr'):
        for serial in elem.find_all('td'):
            try:
                if msg.text == serial.find('strong').text:
                    return bot.send_message(msg.chat.id, str(serial.find('small').replace('<small>', '').replace('<br/>', '\n').replace('</small>', '')))
            except:
                pass


bot.polling(none_stop=True)

# name = input()
# print(series(name))

# #импортируем библиотеку
# import telebot
# import requests
# import bs4

# #токен
# token = '726376465:AAH5NBFRlVJW0Hmhgt6O2UW8U3SnSM4yKuo'

# # создаем бота
# bot = telebot.TeleBot(token)

# #здрасте
# @bot.message_handler(content_types=["text"])
# def start(msg):
#     if msg.text == "Olaf, wake up":
#         bot.send_message(msg.from_user.id, 'Привет! Меня зовут Олаф. Если вам интересно когда выйдет серия вашего любимого зарубежного сериала, то введите /series')

# #ищем сериал и дату
# @bot.message_handler(command=["series"])
# def series(msg):
#     html=requests.get('http://www.ulitka.tv/countdown.html')
#     parsed = bs4.BeautifulSoup(html.text, 'html.parser')
#     for elem in parsed.find('table', id='genre-table').find_all('tr'):
#         for serial in elem.find_all('td'):
#             try:
#                 if msg == serial.find('strong').text:
#                     return str(serial.find('small')).replace('<small>', '').replace('<br/>', '\n').replace('</small>', '')
#             except:
#                 pass

# bot.polling(none_stop=True)

# name = input()
# print(series(name))