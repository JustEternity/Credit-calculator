import datetime
import sys

from Credit_calculator import Ui_MainWindow
from info_window import Ui_Form
from datetime import datetime
from dateutil.relativedelta import relativedelta
from PyQt6.QtWidgets import QApplication, QMainWindow, QButtonGroup, QMessageBox
from PyQt6.QtCore import QDate




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
        match self.radioButton_group.checkedId():
            case 1:
                self.calculate_annuty()
            case 2:
                self.calculate_diff()
            case -1:
                QMessageBox.warning(self.layoutWidget, "Предупреждение", "Выберите тип кредита")



    def change_sum(self, text):
        try:
            self.sum = int(text)
        except ValueError:
            QMessageBox.warning(self.layoutWidget, "Предупреждение", "Здесь должно быть число")

    def change_rate(self, text):
        try:
            self.rate = float(text)
        except ValueError:
            QMessageBox.warning(self.layoutWidget, "Предупреждение", "Здесь должно быть число")

    def change_term(self, text):
        try:
            self.term = int(text)
        except ValueError:
            QMessageBox.warning(self.layoutWidget, "Предупреждение", "Здесь должно быть число")

    def change_date(self, text):
        self.date = text



    def calculate_annuty(self):
        ''' Функция, рассчитывающая ежемесячный платеж, общую сумму кредита и сумму процентов для аннуитентного кредита
        '''
        self.type_term = 1 if self.choice_term.currentText() == 'мес.' else 12
        self.month_rate = self.rate / 1200
        self.month_payment_annuty = self.sum*((self.month_rate * (1 + self.month_rate)**(self.term*self.type_term)) /
                                              ((1 + self.month_rate)**(self.term*self.type_term)  - 1))
        self.all_payments_annuty = self.month_payment_annuty * self.type_term * self.term
        self.annuty_overpayment = self.all_payments_annuty - self.sum

        self.amount_payments.setText(f'Сумма выплат: {self.all_payments_annuty:.2f} руб.')
        self.month_payment.setText(f"Ежемесячный платеж: {self.month_payment_annuty:.2f} руб.")
        self.overpayment.setText(f"Сумма переплаты: {self.annuty_overpayment:.2f} руб.")
        print(self.calculate_annuity_payments(self.sum, self.month_payment_annuty, self.rate/100, self.term*self.type_term, self.date.toString('yyyy-MM-dd')))





    def calculate_annuity_payments(self, loan_amount, monthly_payment, interest_rate, loan_term, issue_date):
        payment_schedule = {}
        remaining_loan = loan_amount
        issue_date = datetime.strptime(issue_date, "%Y-%m-%d")

        for month in range(1, loan_term + 1):
            payment_date = issue_date + relativedelta(months=+month)
            if payment_date.day < issue_date.day:
                payment_date = payment_date + relativedelta(day=31)
            interest_payment = remaining_loan * (interest_rate / 12)
            principal_payment = monthly_payment - interest_payment
            remaining_loan -= principal_payment
            payment_schedule[payment_date.strftime("%Y-%m-%d")] = [monthly_payment, interest_payment, remaining_loan]

        return payment_schedule




    def calculate_diff(self):
        ''' Функция для расчета суммы основного долга для каждого платежа, ежемесячный платеж уменьшается со временем,
        поэтому он показывается только в разделе "График платежей"
        '''
        self.type_term = 1 if self.choice_term.currentText() == 'мес.' else 12
        self.start_date = datetime(self.date.year(), self.date.month(), self.date.day())
        if self.type_term == 12:
            self.end_date = self.start_date + relativedelta(years=self.term)
        else:
            self.end_date = self.start_date + relativedelta(months=self.term)

        self.count_days = (self.end_date - self.start_date).days

        # Часть основного долга, одинаковая для каждого месяца (платежа)
        self.part_of_debt = self.sum / (self.term*self.type_term)
        # Сумма процентов по дифференцированному платежу
        self.percents_diff = ((self.sum*(self.rate/100)*self.count_days)/365)*365
        # Сумма общего долга
        self.all_payments_diff = self.sum + self.percents_diff

        self.amount_payments.setText(f"Платеж без учета процентов: {self.part_of_debt:.2f} руб.")
        self.month_payment.setText(f"Сумма переплаты: {self.percents_diff}")
        self.overpayment.setText(f"")

        print(self.schedule_diff(self.sum, self.rate, self.term*self.type_term, self.date))


    def schedule_diff(self, loan_amount, interest_rate, term, issue_date):
        payments = {}
        monthly_interest_rate = interest_rate / 12 / 100
        monthly_payment = loan_amount / term
        remaining_balance = loan_amount

        # Преобразование QDate в datetime
        issue_date = datetime(issue_date.year(), issue_date.month(), issue_date.day())

        for month in range(1, term + 1):
            interest_payment = remaining_balance * monthly_interest_rate
            principal_payment = monthly_payment - interest_payment
            remaining_balance -= principal_payment

            # Adjust the payment date if necessary
            payment_date = (issue_date + relativedelta(months=+month)).date()
            if payment_date.day != issue_date.day:
                payment_date = payment_date.replace(day=min(issue_date.day, payment_date.day))

            # Store the payment details in the dictionary
            payments[payment_date.strftime("%Y-%m-%d")] = [monthly_payment, interest_payment, principal_payment]

        return payments




    def calculate_paygraph(self):
        ''' Функция для расчета и вывода графика платежей по кредиту
        '''
        self.graph_widget = Graph_window()
        self.graph_widget.show()
        pass

    def show_info(self):
        ''' Функция для вывода справочной информации по кредитованию
        '''
        self.info_widget = Info_window()
        self.info_widget.show()


class Info_window(QMainWindow, Ui_Form):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

class Graph_window(QMainWindow, ):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    window = Calculator_app()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()