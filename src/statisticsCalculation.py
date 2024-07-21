import re
from PyQt5 import QtWidgets

class StatisticsCalculation:
    def __init__(self, path: str, progress_bar: QtWidgets.QProgressBar):
        self.numberOfWords: dict[str, int] = self.wordCount(path, progress_bar)
        self.numberOfLetters: dict[str, int] = self.letterCount(self.numberOfWords, progress_bar)
        
    @staticmethod
    def wordCount(path: str, progress_bar: QtWidgets.QProgressBar) -> dict[str, int]:
        number_of_words: dict[str, int] = dict()
        file_size = sum(1 for _ in open(path, "r"))
        with open(path, encoding="utf-8") as file:
            cnt = 0
            for string in file:
                word_list: list[str] = re.split(r"[-,.!/<>():;?\n\t ]+", string)
                for word in word_list:
                    if not word:
                        continue
                    try:
                        number_of_words[word] += 1
                    except KeyError:
                        number_of_words[word] = 1
                progress_bar.setValue(int(cnt/file_size*50))
                cnt += 1
            progress_bar.setValue(int(50))
        return number_of_words
    
    @staticmethod
    def letterCount(number_of_words: dict[str, int], progress_bar: QtWidgets.QProgressBar) -> dict[str, int]:
        number_of_letters: dict[str, int] = dict()
        file_size = len(number_of_words)
        cnt = 0
        for word in number_of_words:
            for letter in word:
                try:
                    number_of_letters[letter] += number_of_words[word]
                except KeyError:
                    number_of_letters[letter] = number_of_words[word]
            progress_bar.setValue(int(50+(cnt / file_size) * 50))
            cnt += 1
        progress_bar.setValue(int(100))
        return number_of_letters
    
    def getNumberOfWords(self) -> dict[str, int]:
        return self.numberOfWords
    
    def getNumberOfLetters(self) -> dict[str, int]:
        return self.numberOfLetters
