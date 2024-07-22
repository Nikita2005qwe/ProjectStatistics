from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
import matplotlib.pyplot as plt
from os import remove


class StatisticsInterpretation:
    """
    Класс выводящий диаграмму со статистикой по загруженному файлу
    """

    @staticmethod
    def showStatisticOnWords(number_of_words: dict[str, int], label_info: QLabel, word: str, name_diagram: str,
                             *, auto_delete: bool = True) -> None:
        """
        Выводит количество повторений данного слова в файле
        """
        plt.figure()
        x_list: list[str] = []
        y_list: list[int] = []
        for key in number_of_words:
            if key == word:
                x_list.append(key)
                y_list.append(number_of_words[key])
                break
        else:
            x_list.append(word)
            y_list.append(0)
        plt.bar(x_list, y_list)

        plt.savefig(name_diagram)
        screen = QPixmap(name_diagram)
        label_info.setPixmap(screen)
        
        if auto_delete:
            remove(name_diagram)

    @staticmethod
    def showStatisticOnFile(number_of_words: dict[str, int], number_of_letters: dict[str, int],
                            label_info: QLabel, name_diagram: str,
                            *, num_letters: int = 3, num_words: int = 3, num_long_words: int = 1,
                            auto_delete: bool = True) -> None:
        """
        Выводит наиболее повторяющуюся букву с количеством повторений,
        наиболее повторяющееся слово и самое длинное слово
        
        plt.subplot(число строк, число столбцов, индекс графика)
        """
        plt.figure()
        plt.subplot(2, 2, 1)
        x_list: list[str] = []
        y_list: list[int] = []
        cnt = 0
        for key in sorted(number_of_letters, key=number_of_letters.get, reverse=True):
            x_list.append(key)
            y_list.append(number_of_letters[key])
            cnt += 1
            if cnt == num_letters:
                cnt = 0
                break
        plt.bar(x_list, y_list)

        plt.subplot(2, 2, 3)
        x_list: list[str] = []
        y_list: list[int] = []
        for key in sorted(number_of_words, key=number_of_words.get, reverse=True):
            x_list.append(key)
            y_list.append(number_of_words[key])
            cnt += 1
            if cnt == num_words:
                cnt = 0
                break
        plt.bar(x_list, y_list)

        plt.subplot(2, 2, 2)
        x_list: list[str] = []
        y_list: list[int] = []
        for key in sorted(number_of_words, key=len, reverse=True):
            x_list.append(key)
            y_list.append(len(key))
            cnt += 1
            if cnt == num_long_words:
                break
        plt.bar(x_list, y_list)
        
        plt.savefig(name_diagram)
        screen = QPixmap(name_diagram)
        label_info.setPixmap(screen)
        
        if auto_delete:
            remove(name_diagram)
