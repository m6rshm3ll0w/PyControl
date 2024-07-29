import time
import os
from dotenv import dotenv_values
from telebot import *
import socket
import cv2
import subprocess
import time
from tkinter import *
import pyautogui

UPD_PATH = "../upd/upd.exe"

config = dotenv_values("data/.env")

TOKEN = config["TOKEN"]
USER_ID = config["USR_ID"]
BOT_ID = config["BOT_ID"]
VERSION = config["VERSION"]

bot = telebot.TeleBot(TOKEN)
print("###################################\n"
      "             BOT STARTED           \n"
      "###################################")

global TIME


@bot.message_handler(commands=['await_start'])
def await_start(message):
    if message.from_user.id == int(USER_ID) or message.from_user.id == int(BOT_ID):
        select = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("/start", callback_data='main_menu1')
        btn2 = types.InlineKeyboardButton("/await_start", callback_data='await_start')
        select.add(btn1)
        select.add(btn2)
        bot.send_message(chat_id=message.chat.id, text=f'Привет, Бот только что был запущен на компьютере:\n '
                                                       f'"{socket.gethostname()}", если ты нажал или написал,'
                                                       f' /start (вызов главного меню)\n'
                                                       f'a бот не отвечает, то компьютер выключили\n'
                                                       f'V{VERSION}',
                         reply_markup=select)
    else:
        app_link = types.InlineKeyboardMarkup()
        webAppTest = types.WebAppInfo("https://m6rshm3ll0w.github.io")
        link_to_app = types.InlineKeyboardButton("PyControl", web_app=webAppTest)
        app_link.add(link_to_app)
        bot.send_message(message.chat.id,
                         f"Привет @{message.from_user.username}, для настройки своего бота скачай исходники и "
                         f"подключи своего бота из приложения ниже!!!", reply_markup=app_link)


@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.id == int(USER_ID) or message.from_user.id == int(BOT_ID):
        msg = bot.send_message(chat_id=message.chat.id, text='Привет, Идет верефикация....')
        main_menu(msg)
    else:
        app_link = types.InlineKeyboardMarkup()
        webAppTest = types.WebAppInfo("https://m6rshm3ll0w.github.io")
        link_to_app = types.InlineKeyboardButton("PyControl", web_app=webAppTest)
        app_link.add(link_to_app)
        bot.send_message(message.chat.id, f"Привет @{message.from_user.username}, для настройки своего бота скачай "
                                          f"исходники и подключи своего бота из приложения ниже!!!",
                         reply_markup=app_link)


def main_menu(message):
    print(f">>> func(start) run by command /start            <{message.from_user.id} : {message.chat.id}>")
    time.sleep(0.5)
    select = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton("заблокировать пк", callback_data='lock_pc')
    btn2 = types.InlineKeyboardButton("Скриншот.", callback_data='scr')
    btn21 = types.InlineKeyboardButton("Фото", callback_data='photo')
    btn3 = types.InlineKeyboardButton("Перезагрузить пк", callback_data='restart_pc')
    btn4 = types.InlineKeyboardButton("Отмена", callback_data='undo_restart_pc')
    btn5 = types.InlineKeyboardButton("Alt+F4", callback_data='close_app')

    nome = types.InlineKeyboardButton("BSod", callback_data='bsod')

    cent = types.InlineKeyboardButton("1/2", callback_data='0')
    left_m = types.InlineKeyboardButton(">>", callback_data="main_menu2")

    select.add(btn1)
    select.add(btn2, btn21)
    select.add(btn3, btn4)
    select.add(btn5, nome)
    select.add(cent, left_m)
    bot.send_message(chat_id=message.chat.id, text=f"Главное меню V{VERSION}:",
                     reply_markup=select)
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


def main_menu2(message):
    print(f">>> func(start) run by command /start            <{message.from_user.id} : {message.chat.id}>")
    time.sleep(0.5)
    select = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton("Загрузить обновление", callback_data='upload_update')
    btn2 = types.InlineKeyboardButton("Блюр экрана", callback_data='blur')
    right_m = types.InlineKeyboardButton("<<", callback_data="main_menu1")
    cent = types.InlineKeyboardButton("2/1", callback_data='0')

    select.add(btn1)
    select.add(btn2)
    select.add(right_m, cent)
    bot.send_message(chat_id=message.chat.id, text=f"Главное меню V{VERSION}:",
                     reply_markup=select)
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


def upload_upd(message):
    bot.send_message(chat_id=message.chat.id, text=f"Загрузи в этот чат обновление в формате upd.exe размером до 50 мб"
                                                   f"(можно одно обновление разбить на патчи),"
                                                   f" текущая версия - {VERSION}")
    bot.register_next_step_handler(message, save_upd)
    bot.delete_message(message_id=message.id, chat_id=message.chat.id)


def install_upd(message):
    bot.send_message(chat_id=message.chat.id, text='Через 2 секунды бот отключится и выполнит обновление!\n'
                                                   'Для проверки работоспособности введите /await_start'
                                                   ' и подождите до вывода сообщения!')
    bot.delete_message(message_id=message.id, chat_id=message.chat.id)
    time.sleep(2)
    run_installer()


def scr(message):
    print(f">>> func(scr) run by Callback Data 'scr'            <{message.from_user.id} : {message.chat.id}>")
    im1 = pyautogui.screenshot()
    im1.save(r"data/img/git.png")
    photo = open('data/img/git.png', 'rb')
    select = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("вернуться в главное меню", callback_data='main_menu1')
    select.add(btn1)
    bot.send_photo(message.chat.id, photo, caption="Скриншот экрана пк", reply_markup=select)
    bot.delete_message(message.chat.id, message_id=message.message_id)


def photo(message):
    print(f">>> func(scr) run by Callback Data 'scr'            <{message.from_user.id} : {message.chat.id}>")
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite('data/img/cam.png', frame)
    cap.release()
    photo = open('data/img/cam.png', 'rb')
    select = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("вернуться в главное меню", callback_data='main_menu1')
    select.add(btn1)
    bot.send_photo(message.chat.id, photo, caption="Снимок", reply_markup=select)
    bot.delete_message(message.chat.id, message_id=message.message_id)


def select_fon(message):
    select = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("1.figures", callback_data='lock_pc_first_img')
    btn2 = types.InlineKeyboardButton("2.girls", callback_data='lock_pc_second_img')
    select.add(btn1)
    select.add(btn2)

    bot.send_photo(message.chat.id, open('data/img/prevu.png', 'rb'),
                   caption=f"Выбери картинку:\n"
                           f"разрешение экрана {pyautogui.size()};\n"
                           f" разрешение изображений 1920x1080", reply_markup=select)

    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


def lock(message, img):
    print(f">>> func(lock) run by callback(lock)           <{message.from_user.id} : {message.chat.id}>")
    msg = bot.send_message(message.chat.id, f"введи кол-во секунд на которое заблокируетсся пк....")
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    bot.register_next_step_handler(message, lock_m, img, msg)


def lock_m(message, img, msg):
    try:
        bot.delete_message(chat_id=message.chat.id, message_id=msg.message_id)
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        msg = bot.send_message(message.chat.id, f"рабочий стол заблокирован на {int(message.text)} секунд(ды)")
        helpful(int(message.text), img)
        message = bot.edit_message_text(chat_id=message.chat.id, text='Блокировка снята!', message_id=msg.message_id)

        main_menu(message)
    except ValueError:
        bot.send_message(message.chat.id, f"Что - то не так, ЧИСЛО в СЕКУНДАХ....")
        lock(message, img)


def helpful(tt, ds):
    root = Tk()
    x = -2
    y = -2
    if ds == 1:
        abc = PhotoImage(file='data\\img\\figures1.png')
        Label(root, image=abc).pack()
    elif ds == 2:
        abc = PhotoImage(file='data\\img\\mas.png')
        Label(root, image=abc).pack()
    elif ds == 3:
        abc = PhotoImage(file='data\\img\\blur.png')
        Label(root, image=abc).pack()

    root.overrideredirect(True)
    root.lift()
    root.wm_attributes("-topmost", True)
    root.wm_attributes("-disabled", True)
    root.geometry(f'+{x}+{y}')
    root.update()
    time.sleep(tt)
    root.destroy()
    root.mainloop()


def restart():
    subprocess.run(["data\\bats\\rs.bat"])


def call_bsod():
    subprocess.run(["data\\bats\\BSoD.bat"])


def undo_restart():
    subprocess.run(["data\\bats\\usr.bat"])


def close_ap():
    pyautogui.hotkey('alt', 'f4')


def run_installer():
    subprocess.run(["..\\upd\\main.vbs"])


@bot.message_handler(content_types=['document'])
def save_upd(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="нет, я загрузил не тот файл",
                                      callback_data="upload_update")
    btn2 = types.InlineKeyboardButton(text="да, я подтверждаю, что загрузил правильный файл",
                                      callback_data="install_update")
    markup.add(btn1)
    markup.add(btn2)
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    with open(UPD_PATH, 'wb') as new_file:
        new_file.write(downloaded_file)
        new_file.close()

    bot.send_message(chat_id=message.chat.id, text="Хорошо, обновление загружено.\n"
                                                   "желаешь выполнить обновление?",
                     reply_markup=markup)
    bot.delete_message(message_id=message.id, chat_id=message.chat.id)


@bot.callback_query_handler(func=lambda callback: True)
def handle_query(callback):
    if callback.data == 'scr':
        time.sleep(1);
        scr(callback.message)

    elif callback.data == '0':
        pass

    elif callback.data == 'photo':
        time.sleep(1);
        photo(callback.message)

    elif callback.data == 'upload_update':
        time.sleep(1);
        upload_upd(callback.message)

    elif callback.data == 'install_update':
        time.sleep(1);
        run_installer()

    elif callback.data == 'info':
        time.sleep(1);
        await_start(callback.message)

    elif callback.data == 'lock_pc':
        time.sleep(0.5);
        select_fon(callback.message)

    elif callback.data == 'lock_pc_first_img':
        time.sleep(1);
        lock(callback.message, img=1)

    elif callback.data == 'lock_pc_second_img':
        time.sleep(1);
        lock(callback.message, img=2)

    elif callback.data == "blur":
        time.sleep(1);
        lock(callback.message, img=3)

    elif callback.data == 'main_menu1':
        time.sleep(1)
        main_menu(callback.message)

    elif callback.data == 'main_menu2':
        time.sleep(1)
        main_menu2(callback.message)

    elif callback.data == 'restart_pc':
        bot.edit_message_text(chat_id=callback.message.chat.id,
                              text=f"Перезагрузка пк через 20 секунд....",
                              message_id=callback.message.message_id)

        restart()
        main_menu(callback.message)

    elif callback.data == 'undo_restart_pc':
        bot.edit_message_text(chat_id=callback.message.chat.id,
                              text="Перезагрузка отменена!",
                              message_id=callback.message.message_id)

        undo_restart()
        main_menu(callback.message)

    elif callback.data == 'bsod':
        bot.edit_message_text(chat_id=callback.message.chat.id,
                              text="Bsod вызван!!!",
                              message_id=callback.message.message_id)

        call_bsod()
        main_menu(callback.message)

    elif callback.data == 'close_app':
        bot.edit_message_text(chat_id=callback.message.chat.id,
                              text="Нажато Alt+F4",
                              message_id=callback.message.message_id)

        close_ap()
        main_menu(callback.message)


bot.infinity_polling()
