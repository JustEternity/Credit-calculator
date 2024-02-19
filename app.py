import sys

from Credit_calculator import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow, QButtonGroup, QMessageBox


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
        self.all_payments_annuty = self.month_payment_annuty * 12 * self.term
        self.annuty_overpayment = self.all_payments_annuty - self.sum

        self.amount_payments.setText(f'Сумма выплат: {self.all_payments_annuty:.2f} руб.')
        self.month_payment.setText(f"Ежемесячный платеж: {self.month_payment_annuty:.2f} руб.")
        self.overpayment.setText(f"Сумма переплаты: {self.annuty_overpayment:.2f} руб.")



    def calculate_diff(self):
        ''' Функция для расчета суммы основного долга для каждого платежа, ежемесячный платеж уменьшается со временем,
        поэтому он показывается только в разделе "График платежей"
        '''
        self.type_term = 1 if self.choice_term.currentText() == 'мес.' else 12
        # Часть основного долга, одинаковая для каждого месяца (платежа)
        self.part_of_debt = self.sum / (self.term*self.type_term)
        # Сумма процентов по дифференцированному платежу
        self.percents_diff = (self.term * (self.term + 1) * (self.rate/100))/2 *self.sum
        # Сумма общего долга
        self.all_payments_diff = self.sum + self.percents_diff

        self.amount_payments.setText(f"Ежемесячный платеж по\nосновному долгу: {self.part_of_debt:.2f} руб.")
        self.month_payment.setText(f"Для получения более подробной\nинформации о платежах по\nдифференцированному кредиту,\nобратитесь к графику платежей.")
        self.overpayment.setText(f"")


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
        pass


class Info_window(QMainWindow):
    def __init__(self) -> None:
        super().__init__()




class Graph_window(QMainWindow):
    def __init__(self) -> None:
        super().__init__()


def main():
    app = QApplication(sys.argv)
    window = Calculator_app()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()