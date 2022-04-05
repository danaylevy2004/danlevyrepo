class factorial:
    def __init__(self):
        self.factorial = [0, 1]

    def __call__(self, n):
        if n < len(self.factorial):
            return self.factorial[n]
        else:
            # Compute the requested Fibonacci number
            fac_number = n * self(n-1) # two recursive calls to self (__call__(self, n))
            self.factorial.append(fac_number)
        return self.factorial[n]