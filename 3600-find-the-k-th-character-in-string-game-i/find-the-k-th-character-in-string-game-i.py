class Solution:
    def kthCharacter(self, k: int) -> str:
        word = 'a'

        while True:
            if len(word) >= k:
                return word[k-1]
            anti_word = ''
            for c in word:
                a_c = (ord(c) + 1) % 97
                # 97 is ascii value of a
                anti_word += chr(a_c + 97)
            word += anti_word