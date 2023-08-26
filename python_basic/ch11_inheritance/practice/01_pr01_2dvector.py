class C2dVector:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"


class C3dVector(C2dVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"


c2dvector = C2dVector(1, 3)
c3dVector = C3dVector(1, 9, 7)
print(c2dvector)
print(c3dVector)
