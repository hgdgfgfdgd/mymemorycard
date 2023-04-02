from question import Question

q_list = []

q1= ("Какая функция помогает задать вопрос пользователю?",
    "input",
    "len",
    "print",
    "int")
q_list.append(Question(q1))
q2= ("Какая функция возвращает длину списка?",
    "len",
    "print",
    "input",
    "int")
q_list.append(Question(q2))
q3= ("Какая функция помогает вывести результат в консоль?",
    "print",
    "input",
    "len",
    "int")
q_list.append(Question(q3))
q4= ("Сколько библиотек можно импортировать в один проект?",
    "Неограническое количество",
    "10",
    "5",
    "2")
q_list.append(Question(q4))
q5= ("Какая библиотека отвечает за время?",
    "time",
    "Time",
    "clock",
    "int")
q_list.append(Question(q5))