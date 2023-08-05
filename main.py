import subprocess
import pygame
import os
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtChart import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import icons
import sqlite3


QApplication(sys.argv)
####################################loginregister#########################################
class RegisterDialog(QDialog):
    def __init__(self, connection):
        super(RegisterDialog, self).__init__()
        loadUi('register.ui', self)
        self.signup.clicked.connect(lambda: self.register(connection))

    def register(self, connection):
        usernamesign = self.user2.text()
        emailsign = self.email.text()
        passsign = self.pass2.text()
        cursor = connection.cursor()
        # Kiểm tra xem tên người dùng đã tồn tại hay chưa
        result = cursor.execute("SELECT * FROM USERS WHERE user = ?", (usernamesign,))
        if len(result.fetchall()) > 0:
            self.noti2.setText("Tên người dùng đã tồn tại!")
        else:
            # Ghi dữ liệu vào tệp tin SQL
            with open('data.sql', 'a') as sql_file:
                sql_file.write(f"INSERT INTO USERS VALUES('{usernamesign}', '{emailsign}', '{passsign}');\n")
                self.noti2.setText("ĐĂNG KÝ THÀNH CÔNG!!!")
        sys.exit()

class LoginDialog(QDialog):
    def __init__(self):
        super(LoginDialog, self).__init__()
        loadUi('login.ui', self)
        self.login.clicked.connect(self.loginn)
        self.register.clicked.connect(self.registere)
        self.successful = False

        # Kết nối đến cơ sở dữ liệu
        self.connection = sqlite3.connect(":memory:")  # Tạo cơ sở dữ liệu trong bộ nhớ
        cursor = self.connection.cursor()

        # Đọc tệp tin SQL và thực thi các câu lệnh
        with open('data.sql', 'r') as sql_file:
            sql_script = sql_file.read()
            cursor.executescript(sql_script)

    def loginn(self):
        username = self.user1.text()
        password = self.pass1.text()
        cursor = self.connection.cursor()
        result = cursor.execute("SELECT * FROM USERS WHERE user = ? AND pass = ?", (username, password))
        if len(result.fetchall()) > 0:
            print("User Found!")
            self.noti.setText("ĐĂNG NHẬP THÀNH CÔNG!!!")
            self.successful = True
            self.close()
        else:
            print("User Not Found!")
            self.noti.setText("ĐĂNG NHẬP KHÔNG THÀNH CÔNG!!!")

    def registere(self):
        register_dialog = RegisterDialog(self.connection)
        register_dialog.exec_()
####################################loginregister#########################################      


####################################hàm phụ###############################################
def out():
        sys.exit()
def format_text(text, max_chars_per_line=200):
    # Cắt đoạn văn thành các phần nhỏ hơn 200 ký tự
    lines = [text[i:i+max_chars_per_line] for i in range(0, len(text), max_chars_per_line)]
    # Thêm ký tự xuống dòng vào giữa các phần
    return '\n'.join(lines)
####################################hàm phụ###############################################

####################################Class chính###########################################
class Question:
    def __init__(self, question, choiceA, choiceB, choiceC, choiceD, correctChoice):
        self.question = question
        self.choiceA = choiceA
        self.choiceB = choiceB
        self.choiceC = choiceC
        self.choiceD = choiceD
        self.correctChoice = correctChoice
class MainWindow(QMainWindow):
    def __init__(self, file_path_nghe, username):
        super(MainWindow, self).__init__()
        loadUi(r'C:\project\ui.ui', self)
        self.audio_files = []
        self.label_ten.setText(username)
        for filename in os.listdir('C:/project/nghe'):
            if filename.endswith('.mp3'):
                self.audio_files.append(os.path.join('C:/project/nghe', filename))

        self.nghe.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_nghe))
        self.dochieu.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_dochieu))
        self.vanpham.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_vanpham))
        self.trangchu.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_trangchu))
        self.menuBtn.clicked.connect(self.slideLeftMenu)
        self.skipButton.clicked.connect(self.skipQuestion)
        self.backButton.clicked.connect(self.backQuestion)


        self.questions = []
        self.score = 0
        self.currentQuestionIndex = 0
        with open('C:/project/file.txt', 'r', encoding='utf-8') as f:
            for line in f:
                question, choiceA, choiceB, choiceC, choiceD, correctChoice = line.strip().split('|')
                self.questions.append(Question(question, choiceA, choiceB, choiceC, choiceD, correctChoice))
        
        
        # Gom các phương án trả lời vào một nhóm
        self.choiceButtonGroup = QButtonGroup(self)
        self.choiceButtonGroup.addButton(self.choiceARadioButton)
        self.choiceButtonGroup.addButton(self.choiceBRadioButton)
        self.choiceButtonGroup.addButton(self.choiceCRadioButton)
        self.choiceButtonGroup.addButton(self.choiceDRadioButton)
        self.exit_button.clicked.connect(out)
        self.answerButton.clicked.connect(self.checkAnswer)
        self.nextButton.clicked.connect(self.nextQuestion)
        self.showQuestion(self.currentQuestionIndex)
        # Hiển thị câu hỏi đầu tiên

        #########nghe#############################################
        self.file_path_nghe = file_path_nghe
        self.questions_nghe = []
        self.answers_nghe = []
        self.correct_answers_nghe = []
        self.current_question_nghe = 0
        self.score_nghe = 0
        self.load_questions_nghe()
        self.radio_buttons_nghe = []
        self.radio_buttons_nghe.append(self.radio_button_1)
        self.radio_buttons_nghe.append(self.radio_button_2)
        self.radio_buttons_nghe.append(self.radio_button_3)
        self.radio_buttons_nghe.append(self.radio_button_4)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.question_label_nghe)
        vbox.addWidget(self.radio_button_1)
        vbox.addWidget(self.radio_button_2)
        vbox.addWidget(self.radio_button_3)
        vbox.addWidget(self.radio_button_4)
        vbox.addWidget(self.play_button)
        vbox.addWidget(self.check_button)
        vbox.addWidget(self.next_button)
        vbox.addWidget(self.scorelabelnghe)
        vbox.addWidget(self.prev_button)
        self.setLayout(vbox)
        self.question_label_nghe.setText(self.questions_nghe[self.current_question_nghe])
        self.radio_button_1.toggled.connect(lambda:(self.radio_button_1))
        self.radio_button_2.toggled.connect(lambda:(self.radio_button_2))
        self.radio_button_3.toggled.connect(lambda:(self.radio_button_3))
        self.radio_button_4.toggled.connect(lambda:(self.radio_button_4))

        self.prev_button.clicked.connect(self.prev_questions_nghe)
        self.play_button.clicked.connect(self.play_music_nghe)
        self.check_button.clicked.connect(self.check_answer_nghe)
        self.next_button.clicked.connect(self.next_question_nghe)
        self.switch_file_button.clicked.connect(self.switch_file_nghe)
        ######nghe####################################################

        ######đọc hiểu################################################
        # Thiết lập các thuộc tính khác
        self.correct_answer_dochieu = ''
        self.question_number_dochieu = 0
        self.file_number_dochieu = 0
        self.question_history_dochieu = []
        self.score_dochieu = 0
        self.load_file()

        # Kết nối các sự kiện với các phương thức
        self.check_button_dochieu.clicked.connect(self.check_answer_dochieu)
        self.next_question_button_dochieu.clicked.connect(self.load_question_dochieu)
        self.next_file_button_dochieu.clicked.connect(self.load_file)
        self.back_question_button_dochieu.clicked.connect(self.back_question_dochieu)
        ######đọc hiểu################################################
    
    def slideLeftMenu(self):
        width = self.left_side_menu.width()
        if width == 50:
            newWidth = 150
        else :
            newWidth = 50
        self.animation = QPropertyAnimation(self.left_side_menu, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.start()
####################################backend văn phạm######################################
    def showQuestion(self, index):
        question = self.questions[index]
        self.questionLabel.setText(question.question)
        self.choiceARadioButton.setText(question.choiceA)
        self.choiceBRadioButton.setText(question.choiceB)
        self.choiceCRadioButton.setText(question.choiceC)
        self.choiceDRadioButton.setText(question.choiceD)
        
    def checkAnswer(self):
        question = self.questions[self.currentQuestionIndex]
        selectedChoice = self.choiceButtonGroup.checkedButton()
        if selectedChoice is not None and selectedChoice.text() == question.correctChoice:
            # Điều kiện đúng
            self.score += 1
            self.scoreLabel.setText(f"Điểm số: {self.score}")
            self.diemvanpham.setText(f"{self.score}")
            selectedChoice.setStyleSheet("QRadioButton {color: green}")
        else:
            # Điều kiện sai, thay đổi màu sắc của phần tử được chọn
            if selectedChoice is not None:
                selectedChoice.setStyleSheet("QRadioButton {color: red}")
            # Đặt lại màu sắc mặc định cho các phần tử khác
            for choice in self.choiceButtonGroup.buttons():
                if choice != selectedChoice:
                    choice.setStyleSheet("QRadioButton {color: black}")
    def nextQuestion(self):
        self.currentQuestionIndex += 1
        if self.currentQuestionIndex < len(self.questions):
            self.showQuestion(self.currentQuestionIndex)
            self.choiceButtonGroup.setExclusive(False)
            checkedButton = self.choiceButtonGroup.checkedButton()
            if checkedButton is not None:
                checkedButton.setChecked(False)
            self.choiceButtonGroup.setExclusive(True)
        else:
            self.questionLabel.setText("Bạn đã hoàn thành bài kiểm tra!")
            self.choiceARadioButton.hide()
            self.choiceBRadioButton.hide()
            self.choiceCRadioButton.hide()
            self.choiceDRadioButton.hide()
            self.answerButton.hide()
            self.skipButton.hide()
            self.backButton.hide()
        self.scoreLabel.setText("Điểm số: " + str(self.score))
    def skipQuestion(self):
        self.currentQuestionIndex += 1
        if self.currentQuestionIndex < len(self.questions):
            self.showQuestion(self.currentQuestionIndex)
            self.choiceButtonGroup.setExclusive(False)
            checkedButton = self.choiceButtonGroup.checkedButton()
            if checkedButton is not None:
                checkedButton.setChecked(False)
            self.choiceButtonGroup.setExclusive(True)
        else:
            self.questionLabel.setText("Bạn đã hoàn thành bài kiểm tra!")
            self.choiceARadioButton.hide()
            self.choiceBRadioButton.hide()
            self.choiceCRadioButton.hide()
            self.choiceDRadioButton.hide()
            self.answerButton.hide()
            self.skipButton.hide()
            self.backButton.hide()
        self.scoreLabel.setText("Điểm số: " + str(self.score))
    def backQuestion(self):
        self.currentQuestionIndex -= 1
        if self.currentQuestionIndex >= 0:
            self.showQuestion(self.currentQuestionIndex)
            self.choiceButtonGroup.setExclusive(False)
            checkedButton = self.choiceButtonGroup.checkedButton()
            if checkedButton is not None:
                checkedButton.setChecked(False)
            self.choiceButtonGroup.setExclusive(True)
        else:
            self.currentQuestionIndex = 0
        self.scoreLabel.setText("Điểm số: " + str(self.score))
####################################backend văn phạm######################################


####################################backend nghe##########################################
    def set_answer(self, radio_button):
        if radio_button.isChecked():
            self.user_answer = radio_button.text()
    def play_music_nghe(self):
        file_index = int(self.file_path_nghe.split('.')[0][-1])
        audio_file_path = f"C:/project/nghe/{file_index}.mp3"
        self.clear_selection_dochieu()
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(audio_file_path)
            pygame.mixer.music.set_volume(8)
            pygame.mixer.music.play(-1)
        except Exception as e:
            print("Lỗi khi phát file âm thanh: ", str(e))
    def check_answer_nghe(self):
        selected_button = None
        for radio_button in self.radio_buttons_nghe:
            if radio_button.isChecked():
                selected_button = radio_button
                break
        if selected_button is None:
            return
        selected_answer = selected_button.text()
        correct_answer = self.correct_answers_nghe[self.current_question_nghe]
        if selected_answer == correct_answer:
            self.score_nghe += 1
            self.scorelabelnghe.setText(f"Điểm số: {self.score_nghe}")
            self.diemnghe.setText(f"{self.score_nghe}")
        else:
            selected_button.setStyleSheet("QRadioButton{color:red}")
        for radio_button in self.radio_buttons_nghe:
            radio_button.setEnabled(False)
            if radio_button.text() == correct_answer:
                radio_button.setStyleSheet("QRadioButton{color:green}")
    def switch_file_nghe(self):
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0)
        file_index = int(self.file_path_nghe.split('.')[0][-1])
        next_file_path_nghe = f"C:/project/nghe/{file_index + 1}.txt"
        self.clear_selection_dochieu()
        try:
            with open(next_file_path_nghe, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                self.questions_nghe = []
                self.answers = []
                self.correct_answers_nghe = []
                for line in lines:
                    parts = line.strip().split('|')
                    self.questions_nghe.append(parts[0])
                    self.answers.append(parts[1:5])
                    self.correct_answers_nghe.append(parts[5])
                self.file_path_nghe = next_file_path_nghe
                self.current_question_nghe = 0
                
                self.question_label_nghe.setText(self.questions_nghe[self.current_question_nghe])
                for i in range(4):
                    radio_button = self.radio_buttons_nghe[i]
                    radio_button.setText(self.answers[self.current_question_nghe][i])
                    radio_button.setChecked(False)
                    radio_button.setStyleSheet("QRadioButton{color:black}")
                    radio_button.setEnabled(True)
        except FileNotFoundError:
            print("Không tìm thấy file trắc nghiệm tiếp theo!")
    def load_next_file(self):
        file_index = int(self.file_path.split('.')[0][-1])
        next_file_path = f"C:/project/nghe/{file_index + 1}.txt"
        self.clear_selection_dochieu()
        try:
            with open(next_file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                self.questions_nghe = []
                self.answers_nghe = []
                self.correct_answers_nghe = []
                for line in lines:
                    parts = line.strip().split('|')
                    self.questions_nghe.append(parts[0])
                    self.answers_nghe.append(parts[1:5])
                    self.correct_answers_nghe.append(parts[5])
                self.file_path = next_file_path
                return True
        except FileNotFoundError:
            return False
        
    def next_question_nghe(self):
        if self.current_question_nghe == len(self.questions_nghe) - 1:
            if self.load_next_file():
                self.current_question_nghe = 0
            else:
                return
        else:
            self.current_question_nghe += 1
        
        self.question_label_nghe.setText(self.questions_nghe[self.current_question_nghe])
        for i in range(4):
            radio_button = self.radio_buttons_nghe[i]
            radio_button.setText(self.answers_nghe[self.current_question_nghe][i])
            radio_button.setChecked(False)
            radio_button.setStyleSheet("QRadioButton{color:black}")
            radio_button.setEnabled(True)
        self.clear_selection_dochieu()
    def prev_questions_nghe(self):
        if self.current_question_nghe == 0:
            return
        self.current_question_nghe -= 1
        
        self.question_label_nghe.setText(self.questions_nghe[self.current_question_nghe])
        for i in range(4):
            radio_button = self.radio_buttons_nghe[i]
            radio_button.setText(self.answers_nghe[self.current_question_nghe][i])
            radio_button.setChecked(False)
            radio_button.setStyleSheet("QRadioButton{color:black}")
            radio_button.setEnabled(True)
        self.clear_selection_dochieu()

    def load_questions_nghe(self):
        with open(self.file_path_nghe, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                parts = line.strip().split('|')
                self.questions_nghe.append(parts[0])
                self.answers_nghe.append(parts[1:5])
                self.correct_answers_nghe.append(parts[5])
                self.clear_selection_dochieu()
    def clear_selection_nghe(self):
        # Bỏ chọn tất cả các đáp án
        self.radio_buttons_1.setChecked(False)
        self.radio_buttons_2.setChecked(False)
        self.radio_buttons_3.setChecked(False)
        self.radio_buttons_4.setChecked(False)
####################################backend nghe##########################################



####################################backend đọc hiểu######################################
    def load_file(self):
        # Load file txt tiếp theo
        file_path = f'C:/project/dochieu/{self.file_number_dochieu}.txt'
        if os.path.exists(file_path):
            self.questions_dochieu = []
            with open(file_path, 'r', encoding='utf-8') as file:
                dochieu = file.readline().strip()
                formatted_dochieu = format_text(dochieu)
                self.dochieu_label.setText(formatted_dochieu)
                for line in file:
                    question, answer1, answer2, answer3, answer4, correct_answer_dochieu = line.strip().split('|')
                    self.questions_dochieu.append({
                        'question': question,
                        'answer1': answer1,
                        'answer2': answer2,
                        'answer3': answer3,
                        'answer4': answer4,
                        'correct_answer_dochieu': correct_answer_dochieu
                    })
            self.answer1_radio_dochieu.setStyleSheet("QRadioButton { color: black; }")
            self.answer2_radio_dochieu.setStyleSheet("QRadioButton { color: black; }")
            self.answer3_radio_dochieu.setStyleSheet("QRadioButton { color: black; }")
            self.answer4_radio_dochieu.setStyleSheet("QRadioButton { color: black; }")
            self.question_number_dochieu = 0
            self.file_number_dochieu += 1
            self.load_question_dochieu()
            self.clear_selection_dochieu()
    
    def load_question_dochieu(self):
        # Load câu hỏi tiếp theo
        if self.question_number_dochieu < len(self.questions_dochieu):
            question = self.questions_dochieu[self.question_number_dochieu]
            self.question_label_dochieu.setText(question['question'])
            self.answer1_radio_dochieu.setText(question['answer1'])
            self.answer2_radio_dochieu.setText(question['answer2'])
            self.answer3_radio_dochieu.setText(question['answer3'])
            self.answer4_radio_dochieu.setText(question['answer4'])
            self.correct_answer_dochieu = question['correct_answer_dochieu']
            self.question_number_dochieu += 1
            self.clear_selection_dochieu()
            self.question_history_dochieu.append(question)
            self.answer1_radio_dochieu.setStyleSheet("QRadioButton { color: black; }")
            self.answer2_radio_dochieu.setStyleSheet("QRadioButton { color: black; }")
            self.answer3_radio_dochieu.setStyleSheet("QRadioButton { color: black; }")
            self.answer4_radio_dochieu.setStyleSheet("QRadioButton { color: black; }")


    def check_answer_dochieu(self):
        # Kiểm tra đáp án
        selected_button = None
        self.selected_answer = ''
        if self.answer1_radio_dochieu.isChecked():
            selected_button = self.answer1_radio_dochieu
            self.selected_answer = self.answer1_radio_dochieu.text()
        elif self.answer2_radio_dochieu.isChecked():
            selected_button = self.answer2_radio_dochieu
            self.selected_answer = self.answer2_radio_dochieu.text()
        elif self.answer3_radio_dochieu.isChecked():
            selected_button = self.answer3_radio_dochieu
            self.selected_answer = self.answer3_radio_dochieu.text()
        elif self.answer4_radio_dochieu.isChecked():
            selected_button = self.answer4_radio_dochieu
            self.selected_answer = self.answer4_radio_dochieu.text()
        if selected_button is None:
            return
        if self.selected_answer == self.correct_answer_dochieu:
            selected_button.setStyleSheet("QRadioButton { color: green; }")
            self.score_dochieu +=1
            
        else:
            selected_button.setStyleSheet("QRadioButton { color: red; }")
            self.score_dochieu +=0

        self.check_button.setDisabled(True)
        self.next_question_button_dochieu.setDisabled(False)
        self.scorelabeldochieu.setText(f"Điểm số:\n {self.score_dochieu}")
        self.diemdochieu.setText(f"{self.score_dochieu}")
    
    def clear_selection_dochieu(self):
        # Bỏ chọn tất cả các đáp án
        self.answer1_radio_dochieu.setChecked(False)
        self.answer2_radio_dochieu.setChecked(False)
        self.answer3_radio_dochieu.setChecked(False)
        self.answer4_radio_dochieu.setChecked(False)
    def back_question_dochieu(self):
        # Quay lại câu hỏi trước đó trong lịch sử
        if len(self.question_history_dochieu) > 1:
            self.question_history_dochieu.pop() # Xóa câu hỏi hiện tại khỏi lịch sử
            question = self.question_history_dochieu[-1] # Lấy câu hỏi trước đó trong lịchTiếp tục phần mã nguồn QuizApp:
            self.question_label_dochieu.setText(question['question'])
            self.answer1_radio_dochieu.setText(question['answer1'])
            self.answer2_radio_dochieu.setText(question['answer2'])
            self.answer3_radio_dochieu.setText(question['answer3'])
            self.answer4_radio_dochieu.setText(question['answer4'])
            self.correct_answer_dochieu = question['correct_answer_dochieu']
            self.question_number_dochieu -= 1 # Giảm số thứ tự câu hỏi
            self.clear_selection_dochieu()
            self.answer1_radio_dochieu.setStyleSheet("QRadioButton { color: black; }")
            self.answer2_radio_dochieu.setStyleSheet("QRadioButton { color: black; }")
            self.answer3_radio_dochieu.setStyleSheet("QRadioButton { color: black; }")
            self.answer4_radio_dochieu.setStyleSheet("QRadioButton { color: black; }")
####################################backend đọc hiểu######################################


####################################Class chính###########################################


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = LoginDialog()
    login.exec_()
    if login.successful:
        window = MainWindow(r'C:\project\nghe\1.txt', login.user1.text())
        window.show()
    sys.exit(app.exec_())