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
        'Корисні посилання', 'Самбірська РО ТЧХУ'
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
    with open('images/cops.png', 'rb') as image:
        bot.send_photo(message.chat.id, photo=image)
    bot.send_message(message.chat.id, "Поліція: \n"
                                      "вул. Степана Бандрери, 14")


@bot.message_handler(func=lambda message: message.text == "Укриття")
def shelter_message(message):
    with open('images/shelter.png', 'rb') as image:
        bot.send_photo(message.chat.id, photo=image)
    with open('security_text.txt', 'r') as file:
        text = file.read()
    bot.send_message(message.chat.id, text)


@bot.message_handler(func=lambda message: message.text == "Правова допомога")
def lawyer_message(message):
    with open('images/law_help.png', 'rb') as image:
        bot.send_photo(message.chat.id, photo=image)
    with open('law.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(message.chat.id, text=text, parse_mode='HTML')


# кнопка "ДОПОМОГА"
@bot.message_handler(func=lambda message: message.text == "Допомога")
def help_button(message):
    with open('images/help.png', 'rb') as image:
        bot.send_photo(message.chat.id, photo=image)
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(types.KeyboardButton("Фінансова допомога"), types.KeyboardButton("Гуманітарна допомога"),
                 types.KeyboardButton("Житло"), types.KeyboardButton("Одяг"),
                 types.KeyboardButton("Контакти і місцерозташування служб"),
                 types.KeyboardButton(MAIN_MENU_BUTTON))
    bot.send_message(message.chat.id, "Виберіть підрозділ, який вас цікавить:", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == "Фінансова допомога")
def financial_help_message(message):
    with open('images/finance.png', 'rb') as image:
        bot.send_photo(message.chat.id, photo=image)
    bot.send_message(message.chat.id, "1. Консультативно-координаційний центр допомоги ВПО — "
                                      "вул. І.Мазепи, 8, каб. 2\n\n"

                                      "2. Самбірська міська рада — площа Ринок 1")


@bot.message_handler(func=lambda message: message.text == "Гуманітарна допомога")
def humanitarian_aid_message(message):
    with open('images/humanitarian.png', 'rb') as image:
        bot.send_photo(message.chat.id, photo=image)
    with open('humanitarian_help_text.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(message.chat.id, text=text, parse_mode='HTML')


@bot.message_handler(func=lambda message: message.text == "Житло")
def housing_message(message):
    with open('images/home.png', 'rb') as image:
        bot.send_photo(message.chat.id, photo=image)
    with open('housing.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(message.chat.id, text=text, parse_mode='HTML')


@bot.message_handler(func=lambda message: message.text == "Одяг")
def clothing_message(message):
    with open('images/cloth.png', 'rb') as image:
        bot.send_photo(message.chat.id, photo=image)
    bot.send_message(message.chat.id, "Банк одягу — ТЧХУ вул. І. Мазепи, 8, каб. 54")


@bot.message_handler(func=lambda message: message.text == "Контакти і місцерозташування служб")
def help_contacts_message(message):
    with open('images/contacts.png', 'rb') as image:
        bot.send_photo(message.chat.id, photo=image)
    with open('contacts.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(message.chat.id, text=text, parse_mode='HTML')


# кнопка "Заклади охорони здоров'я"
@bot.message_handler(func=lambda message: message.text == "Заклади охорони здоров\'я")
def hospital_button(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(types.KeyboardButton(MAIN_MENU_BUTTON))
    bot.send_message(message.chat.id, "Заклади охорони здоров\'я", reply_markup=keyboard)
    with open('images/health.png', 'rb') as image:
        bot.send_photo(message.chat.id, photo=image)
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
    with open('images/colleges.png', 'rb') as image:
        bot.send_photo(message.chat.id, photo=image)
    with open('high_schools.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(message.chat.id, text=text, parse_mode='HTML')


@bot.message_handler(func=lambda message: message.text == "Школи")
def school_message(message):
    with open('images/schools.png', 'rb') as image:
        bot.send_photo(message.chat.id, photo=image)
    with open('schools.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(message.chat.id, text=text, parse_mode='HTML')


@bot.message_handler(func=lambda message: message.text == "Садки")
def kindergarten_message(message):
    with open('images/kids_garden.png', 'rb') as image:
        bot.send_photo(message.chat.id, photo=image)
    with open('gardens.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(message.chat.id, text=text, parse_mode='HTML')


@bot.message_handler(func=lambda message: message.text == "Гуртки")
def section_message(message):
    with open('images/hobbies.png', 'rb') as image:
        bot.send_photo(message.chat.id, photo=image)
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
    with open('images/chill.png', 'rb') as image:
        bot.send_photo(message.chat.id, photo=image)


@bot.message_handler(func=lambda message: message.text == "Салони краси")
def shelter_message(message):
    with open('images/beauty.png', 'rb') as image:
        bot.send_photo(message.chat.id, photo=image)
    with open('salons.txt', 'r', encoding='utf-8') as file:
        text = file.read()
        text = text.replace('%2B', '+')
    bot.send_message(message.chat.id, text=text, parse_mode='HTML')


@bot.message_handler(func=lambda message: message.text == "Готелі")
def hotel_message(message):
    with open('images/hotels.png', 'rb') as image:
        bot.send_photo(message.chat.id, photo=image)
    with open('hotels.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(message.chat.id, text=text, parse_mode='HTML')


@bot.message_handler(func=lambda message: message.text == "Ресторани/бари")
def bars_message(message):
    with open('images/restaraunts.png', 'rb') as image:
        bot.send_photo(message.chat.id, photo=image)
    with open('bar.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(message.chat.id, text=text, parse_mode='HTML')


@bot.message_handler(func=lambda message: message.text == "Фастфуд")
def fastfood_message(message):
    with open('images/fastfood.png', 'rb') as image:
        bot.send_photo(message.chat.id, photo=image)
    with open('fastfood.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(message.chat.id, text=text, parse_mode='HTML')


@bot.message_handler(func=lambda message: message.text == "Кафе")
def cafe_message(message):
    with open('images/cafe.png', 'rb') as image:
        bot.send_photo(message.chat.id, photo=image)
    with open('cafe.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(message.chat.id, text=text, parse_mode='HTML')


@bot.message_handler(func=lambda message: message.text == "Самбірська РО ТЧХУ")
def sambir_info_button(message):
    with open('images/sambir_logo.png', 'rb') as image:
        bot.send_photo(message.chat.id, photo=image)
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(types.KeyboardButton("Напрямки організації"), types.KeyboardButton("Отримати гуманітарну допомогу"),
                 types.KeyboardButton("Хочу стати волонтером"), types.KeyboardButton(MAIN_MENU_BUTTON))
    bot.send_message(message.chat.id, "Наша організація розвиває декілька напрямків:", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == "Напрямки організації")
def sambir_info_links(message):
    with open('help_directions.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(message.chat.id, text=text, parse_mode='HTML')
    bot.send_message(message.chat.id, "Instagram:\nhttps://www.instagram.com/redcross.sambir/?igshid=YmM0MjE2YWMzOA%3D%3D\n"
                                      "Facebook:\nhttps://www.facebook.com/profile.php?id=100083105293557")


@bot.message_handler(func=lambda message: message.text == "Отримати гуманітарну допомогу")
def get_hum_help(message):
    with open('humanitarian_aid_info.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(message.chat.id, text=text, parse_mode='HTML')
    bot.send_message(message.chat.id, "https://docs.google.com/forms/d/1OnLFgKkffS5UY2FvLlD0FRkZuTJ2Na0pYeQCDuUw9d8/viewform?edit_requested=true")
    bot.send_message(message.chat.id, "А також долучайся до наших соц.мереж❤️")
    bot.send_message(message.chat.id,
                    "Instagram:\nhttps://www.instagram.com/redcross.sambir/?igshid=YmM0MjE2YWMzOA%3D%3D\n"
                    "Facebook:\nhttps://www.facebook.com/profile.php?id=100083105293557")



@bot.message_handler(func=lambda message: message.text == "Хочу стати волонтером")
def volunteer(message):
    with open('volunteer.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(message.chat.id, text=text, parse_mode='HTML')
    bot.send_message(message.chat.id, "А також долучайся до наших соц.мереж❤️")
    bot.send_message(message.chat.id,
                     "Instagram:\nhttps://www.instagram.com/redcross.sambir/?igshid=YmM0MjE2YWMzOA%3D%3D\n"
                     "Facebook:\nhttps://www.facebook.com/profile.php?id=100083105293557")








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
