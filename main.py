    from flask import Flask, request
    import telebot
    import os

    app = Flask(__name__)
    TOKEN = '6209070455:AAHVf08Z-bCK2KaVUw60h2crCSgbFoVgmI8'
    bot = telebot.TeleBot(TOKEN)


    @bot.message_handler(commands=['start'])
    def message_start(message):
        bot.send_message(message.chat.id, 'hello, user')


    @app.route('/' + TOKEN, methods=['POST'])
    def get_message():
        bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
        return "Python Telegram Bot", 200


    @app.route('/')
    def main():
        bot.remove_webhook()
        bot.set_webhook(url='https://redcrossbot.herokuapp.com' + TOKEN)
        return 'Python Telegram Bot', 200


    @bot.message_handler(content_types=["text"])
    def repeat_all_messages(message):
        bot.send_message(message.chat.id, message.text)


    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

