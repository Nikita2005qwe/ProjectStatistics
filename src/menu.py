from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class UiMainWindow(object):
    def __init__(self):
        """
        Инициализация виджетов в основном окне
        
        labelStatistic - лэйбл отвечающий за вывод основной статистики
        label - лэйбл со статичной надписью
        loadFileButton - кнопка загрузки файлов
        showStatisticButton - кнопка выводящая статистику по загруженному файлу
        ExitButton - кнопка выхода из приложения
        showStatisticButton_2 - кнопка выводящая статистику по заданной последовательности символов
        lineEdit - виджет для ввода проверяемой последовательнсоти символов
        progressBar - полоса отображающая завершение анализа статистики
        
        """
        self.centralwidget: QtWidgets.QWidget = QtWidgets.QWidget(MainWindow)
        
        self.labelStatistic: QtWidgets.QLabel = QtWidgets.QLabel(self.centralwidget)
        self.label: QtWidgets.QLabel = QtWidgets.QLabel(self.centralwidget)
        
        self.loadFileButton: QtWidgets.QPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.showStatisticButton: QtWidgets.QPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExitButton: QtWidgets.QPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.showStatisticButton_2: QtWidgets.QPushButton = QtWidgets.QPushButton(self.centralwidget)
        
        self.lineEdit: QtWidgets.QLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.progressBar: QtWidgets.QProgressBar = QtWidgets.QProgressBar(self.centralwidget)
    
    def setupUi(self, main_window):
        """
        Функция устанавливающая расположение и размеры кнопок на основном окне
        
        font - стандартный шрифт
        font_low - шрифт размера 10 пт
        
        """
        main_window.setObjectName("main_window")
        main_window.resize(886, 600)
        
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        
        font_low = QtGui.QFont()
        font_low.setFamily("Microsoft YaHei")
        font_low.setPointSize(10)
        
        self.centralwidget.setObjectName("centralwidget")
        
        self.labelStatistic.setGeometry(QtCore.QRect(20, 9, 600, 570))
        self.labelStatistic.setObjectName("labelStatistic")
        
        self.loadFileButton.setGeometry(QtCore.QRect(630, 420, 240, 50))
        self.loadFileButton.setFont(font_low)
        self.loadFileButton.setObjectName("loadFileButton")
        
        self.showStatisticButton.setGeometry(QtCore.QRect(630, 480, 240, 50))
        self.showStatisticButton.setFont(font_low)
        self.showStatisticButton.setObjectName("showStatisticButton")
        
        self.ExitButton.setGeometry(QtCore.QRect(630, 540, 240, 50))
        self.ExitButton.setFont(font_low)
        self.ExitButton.setObjectName("ExitButton")
        
        self.lineEdit.setGeometry(QtCore.QRect(630, 60, 240, 50))
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        
        self.progressBar.setGeometry(QtCore.QRect(630, 380, 240, 30))
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        
        self.label.setGeometry(QtCore.QRect(630, 20, 240, 30))
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.label.setObjectName("label")
        
        self.showStatisticButton_2.setGeometry(QtCore.QRect(630, 120, 240, 50))
        self.showStatisticButton_2.setFont(font_low)
        self.showStatisticButton_2.setObjectName("showStatisticButton_2")

        self.addFunctions()
        
        main_window.setCentralWidget(self.centralwidget)
        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)
    
    def retranslateUi(self, main_window):
        """
        Функция добавляющая надписи на виджеты
        """
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "MainWindow"))
        self.loadFileButton.setText(_translate("main_window", "Загрузка файла"))
        self.showStatisticButton.setText(_translate("main_window", "Отображение статистики"))
        self.ExitButton.setText(_translate("main_window", "Выход"))
        self.label.setText(_translate("main_window", "Поиск слова"))
        self.showStatisticButton_2.setText(_translate("main_window", "Количество совпадений"))
    
    def addFunctions(self):
        """
        Функция добавляющая функционал кнопкам
        """
        button_assignment: dict[QtWidgets.QPushButton, callable] = {
            self.loadFileButton: self.loadFile,
            self.showStatisticButton: self.showStatistic,
            self.ExitButton: self.Exit,
            self.showStatisticButton_2: self.showStatisticOnWord,
        }
        for btn in button_assignment:
            btn.clicked.connect(button_assignment[btn])
    
    def loadFile(self):
        """
        Функция загрузки файлов расширения .txt
        """
        pass
    
    def showStatistic(self):
        """
        Функция отображающая статистику по загруженному файлу
        """
        pass
    
    def Exit(self):
        """
        Функция осуществляющая корректный выход из приложения
        """
        pass
    
    def showStatisticOnWord(self):
        """
        Функция отображающая статистику по введённой последовательности символов
        в загруженном файле
        """
        pass
    
    def isLoaded(self):
        """
        Функция показывающая загружен ли в данный момент файл
        """
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
