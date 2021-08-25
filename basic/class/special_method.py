# str이 가장 많이 쓰인다.
class Word(object):

    def __init__(self, text) -> None:
        self.text = text

    def __str__(self) -> str:
        return 'Word!!!!!!'

    def __len__(self):
        return len(self.text)

    def __add__(self, word):
        return self.text.lower() + word.text.lower()

    def __eq__(self, word):
        return self.text.lower == word.text.lower()

w = Word('test')
w1 = Word('#####')
# test#####
print(w + w1)
print(w == w1) # False
