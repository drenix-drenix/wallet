api_id = 18205337
api_hash = "811f1c33307e74726e6464b040b5a964"
chatsid = ["@tonchequesss", "@FlRST_TON", "@xRocketDropsPrem", "@TON_DROP_SAKE", "@chequehunters", "@TonTonich01", "@Pa4kaTon", "@tonchb", "@TonFastRu", "@TonKoin607", "@fre_ton", "@chekitonwallet", "@CrazyProfitHyip", "@BearMoney", "@cryptomirtv", "@cryptoboss007e", "https://t.me/+3cW0QLNcapU1NDFl", "@toncoinforfree", "@mcojn", "@ton_buzz", "@CryptoLifeTon", "https://t.me/+X3a1DVAbVycwZDgy", "@chequesTonn", "https://t.me/+Ztw5vGk6xY8yNzBi", "@tonchecksuz", "@Ton_checki", "@botsmoneytgtg", "@toncheckswallet", "@viadecode", "@FreeTONDrops", "@PONA_TON", "@TONKAZI", "@TheTonChecks", "@cheki_ledok", "@qiwixznz", "@Betta_Money", "@kriptoCheki", "@ton_drops_me_wallet", "@easy_m0neeey", "@GENERATOR_TON", "@tonrokew", "@CryptoSharks73", "@topchecks2023", "https://t.me/+Xvcs4VeoElM1YmFi", "@chequesdrops", "@tonpriton1", "@xRocketMoney", "@anmonn8", "@tonfarm1338", "@walletcheki", "@ChequesRu", "@CryptoChekinGram", "https://t.me/+xcp6NXbcUvwxMjZi", "@chekists1", "@tonscheques", "@Crypto_checke", "@ton_botton", "https://t.me/+vlgMenfmW29kNDUy", "@rt_crypto", "@Free_Cheques", "https://t.me/+WGpYqp6YxcFhMjJi", "@eyeofthebomj", "@checikytakbawa", "@crypto_world_ton", "@ScrgCrypto", "@CryptoTon906", "@WalletCHek", "@cryptotoninvestton", "@cryptoworld888128", "@dearroket", "@chekiwallet", "@chekiotkotika", "@usdtaway", "@TONthec", "@free_toncoinn", "@xalyavaton"] 


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
		Client("20")
		]
		
worker = Client("1")

select = int(input('Выберите режим, 1 - запуск, 2 - подписка, 3 - отписка, 4 - создание сессии:'))


#worker.start()
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
