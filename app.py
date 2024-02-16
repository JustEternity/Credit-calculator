import sys

from Credit_calculator import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow, QButtonGroup


class Calculator_app(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.sum = self.enter_sum.text()
        self.rate = self.rate_enter.text()
        self.term = self.enter_term.text()
        self.date = self.dateEdit.date()

        self.enter_sum.textChanged.connect(self.change_sum)
        self.rate_enter.textChanged.connect(self.change_rate)
        self.enter_term.textChanged.connect(self.change_term)
        self.dateEdit.dateChanged.connect(self.change_date)

        self.radioButton_group = QButtonGroup()
        self.radioButton_group.addButton(self.radioButton_1, id=1)
        self.radioButton_group.addButton(self.radioButton_2, id=2)

        self.calculation_button.clicked.connect(self.calc_button_click)
        self.info_button.clicked.connect(self.show_info)
        self.paygraph_button.clicked.connect(self.calculate_paygraph)


    def calc_button_click(self):
        if self.radioButton_group.checkedId() == 1:
            print('an')
            self.calculate_annuty()
        if self.radioButton_group.checkedId() == 2:
            print('dif')
            self.calculate_diff()


    def change_sum(self, text):
        try:
            self.sum = int(text)
        except ValueError:
            print("Это не число!")

    def change_rate(self, text):
        try:
            self.rate = float(text)
        except ValueError:
            print("Это не число!")

    def change_term(self, text):
        try:
            self.term = int(text)
        except ValueError:
            print("Это не число!")

    def change_date(self, text):
        self.date = text



    def calculate_annuty(self):
        ''' Функция, рассчитывающая ежемесячный платеж, общую сумму кредита и сумму процентов для аннуитентного кредита
        '''
        self.month_rate = self.rate / 1200
        self.month_payment_annuty = self.sum*((self.month_rate * (1 + self.month_rate)**(self.term*12)) / ((1 + self.month_rate)**(self.term*12)  - 1))
        self.all_payments_annuty = self.month_payment_annuty * 12 * self.term
        self.annuty_overpayment = self.all_payments_annuty - self.sum

        self.amount_payments.setText(f'Сумма выплат: {self.all_payments_annuty:.2f} руб.')
        self.month_payment.setText(f"Ежемесячный платеж: {self.month_payment_annuty:.2f} руб.")
        self.overpayment.setText(f"Сумма переплаты: {self.annuty_overpayment:.2f} руб.")



    def calculate_diff(self):
        ''' Функция для расчета общей суммы кредита и суммы процентов, ежемесячный платеж уменьшается со временем,
        поэтому он показывается только в разделе "График платежей"
        '''
        # Сумма процентов по дифференцированному платежу
        self.percents_diff = (self.term * (self.term + 1) * (self.rate/100))/2 *self.sum
        # Сумма общего долга
        self.all_payments_diff = self.sum + self.percents_diff



    def calculate_paygraph(self):
        ''' Функция для расчета и вывода графика платежей по кредиту
        '''
        pass

    def show_info(self):
        ''' Функция для вывода справочной информации по кредитованию
        '''
        pass






def main():
    app = QApplication(sys.argv)
    window = Calculator_app()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()