from flask import Flask, request
import telebot
from dotenv import load_dotenv
from telebot import types
import os

load_dotenv('.env')
app = Flask(__name__)
TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

MAIN_MENU_BUTTON = "Головне меню"


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Виберіть категорію:', reply_markup=create_main_menu_keyboard())


# Клавиатура главного меню
def create_main_menu_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in [
        'Безпека', 'Допомога', 'Заклади охорони здоров\'я',
        'Освітні заклади', 'Заходи для відпочинку та розвитку',
        'Корисні посилання'
    ]])
    return keyboard


# Отправляем пользователя в главное меню
@bot.message_handler(func=lambda message: message.text == MAIN_MENU_BUTTON)
def handle_main_menu(message):
    bot.send_message(message.chat.id, 'Виберіть категорію:', reply_markup=create_main_menu_keyboard())


# кнопка "БЕЗПЕКА"
@bot.message_handler(func=lambda message: message.text == "Безпека")
def safety_button(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(types.KeyboardButton("Поліція"), types.KeyboardButton("Укриття"),
                 types.KeyboardButton("Правова допомога"), types.KeyboardButton(MAIN_MENU_BUTTON))
    bot.send_message(message.chat.id, "Виберіть підрозділ, який вас цікавить:", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == "Поліція")
def police_message(message):
    bot.send_message(message.chat.id, "Поліція: \n"
                                      "вул. Степана Бандрери, 14")


@bot.message_handler(func=lambda message: message.text == "Укриття")
def shelter_message(message):
    with open('security_text.txt', 'r') as file:
        text = file.read()
    bot.send_message(message.chat.id, text)


@bot.message_handler(func=lambda message: message.text == "Правова допомога")
def lawyer_message(message):
    with open('law.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(message.chat.id, text=text, parse_mode='HTML')


# кнопка "ДОПОМОГА"
@bot.message_handler(func=lambda message: message.text == "Допомога")
def help_button(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(types.KeyboardButton("Фінансова допомога"), types.KeyboardButton("Гуманітарна допомога"),
                 types.KeyboardButton("Житло"), types.KeyboardButton("Одяг"),
                 types.KeyboardButton("Контакти і місцерозташування служб"),
                 types.KeyboardButton(MAIN_MENU_BUTTON))
    bot.send_message(message.chat.id, "Виберіть підрозділ, який вас цікавить:", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == "Фінансова допомога")
def financial_help_message(message):
    bot.send_message(message.chat.id, "1. Консультативно-координаційний центр допомоги ВПО — "
                                      "вул. І.Мазепи, 8, каб. 2\n\n"

                                      "2. Самбірська міська рада — площа Ринок 1")


@bot.message_handler(func=lambda message: message.text == "Гуманітарна допомога")
def humanitarian_aid_message(message):
    with open('humanitarian_help_text.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(message.chat.id, text=text, parse_mode='HTML')


@bot.message_handler(func=lambda message: message.text == "Житло")
def housing_message(message):
    with open('housing.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(message.chat.id, text=text, parse_mode='HTML')


@bot.message_handler(func=lambda message: message.text == "Одяг")
def clothing_message(message):
    bot.send_message(message.chat.id, "Банк одягу — ТЧХУ вул. І. Мазепи, 8, каб. 54")


@bot.message_handler(func=lambda message: message.text == "Контакти і місцерозташування служб")
def help_contacts_message(message):
    with open('contacts.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(message.chat.id, text=text, parse_mode='HTML')


# кнопка "Заклади охорони здоров'я"
@bot.message_handler(func=lambda message: message.text == "Заклади охорони здоров\'я")
def hospital_button(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(types.KeyboardButton(MAIN_MENU_BUTTON))
    bot.send_message(message.chat.id, "Заклади охорони здоров\'я", reply_markup=keyboard)
    with open('healthy.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(message.chat.id, text=text, parse_mode='HTML')


# кнопка "ОСВІТНІ ЗАКДАДИ"
@bot.message_handler(func=lambda message: message.text == "Освітні заклади")
def education_button(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(types.KeyboardButton("Коледжі"), types.KeyboardButton("Школи"), types.KeyboardButton("Садки"),
                 types.KeyboardButton("Гуртки"),
                 types.KeyboardButton(MAIN_MENU_BUTTON))
    bot.send_message(message.chat.id, "Виберіть підрозділ, який вас цікавить:", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == "Коледжі")
def university_message(message):
    with open('high_schools.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(message.chat.id, text=text, parse_mode='HTML')


@bot.message_handler(func=lambda message: message.text == "Школи")
def school_message(message):
    with open('schools.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(message.chat.id, text=text, parse_mode='HTML')


@bot.message_handler(func=lambda message: message.text == "Садки")
def kindergarten_message(message):
    with open('gardens.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(message.chat.id, text=text, parse_mode='HTML')


@bot.message_handler(func=lambda message: message.text == "Гуртки")
def section_message(message):
    with open('hobby.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(message.chat.id, text=text, parse_mode='HTML')


# кнопка "Корисні посилання"
@bot.message_handler(func=lambda message: message.text == "Корисні посилання")
def other_button(message):
    with open('images/useful_links.png', 'rb') as image:
        bot.send_photo(message.chat.id, photo=image)

    with open('other.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(types.KeyboardButton(MAIN_MENU_BUTTON))
    bot.send_message(message.chat.id, text=text, parse_mode='HTML', reply_markup=keyboard)



@bot.message_handler(func=lambda message: message.text == "Заходи для відпочинку та розвитку")
def other_message(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(types.KeyboardButton("Салони краси"), types.KeyboardButton("Готелі"),
                 types.KeyboardButton("Ресторани/бари"),
                 types.KeyboardButton("Фастфуд"), types.KeyboardButton("Кафе"),
                 types.KeyboardButton(MAIN_MENU_BUTTON))
    bot.send_message(message.chat.id, "Виберіть підрозділ, який вас цікавить:", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == "Салони краси")
def shelter_message(message):
    with open('salons.txt', 'r', encoding='utf-8') as file:
        text = file.read()
        text = text.replace('%2B', '+')
    bot.send_message(message.chat.id, text=text, parse_mode='HTML')


@bot.message_handler(func=lambda message: message.text == "Готелі")
def hotel_message(message):
    with open('hotels.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(message.chat.id, text=text, parse_mode='HTML')


@bot.message_handler(func=lambda message: message.text == "Ресторани/бари")
def bars_message(message):
    with open('bar.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(message.chat.id, text=text, parse_mode='HTML')


@bot.message_handler(func=lambda message: message.text == "Фастфуд")
def fastfood_message(message):
    with open('fastfood.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(message.chat.id, text=text, parse_mode='HTML')


@bot.message_handler(func=lambda message: message.text == "Кафе")
def cafe_message(message):
    with open('cafe.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(message.chat.id, text=text, parse_mode='HTML')


@app.route('/' + TOKEN, methods=['POST'])
def get_message():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "Python Telegram Bot", 200


@app.route('/')
def main():
    bot.remove_webhook()
    bot.set_webhook(url='https://redcrossbot.herokuapp.com/' + os.environ.get('TOKEN'))
    return 'Python Telegram Bot', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
