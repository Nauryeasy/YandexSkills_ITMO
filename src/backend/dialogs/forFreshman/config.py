message = \
    """
    Вы направились в категорию "Первокурсникам"
    
    Друзья, поздравляем! Стартовал ваш первый учебный год  в Университете ИТМО!
    
    Все вопросы, возникающие во время обучения, можно решить если перейти по ссылке - https://student.itmo.ru/ru/. Например, узнать о процессе обучения в ИТМО, можно по ссылке  -https://student.itmo.ru/ru/edu_time/.
    
    Мобильные приложения
    Чтобы всегда быть в теме, скачивайте полезные мобильные приложения для студентов Университета ИТМО:
    
    Приложение на IOS  называется - my.itmo
    Приложение на Android называется - my.itmo
    """
 
tts = \
    """
    Вы направились в категорию "Первокурсникам".
    
    Друзья. Поздравляем! Стартовал ваш первый учебный год в Университете ИТМО!
    
    Все вопросы, возникающие во время обучения, можно решить если нажать на кнопку "ИТМО".
   
    Чтобы всегда быть в теме, скачивайте полезные мобильные приложения для студентов Университета ИТМО.
    
    Приложение на IOS и на Android называется - my.itmo
    """

buttons = [
    "Повторить ещё раз",
    "Помощь",
    "Назад",
    "Выйти"  
]

card = {
    'type': 'BigImage',
    'image_id': '937455/40f0536e426907808499',
    'title': 'ПЕРВОКУРСНИКАМ',
    'description': \
        """
        Все вопросы, возникающие во время обучения, можно решить если перейти по ссылке - https://student.itmo.ru/ru/. Например, узнать о процессе обучения в ИТМО, можно по ссылке - https://student.itmo.ru/ru/edu_time/.

        """
}

session_state = {
    "branch": "forFreshman"
}


def getConfig():
    return {
        'message': message,
        'tts': tts,
        'buttons': buttons,
        'card': card,
        'session_state': session_state
    }
