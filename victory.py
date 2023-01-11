class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "В каком году родился М.Ю. Лермнотов? ", #1814
    "В каком году родился М.В. Ломоносов? ", #1711
    "В каком году родился Н.В. Гоголь? ", #1809
    "В каком году родился Ф.М. Достоевский? ", #1821
    "В каком году родился А.П. Чехов? " #1860
]

questions = [
    Question(question_prompts[0], 1814),
    Question(question_prompts[1], 1711),
    Question(question_prompts[2], 1809),
    Question(question_prompts[3], 1821),
    Question(question_prompts[4], 1860)
]

def run_test(questions):
    while True:
        score = 0
        wrong_answers = 0
        for i in questions:
            answer = input(i.prompt)
            if answer == i.answer:
                score += 1
            else:
                wrong_answers += 1

        print('Вы ответили неправильно на ' + str(wrong_answers) + ' вопросов из ' + str(len(questions)))
        print('Вы ответили правильно на ' + str(score) + ' вопросов из ' + str(len(questions)))
        print('Процент правильных ответов: ' + str((score * 100) / len(questions)) + '%')
        print('Процент неправильных ответов: ' + str(100 - ((score * 100) / len(questions))) + '%')

        one_more_time = input('Хотите сыграть ещё? ')

        if one_more_time == "да":
            print("Сыграем ещё раз")
        else:
            break

run_test(questions)