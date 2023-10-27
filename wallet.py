#!/usr/bin/python3.8
api_id = 18205337
api_hash = "811f1c33307e74726e6464b040b5a964"
chatsid = ["https://t.me/tonchequesss", "https://t.me/FlRST_TON", "https://t.me/xRocketDropsPrem", "https://t.me/TON_DROP_SAKE", "https://t.me/chequehunters", "https://t.me/TonTonich01", "https://t.me/Pa4kaTon", "https://t.me/tonchb", "https://t.me/TonFastRu", "https://t.me/TonKoin607", "https://t.me/fre_ton", "https://t.me/chekitonwallet", "https://t.me/CrazyProfitHyip", "https://t.me/BearMoney", "https://t.me/cryptomirtv", "https://t.me/cryptoboss007e", "https://t.me/+3cW0QLNcapU1NDFl", "https://t.me/toncoinforfree", "https://t.me/mcojn", "https://t.me/ton_buzz", "https://t.me/CryptoLifeTon", "https://t.me/+X3a1DVAbVycwZDgy", "https://t.me/chequesTonn", "https://t.me/+Ztw5vGk6xY8yNzBi", "https://t.me/tonchecksuz", "https://t.me/Ton_checki", "https://t.me/botsmoneytgtg", "https://t.me/toncheckswallet", "https://t.me/viadecode", "https://t.me/FreeTONDrops", "https://t.me/PONA_TON", "https://t.me/TONKAZI", "https://t.me/TheTonChecks", "https://t.me/cheki_ledok", "https://t.me/qiwixznz", "https://t.me/Betta_Money", "https://t.me/kriptoCheki", "https://t.me/ton_drops_me_wallet", "https://t.me/easy_m0neeey", "https://t.me/GENERATOR_TON", "https://t.me/tonrokew", "https://t.me/CryptoSharks73", "https://t.me/topchecks2023", "https://t.me/+Xvcs4VeoElM1YmFi", "https://t.me/chequesdrops", "https://t.me/tonpriton1", "https://t.me/xRocketMoney", "https://t.me/anmonn8", "https://t.me/tonfarm1338", "https://t.me/walletcheki", "https://t.me/ChequesRu", "https://t.me/CryptoChekinGram", "https://t.me/+xcp6NXbcUvwxMjZi", "https://t.me/chekists1", "https://t.me/tonscheques", "https://t.me/Crypto_checke", "https://t.me/ton_botton", "https://t.me/+vlgMenfmW29kNDUy", "https://t.me/rt_crypto", "https://t.me/Free_Cheques", "https://t.me/+WGpYqp6YxcFhMjJi", "https://t.me/eyeofthebomj", "https://t.me/checikytakbawa", "https://t.me/crypto_world_ton", "https://t.me/ScrgCrypto", "https://t.me/CryptoTon906", "https://t.me/WalletCHek", "https://t.me/cryptotoninvestton", "https://t.me/cryptoworld888128", "https://t.me/dearroket", "https://t.me/chekiwallet", "https://t.me/chekiotkotika", "https://t.me/usdtaway", "https://t.me/TONthec", "https://t.me/free_toncoinn", "https://t.me/xalyavaton"] 


from pyrogram import Client, filters, enums,idle,filters
from pyrogram.handlers import MessageHandler
import asyncio

apps = [
		Client("2"),
	  Client("3"),
	  Client("4"),
    Client("5"),
    Client("6"),
    Client("7"),
    Client("8"),
		Client("9"),
		Client("10"),
		Client("11"),
		Client("12"),
		Client("13"),
		Client("14"),
		Client("15"),
		Client("16"),
		Client("17"),
		Client("18"),
		Client("19"),
		]
		
worker = Client("1")

select = int(input('Выберите режим, 1 - запуск, 2 - подписка, 3 - отписка, 4 - создание сессии:'))


worker.start()
async def wallet(app, message):
    try:
        if "Вы не можете активировать этот чек, так как вы не являетесь подписчиком канала" in message.text or\
            "You cannot activate this cheque because you are not a member of the channel" in message.text:
            chatlink = message.reply_markup.inline_keyboard[0][0].url
            chequelink = message.reply_markup.inline_keyboard[1][0].url[26:]
            chequeusername = message.reply_markup.inline_keyboard[0][0].text
            
            await app.join_chat(chatlink)
            await asyncio.sleep(1)
            await app.send_message("wallet", f"/start {chequelink}")
            await asyncio.sleep(84000)
            await app.leave_chat(chequeusername)
            
        elif "Вы получили" in message.text or "You received" in message.text:
            print("Чек собран!")
            
        elif "Этот чек уже активирован" in message.text or\
             "This cheque has already been activated" in message.text:
            print("Чек активирован ранее!")
            
        elif "К сожалению, другие пользователи уже собрали все средства" in message.text or\
             "Unfortunately, other users have collected all the funds" in message.text:
            print("Чек закончился!")
            
        else:
            print("Неизвестный запрос,ошибка,бан аккаунта или обработка чека")
    except:
        pass
    
async def findcheque(client, message):
    try:
        if message.reply_markup.inline_keyboard[0][0].url.startswith("https://t.me/wallet?start="):
            print(message.chat.title)
            print('Найден чек!')
            code = message.reply_markup.inline_keyboard[0][0].url[26:]
            await worker.send_message("wallet", f"/start {code}")
            for app in apps:
                await app.send_message("wallet", f"/start {code}")
    except:
        pass
    try:
        if "https://t.me/wallet?start=" in message.text:
            print(message.chat.title)
            print('Найден чек!')
            first = message.text.find("https://t.me/wallet?start=")
            last = message.text[first:].find(" ")
            if last == -1:
                code = message.text[first:].replace("https://t.me/wallet?start=","")
                await worker.send_message("wallet", f"/start {code}")
                for app in apps:
                    await app.send_message("wallet", f"/start {code}")
            else:
                code = message.text[first:last].replace("https://t.me/wallet?start=","")
                await worker.send_message("wallet", f"/start {code}")
                for app in apps:
                    await app.send_message("wallet", f"/start {code}")
    except:
        pass
    try:
        if "https://t.me/wallet?start=" in message.entities[0].url:
            print(message.chat.title)
            print('Найден чек!')
            code = message.entities[0].url.replace("https://t.me/wallet?start=","")
            await worker.send_message("wallet", f"/start {code}")
            for app in apps:
                await app.send_message("wallet", f"/start {code}")
        
    except:
        pass

if select == 1:
    async def main():	
        count_start = 0
        for app in apps:
            await app.start()
            app.add_handler(MessageHandler(wallet,filters.chat("wallet") & ~filters.me)) 
            count_start+=1
            print(f"Аккаунтов запущено:{count_start}")
            
        worker.add_handler(MessageHandler(findcheque,filters.chat(chatsid)))
        worker.add_handler(MessageHandler(wallet,filters.chat("wallet") & ~filters.me)) 
             
        print('Запущено!')
        try:
            await idle()
        except KeyboardInterrupt:
            for app in apps:
                try:
                    await app.stop()
                except:
                    pass
            worker.stop()
              
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    
elif select == 2:
    count_start = 0
    for app in apps:
        app.start()
        count_start+=1
        print(f"Аккаунтов запущено:{count_start}")
  
    while True:
        channel = input("Введите юзер,ссылку или приват ссылку:")
        if "https://t.me/" in channel and "https://t.me/+" not in channel:
            channel = channel.replace("https://t.me/","@")
    
        try:
            worker.join_chat(channel)
            print('Успешно Подписано!')
        except:
            print('Вы уже подписаны или возникла ошибка')
     
        for app in apps:
            try:
                app.join_chat(channel)
                print('Успешно Подписано!')
            except:
                print('Вы уже подписаны или возникла ошибка')
                
elif select == 3:
    count_start = 0
    for app in apps:
        app.start()      
        count_start+=1
        print(f"Аккаунтов запущено:{count_start}")
        
    while True:
        channel = input("Введите юзер,ссылку или приват ссылку:")
        if "https://t.me/" in channel and "https://t.me/+" not in channel:
            channel = channel.replace("https://t.me/","@")

        try:
            worker.join_chat(channel)
            print('Успешно Отписано!')
        except:
            print('Возникла ошибка!')
       
        for app in apps:
            try:
                app.leave_chat(channel)
                print('Успешно Отписано!')
            except Exception as e:
                #print(e)
                print('Возникла ошибка!')
                
                                   
elif select == 4:
    name = input("Введите имя аккаунта:")
    
    app = Client(name,api_id=api_id,api_hash=api_hash,password="drenix444")
    app.start()
    
    info_me = app.get_me()
    
    print(f"Аккаунт уже создан: {info_me.first_name}(+{info_me.phone_number})(@{info_me.username})")
    app.stop()
