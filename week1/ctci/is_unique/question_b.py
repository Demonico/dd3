class QuestionB:
    @staticmethod
    def is_unique(s:str) -> bool:
        if len(s) > 26: return False

        checker = 0
        for i in range(len(s)):
            # get the offset from 'a'
            val = ord(s[i]) - ord('a')
            # if bitshift val exists in checker, return False
            if (checker & (1 << val)) > 0: return False
            #  add val to checker
            checker |= (1 << val)

        return True
