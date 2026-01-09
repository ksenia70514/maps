from telegram.ext import Updater, CommandHandler
import logic


def start(update, context):
    update.message.reply_text("Привет! Я могу показать карту с городами. Используйте /all_cities или /city <название>.")

def show_all_cities(update, context):
    cities = get_all_cities()  
    filename = logic.create_graph(cities)
    update.message.reply_photo(open(filename, 'rb'))

def show_city(update, context):
    city_name = ' '.join(context.args)
    city = get_city_by_name(city_name)  
        filename = logic.create_graph([city])  
        update.message.reply_photo(open(filename, 'rb'))
    else:
        update.message.reply_text("Город не найден!")


def main():
    updater = Updater('TOKEN')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('all_cities', show_all_cities))
    dp.add_handler(CommandHandler('city', show_city, pass_args=True))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
color_choice = 'red' 

def set_color(update, context):
    global color_choice
    if context.args:
        color_choice = context.args[0]
        update.message.reply_text(f"Цвет маркеров установлен: {color_choice}")
    else:
        update.message.reply_text("Пожалуйста, укажите цвет, например: /set_color blue")
    main()
