import telebot
from telebot import types
from config import pesan, tokenBot
import views, time

bot = telebot.TeleBot(tokenBot, threaded=False)

def makrup_paksa():
    return types.ForceReply(selective=False)

def inlineForWali():
	markup = types.InlineKeyboardMarkup()
	markup.row(
		types.InlineKeyboardButton("Absensi", callback_data="absensi"),
		types.InlineKeyboardButton("Bantuan", callback_data="bantuan"),
	)
	markup.row(
		types.InlineKeyboardButton("Hubungi Kami", url="t.me/allezaen"),
	)

	return markup

@bot.message_handler(commands=["start", "help"])
def mulaiBot(m):
    pilihan = m.text
    if pilihan == "/start":
        bot.send_message(m.chat.id, "Selamat Datang", reply_markup=inlineForWali())
    elif pilihan == "/help":
        bot.send_message(m.chat.id, "Silahkan dipilih", reply_markup=inlineForWali())

def absensi(m):
    msg = bot.send_message(m.chat.id, "Masukkan Nama yang mau di cari", reply_markup=makrup_paksa())
    bot.register_next_step_handler(msg, proses_absensi)

def proses_absensi(m):
    nama = m.text.lower()
    data = views.cariNama(nama)
    if data:
        for i in data:
            bot.send_message(m.chat.id, i)
    else:
        bot.send_message(m.chat.id, pesan["tidak_ditemukan"])

def bantuan(m):
    bot.send_message(m.chat.id, pesan["bantuan"])

@bot.callback_query_handler(func=lambda call: True)
def callbarQuery(c):
	try:
		if c.data == 'absensi':
			absensi(c.message)
		elif c.data == 'bantuan':
			bantuan(c.message)
	except Exception as e:
		print(e)

def telegram_polling():
	try:
		bot.polling(none_stop=True)
	except Exception:
		bot.stop_polling()
		time.sleep(5)
		telegram_polling()

if __name__ == '__main__':
	telegram_polling()
