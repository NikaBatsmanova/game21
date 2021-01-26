import telebot
from telebot import types

bot = telebot.TeleBot("1409664840:AAGjcvXHPWzKelC7pHhdejM5zsS-5Csuz_U")


@bot.message_handler(commands=['start'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, "Привет, я расскажу тебе про курс ЕГЭ по литературе на 80+ за полгода.")
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    about_course = types.InlineKeyboardButton(text="О курсе", callback_data='course')
    about_author = types.InlineKeyboardButton(text="Об авторе", callback_data='author')
    cost = types.InlineKeyboardButton(text="Стоимость", callback_data='the_cost')
    contacts = types.InlineKeyboardButton(text="Контакты", callback_data='the_contacts')
    reviews = types.InlineKeyboardButton(text="Отзывы", callback_data='the_reviews')
    link = types.InlineKeyboardButton(text="Ссылка на курс", callback_data='the_link')
    promo_link = types.InlineKeyboardButton(text="Ссылка на бесплатный промо-курс", callback_data='the_promo_link')
    keyboard.add(about_course, about_author, cost, reviews, contacts, promo_link, link)
    bot.send_message(message.from_user.id, "Выбери раздел", reply_markup=keyboard, parse_mode="Html")


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "course":
        msg1 = '''Авторский курс подготовки к экзамену по литературе рассчитан на 60 часов. Это 20 учебных недель по 2 занятия в неделю продолжительностью 90 минут - 1,5 часа. 
За это время вы прорешаете не менее 50 тестовых заданий ЕГЭ по литературе и напишете не менее 50 сочинений. Тесты с автоматической проверкой составлены в соответствии с критериями ФИПИ. 
После каждого занятия дается домашнее задание по той же теме, которая изучалась на занятии, на отработку решения каждого тестового задания и доведения этого умения до автоматизма, так, чтобы на экзамене вы смогли применить свои знания и решить все тесты правильно. 
Дома предлагается написать сочинение по образцу того, что было в видеоуроке, чтобы вы смогли научиться писать сочинения. Их проверяет до следующего занятия сертифицированный эксперт ЕГЭ по литературе, кандидат филологических наук, доцент кафедры русской и зарубежной филологии НГПУ им. К. Минина.'''
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg1)
    if call.data == "author":
        msg2 = ''' Меня зовут Диана Михайловна Шевцова. 
Я кандидат филологических наук, доцент кафедры культуры и психологии предпринимательства Нижегородского государственного университета имени Н.И.Лобачевского.

Я - профессиональный репетитор по литературе. 
С 2009 года успешно готовлю учеников к ЕГЭ по литературе.
Я помогаю всем ребятам, решившим сдать ЕГЭ по литературе, выучить этот предмет так, чтобы они могли уверенно сдать Единый государственный экзамен, получить высокий балл и поступить в ВУЗ своей мечты.  
Кроме того, я не понаслышке знаю все беды и боли своих учеников.
С сентября 2020 года со мной занимаются 100 учеников в месяц. 
Есть индивидуальные ученики – 70%, минигруппы (до 5 человек) – 30%. Работаю онлайн 3 года, сейчас 90% учеников онлайн – от Южно-Сахалинска до Калининграда! Проводила вебинарный курс по подготовке к ЕГЭ по литературе. 
В 2020 году лучший результат ЕГЭ по литературе - 100 баллов, средний балл 85.                                                                                
Средний балл моих учеников на 20 баллов выше среднего балла ЕГЭ. 
Ваши шансы сдать ЕГЭ и получить проходной балл в ВУЗ вашей мечты взлетают в 10 раз, если вы готовитесь со мной.
'''
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg2)
    if call.data == "the_cost":
        msg3 = ''' Тариф с поддержкой за весь курс обучения стоит 20 000 рублей.
Тариф без поддержки за весь курс обучения стоит 15 000 рублей.

Первый тариф предполагает проверку сочинений действующим экспертом ЕГЭ по литературе, кандидатом филологических наук, доцентом кафедры литературы. На втором – вы делаете всё самостоятельно.

Если вам не интересен данный курс, но у вас есть знакомые или ученики, которым он может быть полезен, я заплачу 2 000 рублей за рекомендацию (после оплаты курса учеником, которого вы приведете).  
'''
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg3)
    if call.data == "the_contacts":
        msg4 = '''Если у вас еще остались вопросы, 
вы можете написать мне на Электронный адрес: dshevcova@mail.ru
связаться со мной через мессенджеры:
Телеграмм https://t-do.ru/Diana_Mihailovna1
Вайбер https://viber.click/79519141026
Ватсап https://wa.me/79519141026
'''
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg4)
    if call.data == "the_link":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        url_button = types.InlineKeyboardButton(text="Курс ЕГЭ по литературе на 80+ за полгода",
                                                url="https://get.tutorsmart.ru/ege_in_literature_at_80_points")
        keyboard.add(url_button)
        bot.send_message(call.message.chat.id, "Нажми на кнопку и перейди на страницу курса", reply_markup=keyboard, parse_mode="Html")
    if call.data == "the_promo_link":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        url_button = types.InlineKeyboardButton(text="Бесплатный промо-курс",
                                                url="https://get.tutorsmart.ru/promo_ege_in_literature_at_80_points")
        keyboard.add(url_button)
        bot.send_message(call.message.chat.id, "Нажми на кнопку и перейди на страницу промо-курса 5 шагов для успешной сдачи ЕГЭ по литературе", reply_markup=keyboard, parse_mode="Html")
    if call.data == "the_reviews":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="Профи.ру",
                                                 url="https://profi.ru/profile/ShevtsovaDM/")
        url_button2 = types.InlineKeyboardButton(text="ВашРепетитор",
                                                 url="https://nnov.repetitors.info/comments.php?p=ShevtsovaDM")
        keyboard.add(url_button1, url_button2)
        bot.send_message(call.message.chat.id, "Нажми на кнопку и перейди на страницу отзывов", reply_markup=keyboard, parse_mode="Html")

@bot.message_handler(content_types=["text"])
def default_test(message):
    bot.send_message(message.chat.id, "Извините, я вас не понимаю, чтобы получить информацию напишите /start")


bot.polling()
