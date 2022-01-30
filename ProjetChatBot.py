# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 23:49:45 2022

@author: azuz
"""

import telebot
from telebot import types

#API Générer par BotFather sur instagram pour permettre la création du chatbot

API_KEY = "5193249564:AAEjTuL-JBGh8rTFJjR5aoW1vt6lV7VU2IM"

#Connexion au chatbot

bot = telebot.TeleBot(API_KEY)

objectif="=========================================================\n \
    Hello! Welcome dear customer, we are all ear. This bot will take care of you in this out of time service.\
    We will come back to you soon as possible. To start let's make some greeting /hello.\n \
    =========================================================\n "

options="Hello! This chatbot exist to help customer to verify validity of client's code with \
    the suites options:\n \
    1) To access to main menu type: /Main_Menu \n \
    2) To relance new research type: /New_search \n \
    3) To close session type: /End"

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message,objectif)
    
@bot.message_handler(commands=['hello'])
def hello(message):
    bot.send_message(message.chat.id, options)
    markup=types.ReplyKeyboardMarkup(row_width=3)
    option1=types.KeyboardButton("/hello")
    option2=types.KeyboardButton("/Main_Menu")
    option3=types.KeyboardButton("/track_my_code")
    option4=types.KeyboardButton("/New_search")
    option5=types.KeyboardButton("/Other")
    option6=types.KeyboardButton("/End")
    
    markup.add(option1,option2,option3,option4,option5,option6)
    bot.send_message(chat_id=message.chat.id,text="",reply_markup=markup)
    
@bot.message_handler(commands=["Main_Menu"])
def Main_Menu(message):
    bot.reply_to(message,"You can access to two options in this method:\n\
    1) You can track your customer code with this method: /track_my_code\n\
    2)For other sercices press or type this: /Other")
    
@bot.message_handler(commands=["track_my_code"])
def track_my_code(message):
    bot.reply_to(message,"Please type your code:")
    code=int(input("Please type your code:"))

    if code in range(100):
        
        bot.reply_to(message,"Your code is on the system.You can continue with /New_search, /Main_Menu or /End")
    
    else:
    
        bot.reply_to(message,"Your code is not on the system. You can retry again /New_search, /Main_menu or /End")

@bot.message_handler(commands=["Other"])
def Other(message):
    bot.reply_to(message,"Sorry, they aren't currently other service. Go back to /Main_Menu")


@bot.message_handler(commands=["New_search"])
def New_search(message):
    return track_my_code(message)

@bot.message_handler(commands=["End"])
def End(message):
    bot.reply_to(message,"Bot is idled. See you next time!!!")

@bot.message_handler(func=lambda msg: msg.from_user)
def handle_out_box_message(msg):
    bot.reply_to(msg,"Sorry! Did you mean /Main_Menu ?")

bot.polling()