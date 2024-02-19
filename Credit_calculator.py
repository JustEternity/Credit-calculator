# Form implementation generated from reading ui file 'D:\PyProjects\Repositories\Credit_calc\MainWindow2.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 571)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(960, 571))
        MainWindow.setMaximumSize(960, 571)
        MainWindow.setMouseTracking(False)
        MainWindow.setFocusPolicy(QtCore.Qt.FocusPolicy.WheelFocus)
        icon = QtGui.QIcon.fromTheme("accessories-calculator")
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget {\n"
                                        "background-color: #ebfabe;\n"
                                        "}")
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 920, 531))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())

        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(920, 480))
        self.groupBox.setSizeIncrement(QtCore.QSize(20, 20))
        self.groupBox.setBaseSize(QtCore.QSize(920, 590))
        self.groupBox.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet("#groupBox {\n"
                                        "background-color: #cfffd7;\n"
                                        "border-radius: 70px;\n"
                                        "border: 4px inset gray;\n"
                                        "}")
        self.groupBox.setTitle("")
        self.groupBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupBox.setObjectName("groupBox")

        self.calculation_button = QtWidgets.QPushButton(parent=self.groupBox)
        self.calculation_button.setGeometry(QtCore.QRect(650, 380, 211, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.calculation_button.setFont(font)
        self.calculation_button.setStyleSheet("#calculation_button {\n"
                                                "border-radius: 30px;\n"
                                                "background-color: #f5f754;\n"
                                                "}")
        self.calculation_button.setObjectName("calculation_button")

        self.info_button = QtWidgets.QPushButton(parent=self.groupBox)
        self.info_button.setGeometry(QtCore.QRect(864, 30, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.info_button.setFont(font)
        self.info_button.setStyleSheet("#info_button {\n"
                                        "background-color: #f5f754;\n"
                                        "border-radius: 10%;\n"
                                        "}")
        self.info_button.setObjectName("info_button")

        self.layoutWidget = QtWidgets.QWidget(parent=self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 60, 801, 102))
        self.layoutWidget.setObjectName("layoutWidget")

        self.data_input = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.data_input.setContentsMargins(0, 0, 0, 0)
        self.data_input.setSpacing(10)
        self.data_input.setObjectName("data_input")

        self.credit_sum = QtWidgets.QGroupBox(parent=self.layoutWidget)
        self.credit_sum.setMinimumSize(QtCore.QSize(192, 100))
        self.credit_sum.setMaximumSize(QtCore.QSize(192, 16777215))
        self.credit_sum.setStyleSheet("#credit_sum {\n"
                                        "background-color: #fcc288;\n"
                                        "border-radius: 50%;\n"
                                        "}")
        self.credit_sum.setTitle("")
        self.credit_sum.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.credit_sum.setObjectName("credit_sum")

        self.gridLayout = QtWidgets.QGridLayout(self.credit_sum)
        self.gridLayout.setContentsMargins(-1, 3, -1, 9)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")

        self.enter_sum = QtWidgets.QLineEdit(parent=self.credit_sum)
        self.enter_sum.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.enter_sum.setFont(font)
        self.enter_sum.setStyleSheet("#enter_sum {\n"
                                    "background: transparent;\n"
                                    "border: none;\n"
                                    "}")
        self.enter_sum.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.enter_sum.setClearButtonEnabled(False)
        self.enter_sum.setObjectName("enter_sum")
        self.enter_sum.setPlaceholderText('0')

        self.gridLayout.addWidget(self.enter_sum, 1, 0, 1, 1)
        self.label_sum = QtWidgets.QLabel(parent=self.credit_sum)
        self.label_sum.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_sum.setFont(font)
        self.label_sum.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_sum.setObjectName("label_sum")

        self.gridLayout.addWidget(self.label_sum, 0, 0, 1, 1)
        self.data_input.addWidget(self.credit_sum)
        self.credit_date = QtWidgets.QGroupBox(parent=self.layoutWidget)
        self.credit_date.setMinimumSize(QtCore.QSize(192, 100))
        self.credit_date.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.credit_date.setStyleSheet("#credit_date {\n"
                                        "background-color: #fcc288;\n"
                                        "border-radius: 50%;\n"
                                        "}")
        self.credit_date.setTitle("")
        self.credit_date.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.credit_date.setObjectName("credit_date")

        self.gridLayout_4 = QtWidgets.QGridLayout(self.credit_date)
        self.gridLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")

        self.cred_date = QtWidgets.QLabel(parent=self.credit_date)
        self.cred_date.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.cred_date.setFont(font)
        self.cred_date.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.cred_date.setObjectName("cred_date")

        self.gridLayout_4.addWidget(self.cred_date, 0, 0, 1, 1)
        self.choice_date = QtWidgets.QGroupBox(parent=self.credit_date)
        self.choice_date.setMaximumSize(QtCore.QSize(112, 35))
        self.choice_date.setStyleSheet("#choice_date {\n"
                                        "border: none;\n"
                                        "}")
        self.choice_date.setTitle("")
        self.choice_date.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.choice_date.setObjectName("choice_date")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.choice_date)
        self.verticalLayout_2.setContentsMargins(15, -1, 5, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.dateEdit = QtWidgets.QDateEdit(parent=self.choice_date)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("#dateEdit {\n"
                                "background: transparent;\n"
                                "border: none;\n"
                                "}")
        self.dateEdit.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDate|QtCore.Qt.InputMethodHint.ImhPreferNumbers)
        self.dateEdit.setWrapping(False)
        self.dateEdit.setFrame(True)
        self.dateEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.dateEdit.setAccelerated(False)
        self.dateEdit.setProperty("showGroupSeparator", False)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")

        self.verticalLayout_2.addWidget(self.dateEdit)

        self.gridLayout_4.addWidget(self.choice_date, 1, 0, 1, 1)

        self.data_input.addWidget(self.credit_date)

        self.rate = QtWidgets.QGroupBox(parent=self.layoutWidget)
        self.rate.setMinimumSize(QtCore.QSize(192, 100))
        self.rate.setMaximumSize(QtCore.QSize(192, 16777215))
        self.rate.setStyleSheet("#rate {\n"
                                "background-color: #fcc288;\n"
                                "border-radius: 50%;\n"
                                "}")
        self.rate.setTitle("")
        self.rate.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.rate.setObjectName("rate")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.rate)
        self.gridLayout_2.setContentsMargins(-1, -1, -1, 10)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.label_rate = QtWidgets.QLabel(parent=self.rate)
        self.label_rate.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_rate.setFont(font)
        self.label_rate.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_rate.setAutoFillBackground(False)
        self.label_rate.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.label_rate.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label_rate.setScaledContents(False)
        self.label_rate.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_rate.setWordWrap(True)
        self.label_rate.setObjectName("label_rate")

        self.gridLayout_2.addWidget(self.label_rate, 1, 0, 1, 1)

        self.rate_enter = QtWidgets.QLineEdit(parent=self.rate)
        self.rate_enter.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.rate_enter.setFont(font)
        self.rate_enter.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.rate_enter.setStyleSheet("#rate_enter {\n"
                                        "background: transparent;\n"
                                        "border: none;\n"
                                        "margin-left: 50px;\n"
                                        "}")
        self.rate_enter.setFrame(True)
        self.rate_enter.setCursorPosition(3)
        self.rate_enter.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTop|QtCore.Qt.AlignmentFlag.AlignTrailing)
        self.rate_enter.setDragEnabled(False)
        self.rate_enter.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.LogicalMoveStyle)
        self.rate_enter.setClearButtonEnabled(False)
        self.rate_enter.setObjectName("rate_enter")
        self.rate_enter.setPlaceholderText('0.0')

        self.gridLayout_2.addWidget(self.rate_enter, 3, 0, 1, 1)

        self.data_input.addWidget(self.rate)

        self.term = QtWidgets.QGroupBox(parent=self.layoutWidget)
        self.term.setMinimumSize(QtCore.QSize(192, 100))
        self.term.setMaximumSize(QtCore.QSize(192, 100))
        self.term.setStyleSheet("#term {\n"
                                "background-color: #fcc288;\n"
                                "border-radius: 50%;\n"
                                "}")
        self.term.setTitle("")
        self.term.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.term.setObjectName("term")

        self.gridLayout_3 = QtWidgets.QGridLayout(self.term)
        self.gridLayout_3.setContentsMargins(-1, -1, -1, 12)
        self.gridLayout_3.setHorizontalSpacing(20)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.label_term = QtWidgets.QLabel(parent=self.term)
        self.label_term.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_term.setFont(font)
        self.label_term.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_term.setAutoFillBackground(False)
        self.label_term.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.label_term.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label_term.setScaledContents(False)
        self.label_term.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_term.setWordWrap(True)
        self.label_term.setObjectName("label_term")

        self.gridLayout_3.addWidget(self.label_term, 1, 0, 1, 1)

        self.credit_term = QtWidgets.QHBoxLayout()
        self.credit_term.setContentsMargins(40, -1, 50, 0)
        self.credit_term.setSpacing(0)
        self.credit_term.setObjectName("credit_term")

        self.enter_term = QtWidgets.QLineEdit(parent=self.term)
        self.enter_term.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.enter_term.setFont(font)
        self.enter_term.setStyleSheet("#enter_term {\n"
                                        "border: none;\n"
                                        "background: transparent;\n"
                                        "}")
        self.enter_term.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.enter_term.setObjectName("enter_term")
        self.enter_term.setPlaceholderText('0')

        self.credit_term.addWidget(self.enter_term)

        self.choice_term = QtWidgets.QComboBox(parent=self.term)
        self.choice_term.setMinimumSize(QtCore.QSize(50, 0))
        self.choice_term.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.choice_term.setFont(font)
        self.choice_term.setStyleSheet("#choice_term {\n"
                                        "background: transparent;\n"
                                        "border: none;\n"
                                        "}")
        self.choice_term.setObjectName("choice_term")
        self.choice_term.addItem("")
        self.choice_term.addItem("")

        self.credit_term.addWidget(self.choice_term)

        self.gridLayout_3.addLayout(self.credit_term, 2, 0, 1, 1)

        self.data_input.addWidget(self.term)

        self.user_res = QtWidgets.QGroupBox(parent=self.groupBox)
        self.user_res.setGeometry(QtCore.QRect(60, 280, 311, 181))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_res.setFont(font)
        self.user_res.setStyleSheet("#user_res {\n"
                                "border-radius: 30%;\n"
                                "background: #ebfabe;\n"
                                "}")
        self.user_res.setTitle("")
        self.user_res.setObjectName("user_res")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.user_res)
        self.verticalLayout.setObjectName("verticalLayout")

        self.amount_payments = QtWidgets.QLabel(parent=self.user_res)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.amount_payments.setFont(font)
        self.amount_payments.setObjectName("amount_payments")

        self.verticalLayout.addWidget(self.amount_payments)

        self.month_payment = QtWidgets.QLabel(parent=self.user_res)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.month_payment.setFont(font)
        self.month_payment.setObjectName("month_payment")

        self.verticalLayout.addWidget(self.month_payment)

        self.overpayment = QtWidgets.QLabel(parent=self.user_res)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.overpayment.setFont(font)
        self.overpayment.setObjectName("overpayment")

        self.verticalLayout.addWidget(self.overpayment)

        self.paygraph_button = QtWidgets.QPushButton(parent=self.groupBox)
        self.paygraph_button.setGeometry(QtCore.QRect(400, 410, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.paygraph_button.setFont(font)
        self.paygraph_button.setStyleSheet("#paygraph_button {\n"
                                        "background-color: #ebfabe;\n"
                                        "border-radius: 25px;\n"
                                        "border: 2px solid gray;\n"
                                        "}")
        self.paygraph_button.setAutoRepeat(False)
        self.paygraph_button.setAutoExclusive(False)
        self.paygraph_button.setAutoDefault(False)
        self.paygraph_button.setDefault(False)
        self.paygraph_button.setFlat(False)
        self.paygraph_button.setObjectName("paygraph_button")

        self.layoutWidget1 = QtWidgets.QWidget(parent=self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(60, 170, 801, 51))
        self.layoutWidget1.setObjectName("layoutWidget1")

        self.type_of_credit = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.type_of_credit.setContentsMargins(0, 0, 0, 0)
        self.type_of_credit.setObjectName("type_of_credit")

        self.label_credit_type = QtWidgets.QLabel(parent=self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_credit_type.setFont(font)
        self.label_credit_type.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_credit_type.setObjectName("label_credit_type")

        self.type_of_credit.addWidget(self.label_credit_type)

        self.radioButton_1 = QtWidgets.QRadioButton(parent=self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.radioButton_1.setFont(font)
        self.radioButton_1.setStyleSheet("#radioButton_1 {\n"
                                        "  padding: 10px 20px; \n"
                                        "  font-family: Arial, sans-serif; \n"
                                        "  cursor: pointer; \n"
                                        "  border: 1px solid #000; \n"
                                        "  border-radius: 5px; \n"
                                        "  margin: 5px; \n"
                                        "  background-color: #ebfabe; \n"
                                        "}\n"
                                        "\n"
                                        "#radioButton_1:checked {\n"
                                        "  background-color: #fcc288; \n"
                                        "  color: white; \n"
                                        "}")
        self.radioButton_1.setObjectName("radioButton_1")

        self.type_of_credit.addWidget(self.radioButton_1)

        self.radioButton_2 = QtWidgets.QRadioButton(parent=self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("#radioButton_2 {\n"
                                        "  padding: 10px 20px; /* Отступы вокруг метки */\n"
                                        "  font-family: Arial, sans-serif; /* Выбор шрифта */\n"
                                        "  cursor: pointer; /* Изменение курсора при наведении */\n"
                                        "  border: 1px solid #000; /* Граница */\n"
                                        "  border-radius: 5px; /* Закругление углов */\n"
                                        "  margin: 5px; /* Отступы вокруг Radio-кнопки */\n"
                                        "  background-color: #ebfabe; /* Цвет фона по умолчанию */\n"
                                        "}\n"
                                        "\n"
                                        "#radioButton_2:checked {\n"
                                        "  background-color: #fcc288; /* Цвет фона при выборе */\n"
                                        "  color: white; /* Цвет текста при выборе */\n"
                                        "}")
        self.radioButton_2.setObjectName("radioButton_2")

        self.type_of_credit.addWidget(self.radioButton_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.calculation_button.setText(_translate("MainWindow", "Рассчитать"))
        self.info_button.setText(_translate("MainWindow", "?"))
        self.label_sum.setText(_translate("MainWindow", "Сумма кредита"))
        self.cred_date.setText(_translate("MainWindow", "Дата выдачи"))
        self.label_rate.setText(_translate("MainWindow", "Процентная ставка (% годовых)"))
        self.label_term.setText(_translate("MainWindow", "Срок кредита"))
        self.choice_term.setCurrentText(_translate("MainWindow", "лет"))
        self.choice_term.setItemText(0, _translate("MainWindow", "лет"))
        self.choice_term.setItemText(1, _translate("MainWindow", "мес."))
        self.amount_payments.setText(_translate("MainWindow", "Сумма выплат:"))
        self.month_payment.setText(_translate("MainWindow", "Ежемесячный платеж:"))
        self.overpayment.setText(_translate("MainWindow", "Сумма переплаты:"))
        self.paygraph_button.setText(_translate("MainWindow", "График платежей"))
        self.label_credit_type.setText(_translate("MainWindow", "Вид платежа:"))
        self.radioButton_1.setText(_translate("MainWindow", "Аннуитентный"))
        self.radioButton_2.setText(_translate("MainWindow", "Дифференцированный"))
