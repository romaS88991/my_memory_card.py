from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QGroupBox, QRadioButton
from random import randint
from random import shuffle

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory card')
text = QLabel('Какой национальности не существует?')
button = QPushButton('Сгенерировать?')
RadioGroupBox = QGroupBox('Варианты ответов:')
rbtn_1 = QRadioButton('Эйцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чульмцы')
rbtn_4 = QRadioButton('Алеуты')
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('Правильно/Неправильно')
lb_Correct = QLabel('Правильный ответ')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result)
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
main_win.setLayout(layout_card)

def show_result():
    AnsGroupBox.hide()
    AnsGroupBox.show()
    AnsGroupBox.setText()
btn_Ok.clicked.connect(show_result)

def show_questions():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_Ok.setText('Ответить')
    RadioGroupBox.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_aswer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Question.setText(q.right_aswer)
    show_questions()

def show_correct(res):
    Ib_Result.setText(res)
    show_result()

def test():
    if 'Ответь' == btn_OK.test():
        show_result()
    else: 
        show_questions()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
    else:
        if answers[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            swow_correct('Неверно!')

class Question():
    def __init__ (self, question, right_aswer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_aswer = right_aswer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Государственный язык Португалии', 'Португальский', 'Английский', 'Испанский', 'Французкий'))
question_list.append(Question('Государственный язык России', 'Русский', 'Украинский', 'Казахский', 'Немецкий'))

main_win.cur_question = -1

def next_question():
    main_win.cur_question += 1
    if main_win.cur_question >= len(question_list):
        main_win.cur_question = 0
    q = question_list[window.cur_question]
    ask(q)

def click_ok():
    if btn_OK.text() == 'Ответить':
        check_answer() # проверка ответа
    else:
        next_question() # следующий вопрос    

main_win.show()
app.exec_()