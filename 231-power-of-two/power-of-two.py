from collections import Counter
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # in the bit representation there only be one 1

        # we get bit representation of n # we count the ones in it

        if n < 0:
            return False
            
        n_bin = Counter(bin(n))

        if n_bin.get('1', 0) == 1:
            return True
        return False

