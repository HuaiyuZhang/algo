def truncateSentence(self, s: str, k: int) -> str:
        a = s.split()
        return ' '.join(a[:(k)])