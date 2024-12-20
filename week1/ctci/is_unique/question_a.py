class QuestionA:
    @staticmethod
    def is_unique(s: str) -> bool:
        # Check if string length is longer than the set of ascii chars
        if len(s) > 128: return False

        char_set = [False for _ in range(128)]
        for char in s:
            val = ord(char)
            if char_set[val]: return False
            char_set[val] = True
        return True

