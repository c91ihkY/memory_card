from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import * 
from random import shuffle

app = QApplication([])

button_ok = QPushButton('Ответить')
lb_question = QLabel('Очень сложный вопрос!!!!')

RadioGroupBox = QGroupBox('Варианты ответа')

rbutton_1 = QRadioButton('1')
rbutton_2 = QRadioButton('2')
rbutton_3 = QRadioButton('3')
rbutton_4 = QRadioButton('4')
#что-то такое#


RadioGroup = QButtonGroup()
RadioGroup.addButton(rbutton_1)
RadioGroup.addButton(rbutton_2)
RadioGroup.addButton(rbutton_3)
RadioGroup.addButton(rbutton_4)


layout_answer1 = QHBoxLayout()
layout_answer2 = QVBoxLayout()
layout_answer3 = QVBoxLayout()

layout_answer2.addWidget(rbutton_1)
layout_answer2.addWidget(rbutton_2)
layout_answer3.addWidget(rbutton_3)
layout_answer3.addWidget(rbutton_4)

layout_answer1.addLayout(layout_answer2)
layout_answer1.addLayout(layout_answer3)

RadioGroupBox.setLayout(layout_answer1)

AnsGroupBox = QGroupBox('')
lb_result = QLabel('ты крутой?')
lb_answer = QLabel('ответ тута.')

layout_ans = QVBoxLayout()
layout_ans.addWidget(lb_result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_ans.addWidget(lb_answer,alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_ans)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(button_ok , stretch=4)
layout_line3.addStretch(1)

layout_main = QVBoxLayout()

layout_main.addLayout(layout_line1, stretch=2)
layout_main.addLayout(layout_line2, stretch=7)
layout_main.addStretch(1)
layout_main.addLayout(layout_line3, stretch=1)
layout_main.addStretch(1)
layout_main.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button_ok.setText('Следующий вопрос')

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    button_ok.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbutton_1.setChecked(False)
    rbutton_2.setChecked(False)
    rbutton_3.setChecked(False)
    rbutton_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbutton_1, rbutton_2, rbutton_3, rbutton_4]

class Question:
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def ask(q : Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_question.setText(q.question)
    lb_answer.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Верно! ')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно! , ты нуб')

def next_question():
    window.cur_question = window.cur_question + 1
    if window.cur_question >= len(questions_list):
        window.cur_question = 0
    q = questions_list[window.cur_question]
    ask(q)

def click_OK():
    if button_ok.text() == 'Ответить':
        check_answer()
    else:
        next_question()


window = QWidget()
window.setLayout(layout_main)
window.setWindowTitle('Тест')

window.cur_question = -1

questions_list = []
questions_list.append(Question('Государственный язык Бельгии ', 'Нидерландский', 'Немецкий', 'Французский', 'Английский'))
questions_list.append(Question('Какого цвета нет на флаге Италии?', 'Жёлтый' , 'Зеленый' , 'Белый', 'Красный'))
questions_list.append(Question('Как меня зовут ?' , 'Арсен', 'Александр' , 'Иван' , 'меня не зовут , я сам прихожу'))
questions_list.append(Question('Кто убил Пушкина?' , 'Дантес' , 'Есенин' , 'Лермонтов ' , 'Дуэйн Скала Джонсон'))
questions_list.append(Question('Моя руссичка крутая?', 'Да ' , 'Нет ', 'Нет ' , 'Кристина Валерьевна не убивайте меня пожалуйста((('))
questions_list.append(Question('Моя мама крутая ? ', 'Конечно да!!!!' , 'Нет' , 'Ну хз' , 'Нет , вообще ботиха '))
questions_list.append(Question('Кто написал песню : The Real Slim Shady?' , 'Eminem' , 'Morgenshtern' , ' Егор Крид' , 'Snopp Dogg'))



button_ok.clicked.connect(click_OK)
next_question()

window.show()
app.exec()
