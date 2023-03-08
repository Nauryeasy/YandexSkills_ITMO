def student_office_about(event, context):
    buttons = {
        'suggests': [
            '<buttons>'
        ]
    }
    return {
        'response': {
            'text':
                """
Студенческий офис – это компас студента в мире сложных и непонятных вопросов. 
Менеджеры офиса вряд ли помогут решить задачу по математике, но точно подскажут,
как заселиться в общежитие или получить социальную стипендию.
                """,
            'tts':
                """
Студенческий офис – это компас студента в мире сложных и непонятных вопросов. 
Менеджеры офиса вряд ли помогут решить задачу по математике, но точно подскажут,
как заселиться в общежитие или получить социальную стипендию.
                """,
            'card': {
                'type': 'BigImage',
                'image_id': '937455/40f0536e426907808499',
                'title': 'Студенческий офис',
                'description':
                    """
Студенческий офис – это компас студента в мире сложных и непонятных вопросов. 
Менеджеры офиса вряд ли помогут решить задачу по математике, но точно подскажут,
как заселиться в общежитие или получить социальную стипендию.
                """,
            },
            'buttons': [
                {
                    'title': title,
                    'payload': {},
                    'hide': 'true'
                } for title in buttons['suggests']
            ],
            'end': 'false'
        },
        'session': event['session'],
        'session_state': {
            'branch': 'student_office'
        },
        'version': event['version']
    }


def student_office_for_what(event, context):
    buttons = {
        'suggests': [
            '<buttons>'
        ]
    }
    return {
        'response': {
            'text':
                """
Через студенческий офис вы можете:
· получить любую справку;
· продлить/заменить студенческий билет;
· заменить паспортные данные;
· продлить сессию по уважительной причине;
· подать заявление на академический отпуск / перевод / восстановление / отчисление;
· временно получить свой документ об образовании (аттестат/диплом).
                """,
            'tts':
                """
Через студенческий офис вы можете:
· получить любую справку;
· продлить/заменить студенческий билет;
· заменить паспортные данные;
· продлить сессию по уважительной причине;
· подать заявление на академический отпуск / перевод / восстановление / отчисление;
· временно получить свой документ об образовании (аттестат/диплом).
                """,
            'card': {
                'type': 'BigImage',
                'image_id': '937455/40f0536e426907808499',
                'title': 'Студенческий офис',
                'description':
                    """
Через студенческий офис вы можете:
· получить любую справку;
· продлить/заменить студенческий билет;
· заменить паспортные данные;
· продлить сессию по уважительной причине;
· подать заявление на академический отпуск / перевод / восстановление / отчисление;
· временно получить свой документ об образовании (аттестат/диплом).
                """,
            },
            'buttons': [
                {
                    'title': title,
                    'payload': {},
                    'hide': 'true'
                } for title in buttons['suggests']
            ],
            'end': 'false'
        },
        'session': event['session'],
        'session_state': {
            'branch': 'student_office'
        },
        'version': event['version']
    }


def student_office_get_previous_education_document(event, context):
    buttons = {
        'suggests': [
            '<buttons>'
        ]
    }
    return {
        'response': {
            'text':
                """
Вам необходимо перейти на портал ИСУ, а дальше все просто! Подайте заявку через ту форму, которую предлагает система.
                """,
            'tts':
                """
Вам необходимо перейти на портал ИСУ, а дальше все просто! Подайте заявку через ту форму, которую предлагает система.
                """,
            'card': {
                'type': 'BigImage',
                'image_id': '937455/40f0536e426907808499',
                'title': 'Студенческий офис',
                'description':
                    """
Вам необходимо перейти на портал ИСУ, а дальше все просто! Подайте заявку через ту форму, которую предлагает система.
                """,
            },
            'buttons': [
                {
                    'title': title,
                    'payload': {},
                    'hide': 'true'
                } for title in buttons['suggests']
            ],
            'end': 'false'
        },
        'session': event['session'],
        'session_state': {
            'branch': 'student_office'
        },
        'version': event['version']
    }


def student_office_get_consult(event, context):
    buttons = {
        'suggests': [
            '<buttons>'
        ]
    }
    return {
        'response': {
            'text':
                """
Приходите к нам в офис на ул. Ломоносова, д.9. Менеджеры примут вас в порядке живой очереди.
Также вы можете записаться на консультацию через приложение «Электронная очередь» в личном кабинете ИСУ.
                """,
            'tts':
                """
Приходите к нам в офис на ул. Ломоносова, д.9. Менеджеры примут вас в порядке живой очереди.
Также вы можете записаться на консультацию через приложение «Электронная очередь» в личном кабинете ИСУ.
                """,
            'card': {
                'type': 'BigImage',
                'image_id': '937455/40f0536e426907808499',
                'title': 'Студенческий офис',
                'description':
                    """
Приходите к нам в офис на ул. Ломоносова, д.9. Менеджеры примут вас в порядке живой очереди.
Также вы можете записаться на консультацию через приложение «Электронная очередь» в личном кабинете ИСУ.
                """,
            },
            'buttons': [
                {
                    'title': title,
                    'payload': {},
                    'hide': 'true'
                } for title in buttons['suggests']
            ],
            'end': 'false'
        },
        'session': event['session'],
        'session_state': {
            'branch': 'student_office'
        },
        'version': event['version']
    }


def student_office_help_me(event, context):
    buttons = {
        'suggests': [
            '<buttons>'
        ]
    }
    return {
        'response': {
            'text':
                """
Конечно! Помимо перечисленных вопросов, вы можете получить информацию о:
· оплате обучения;
· учебном процессе;
· получении места в общежитии/переселении.
                """,
            'tts':
                """
Конечно! Помимо перечисленных вопросов, вы можете получить информацию о:
· оплате обучения;
· учебном процессе;
· получении места в общежитии/переселении.
                """,
            'card': {
                'type': 'BigImage',
                'image_id': '937455/40f0536e426907808499',
                'title': 'Студенческий офис',
                'description':
                    """
Конечно! Помимо перечисленных вопросов, вы можете получить информацию о:
· оплате обучения;
· учебном процессе;
· получении места в общежитии/переселении.
                """,
            },
            'buttons': [
                {
                    'title': title,
                    'payload': {},
                    'hide': 'true'
                } for title in buttons['suggests']
            ],
            'end': 'false'
        },
        'session': event['session'],
        'session_state': {
            'branch': 'student_office'
        },
        'version': event['version']
    }