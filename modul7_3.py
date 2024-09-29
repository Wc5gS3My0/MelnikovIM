import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower().translate(str.maketrans("", "", string.punctuation))
                    words.extend(line.split())
                all_words[file_name] = words
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        result = {}
        for name, words in all_words.items():
            if word.lower() in words:
                result[name] = words.index(word.lower())
        return result

    def count(self, word):
        all_words = self.get_all_words()
        result = {}
        for name, words in all_words.items():
            result[name] = words.count(word.lower())
        return result


with open('test_file.txt', 'w', encoding='utf-8') as f:
    f.write("It's a text for task найти везде. Используйте его для самопроверки. Успехов в решении задачи! TEXT text text.")


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
