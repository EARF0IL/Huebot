class Huenizator:
    source_word: str
    huenizated_word: str
    vowel_letters: dict[str, str]

    def __init__(self, word: str):
        self.source_word = word.lower()
        self.huenizated_word = ''
        self.vowel_letters = {'у': 'ю', 'е': 'е', 'ы': 'и',
                              'а': 'я', 'о': 'ё', 'э': 'й',
                              'я': 'я', 'и': 'и', 'ю': 'ю', 'ё': 'ё'}

    def _huenizaton(self) -> None:
        if self.huenizated_word:
            return
        first_vowel_letter_index = 0
        while self.source_word[first_vowel_letter_index] not in self.vowel_letters.keys():
            first_vowel_letter_index += 1
        first_vowel_letter = self.source_word[first_vowel_letter_index]
        self.huenizated_word = 'ху' +\
                               self.vowel_letters[first_vowel_letter] +\
                               self.source_word[first_vowel_letter_index + 1:]

        



    def get_source_word(self) -> str:
        return self.source_word

    def get_huenizated_word(self) -> str:
        self._huenizaton()
        return self.huenizated_word
