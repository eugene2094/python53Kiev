# Class responsible for reading and writing data to a text file
from abc import ABC, abstractmethod


class DataSource(ABC):
    def __init__(self, path):
        self.path = path

    @abstractmethod
    def read_text_data(self):
        pass

    @abstractmethod
    def write_text_data(self):
        pass


class TextDataSource(DataSource):
    # Reads the data from the file
    def read_text_data(self):
        with open(self.path, 'r') as file:
            data = file.read()
        return data

    # Writes data to the file
    def write_text_data(self, data):
        with open(self.path, 'w') as file:
            file.write(data)


class CloudDataSource(DataSource):
    # Reads the data from the file
    def read_text_data(self):
        with open(self.path, 'r') as file:
            data = file.read()
        return data

    # Writes data to the file
    def write_text_data(self, data):
        with open(self.path, 'w') as file:
            file.write(data)


# Class for operations on the text data
class TextOperations:
    def __init__(self, DataSource):
        self.text_source = DataSource
        self.data = self.text_source.read_text_data()

    # Searches for a word in the data
    def search_for_word(self, word):
        return word in self.data

    # Counts the occurrences of a word in the data
    def count_occurences(self, word):
        return self.data.count(word)


# file = TextFileOperations("output.txt")
#
# obj = TextOperations(file)
# print(f"{obj.search_for_word('more')}")
# print(f"{obj.count_occurences('be')}")
