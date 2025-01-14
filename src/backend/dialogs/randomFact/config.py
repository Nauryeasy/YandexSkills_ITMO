import random

facts = [
    "Опросы показывают, что студенты, которые принимают заметки вручную, имеют более высокие оценки, чем те, кто использует ноутбуки для заметок. Один из возможных объяснений этого явления заключается в том, что ручное письмо способствует более глубокому пониманию материала.",
    "Исследования показывают, что физическая активность, такая как занятия спортом, может помочь студентам улучшить свои результаты в учебе. Это связано с тем, что упражнения способствуют лучшему кровообращению в мозге и улучшению когнитивных функций.",
    "Учёные утверждают, что обучение в группах может способствовать более эффективному усвоению материала. Общение со своими коллегами может помочь студентам более глубоко понять тему и осознать её применение в реальной жизни.",
    "Сон играет важную роль в учебном процессе. Исследования показывают, что студенты, которые получают достаточно сна, имеют лучшие результаты в учебе, чем те, кто страдает от недостатка сна. Для взрослых людей рекомендуется спать от 7 до 9 часов в сутки.",
    "Учёные также говорят, что регулярные перерывы во время учебы могут помочь улучшить ваши результаты. Это связано с тем, что наш мозг может лучше обрабатывать информацию, когда мы регулярно меняем вид деятельности.",
    "Исследования показывают, что использование цвета при заметках и выделении ключевых слов в тексте может помочь улучшить запоминание информации. Это может быть особенно полезно при подготовке к экзаменам.",
    "Студенты, которые занимаются спортом, обычно имеют лучшие результаты в учёбе, чем те, кто не занимается спортом.",
    "Некоторые исследования показывают, что люди лучше запоминают информацию, когда они её записывают вручную, а не печатают на компьютере.",
    "Чтение вслух может помочь студентам запомнить информацию лучше, чем просто чтение в уме.",
    "Студенты, которые спят достаточно, часто имеют лучшие результаты в учёбе, чем те, кто не высыпается.",
    "Исследования показывают, что студенты, которые занимаются в комнате с ярким освещением, имеют лучшие результаты в учёбе, чем те, кто занимается в темном помещении.",
    "Некоторые эксперты советуют заниматься физическими упражнениями перед началом учёбы, чтобы улучшить кровообращение в мозге и улучшить способность к концентрации.",
    "Студенты, которые пользуются цветными ручками при записи лекций и заметок, лучше запоминают информацию, чем те, кто использует только один цвет.",
    "Регулярное повторение и закрепление материала, которое происходит в течение длительного периода времени, помогает улучшить запоминание и уменьшить забывание.",
    "Использование мнемоников, таких как акронимы, помогает запоминать и организовывать информацию.",
    "Изучение предмета на практике может помочь лучше понять теоретический материал. Например, при изучении языка, можно попрактиковаться в общении на этом языке с носителями.",
    "Некоторые исследования показывают, что небольшие паузы во время учёбы, когда вы занимаетесь чем-то другим, могут помочь улучшить запоминание информации.",
    "Постоянное участие в академических мероприятиях, таких как лекции, семинары и конференции, может помочь улучшить понимание и знания в вашей области.",
    "Чтение и написание своих собственных заметок может помочь вам улучшить понимание материала и организовать свои мысли.",
    "Сон играет важную роль в процессе запоминания и консолидации информации. Старайтесь спать достаточное количество часов, чтобы ваш мозг мог обработать и закрепить информацию, полученную в течение дня."]

message = 'Случайный факт: \n'

buttons = [
    "Повторить ещё раз",
    "Помощь"
    "Назад",
    "Выйти"
]

session_state = {
    "branch": "randomFact"
}


def getConfig():
    return {
        'message': message + facts[random.randint(0, len(facts))],
        'tts': message,
        'buttons': buttons,
        'session_state': session_state
    }
