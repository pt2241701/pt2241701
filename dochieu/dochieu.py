import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QRadioButton, QPushButton
from PyQt5.uic import loadUi

def format_text(text, max_chars_per_line=200):
    # Cắt đoạn văn thành các phần nhỏ hơn 200 ký tự
    lines = [text[i:i+max_chars_per_line] for i in range(0, len(text), max_chars_per_line)]
    # Thêm ký tự xuống dòng vào giữa các phần
    return '\n'.join(lines)

class QuizApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi(r'C:\project\ui.ui', self)
        self.setWindowTitle('Quiz App')

        # Thiết lập các thuộc tính khác
        self.correct_answer_dochieu = ''
        self.question_number_dochieu = 0
        self.file_number_dochieu = 0
        self.question_history_dochieu = []
        self.load_file()

        # Kết nối các sự kiện với các phương thức
        self.check_button_dochieu.clicked.connect(self.check_answer_dochieu)
        self.next_question_button_dochieu.clicked.connect(self.load_question_dochieu)
        self.next_file_button_dochieu.clicked.connect(self.load_file)
        self.back_question_button_dochieu.clicked.connect(self.back_question_dochieu)
    

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
            
        else:
            selected_button.setStyleSheet("QRadioButton { color: red; }")
            
        self.check_button.setDisabled(True)
        self.next_question_button_dochieu.setDisabled(False)
    
    def clear_selection_dochieu(self):
        # Bỏ chọn tất cả các đáp án
        self.answer1_radio_dochieu.setChecked(False)
        self.answer2_radio_dochieu.setChecked(False)
        self.answer3_radio_dochieu.setChecked(False)
        self.answer4_radio_dochieu.setChecked(False)
        self.check_button_dochieu.setDisabled(False)
        self.next_question_button_dochieu.setDisabled(True)
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

if __name__ == '__main__':
    app = QApplication([])
    quiz_app = QuizApp()
    quiz_app.show()
    app.exec_()