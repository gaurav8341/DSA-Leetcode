class Solution:
    def kthCharacter(self, k: int) -> str:
        word = 'a'

        while True:
            if len(word) >= k:
                return word[k-1]
            anti_word = ''
            for c in word:
                a_c = (ord(c) + 1) % ord('a')
                anti_word += chr(a_c + ord('a'))
            word += anti_word