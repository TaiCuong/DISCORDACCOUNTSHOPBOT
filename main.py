from config import API_TOKEN
import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = telebot.TeleBot(token=API_TOKEN)
# user_id = []
# @bot.message_handler(commands=['start'])
# def welcome(message):
#     welcome_text = f'Welcome {message.from_user.first_name} welcome DiscordShop OLD Account'
#     bot.send_message(message.chat.id, welcome_text)
#     if message.chat.id not in user_id:
#         user_id.append(message.chat.id)
# @bot.message_handler(commands=['help'])
# def send_update(message):
#     for id in user_id:
#         bot.send_message(id, "Please contact my tele @mmosp2021")
# @bot.message_handler(func=lambda message: True)
# def reply_func(message):
#     bot.reply_to(message, text="Please choose option on Menu")

button1 = InlineKeyboardButton(text="List Product", callback_data= "btn1")
button2 = InlineKeyboardButton(text="Referral", callback_data= "btn2")
button3 = InlineKeyboardButton(text="Contact with Admin", callback_data= "btn3")
button4 = InlineKeyboardButton(text="Choose language", callback_data= "btn4")
buttonClick = InlineKeyboardButton(text="Click to buy", callback_data= "btnclick")
buttonBack = InlineKeyboardButton(text="Back to menu", callback_data= "btnback")
buttonUS = InlineKeyboardButton(text="US", callback_data= "btnUS")
buttonVN = InlineKeyboardButton(text="US", callback_data= "btnVN")
inline_keyboard = InlineKeyboardMarkup(row_width=2)
inline_keyboard1 = InlineKeyboardMarkup(row_width=1)
inline_keyboard2 = InlineKeyboardMarkup(row_width=1)
inline_keyboardLanguage = InlineKeyboardMarkup(row_width=2)
inline_keyboardLanguage.add(buttonUS, buttonVN)
inline_keyboard.add(button1, button2,button3, button4)
inline_keyboard1.add(buttonClick)
inline_keyboard2.add(buttonBack)

user_id = []
@bot.message_handler(commands=['start'])
def welcome(message):
    welcome_text = f'Welcome {message.from_user.first_name} welcome DiscordShop OLD Account'
    bot.send_message(message.chat.id, "Welcome to Discord Shop NT",
                     reply_markup=inline_keyboard)


@bot.callback_query_handler(func= lambda call:True)
def check_button(call):
    if call.data == "btn1":
        bot.send_message(call.message.chat.id, "Đây là danh sách sản phẩm", reply_markup=inline_keyboard1)
    elif call.data == "btn2":
        bot.send_message(call.message.chat.id, "Tôi là Nguyễn Tài Cương", reply_markup=inline_keyboard2)
    elif call.data == "btn3":
        bot.send_message(call.message.chat.id, "Vui lòng liên hệ", reply_markup=inline_keyboard2)
    elif call.data == "btn4":
        bot.send_message(call.message.chat.id, "Chọn ngôn ngữ", reply_markup=inline_keyboardLanguage)
    elif call.data == "btnback":
        bot.send_message(call.message.chat.id, "Tôi là Nguyễn Tài Cương", reply_markup=inline_keyboard)
bot.polling()