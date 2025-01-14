message = \
    """
    Вопрос:
    Зачем мне обращаться в Студенческий офис?
    
    Ответ:
    Через студенческий офис вы можете:
    получить любую справку.
    продлить/заменить студенческий билет.
    заменить паспортные данные.
    продлить сессию по уважительной причине.
    подать заявление на академический отпуск / перевод / восстановление / отчисление.
    временно получить свой документ об образовании (аттестат/диплом).
    """

tts = \
    """
    Через студенческий офис вы можете:
    получить любую справку.
    продлить или заменить студенческий билет.
    заменить паспортные данные.
    продлить сессию по уважительной причине.
    подать заявление на академический отпуск, перевод, восстановление, отчисление.
    временно получить свой документ об образовании. Аттестат или диплом.
    """

buttons = [
    "Повторить ещё раз",
    "Помощь"
    "Назад",
    "Выйти",
]

card = {
    'type': 'BigImage',
    'image_id': '937455/40f0536e426907808499',
    'title': 'ЗАЧЕМ МНЕ ОБРАЩАТЬСЯ В СТУДЕНЧЕСКИЙ ОФИС?',
    'description': \
        """
        Через студенческий офис вы можете: получить любую справку, продлить/заменить студенческий билет; заменить паспортные данные, продлить сессию по уважительной причине, подать заявление на академический отпуск / перевод / восстановление / отчисление, временно получить свой документ об образовании (аттестат/диплом).
        """
}

session_state = {
    "branch": "studentOffice"
}


def getConfig():
    return {
        'message': message,
        'tts': tts,
        'buttons': buttons,
        'card': card,
        'session_state': session_state
    }
