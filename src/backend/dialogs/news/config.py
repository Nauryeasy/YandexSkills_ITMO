message = \
    """
    Вы направились в категорию "Новости".
    Выберите раздел новости, которую хотите посмотреть. Анонсы или Контесты.
    """

tts = \
    """
    Вы направились в категорию "Новости".
    Выберите раздел новости, которую хотите посмотреть.
    Первое - это Анонсы.
    Второе - это Контесты.
    """

buttons = [
    "Анонсы",
    "Контесты",
    "Назад",
    "Выйти",
    "Помощь"
]

card = {
    'type': 'BigImage',
    'image_id': '937455/40f0536e426907808499',
    'title': 'НОВОСТИ',
    'description': \
        """
        Выберите раздел новостей: Анонсы или Контесты.
        """
}

session_state = {
    "branch": "news"
}


def getConfig():
    return {
        'message': message,
        'tts': tts,
        'buttons': buttons,
        'card': card,
        'session_state': session_state
    }
