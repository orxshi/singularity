def step(x, a):
    if x >= a:
        return 1
    return 0

def bracket(x, a, n):
    return step(x, a) * (x - a) ** n


class Loading:
    def __add__(self, other):
        l = Loading()
        l.w = self.w + other.w
        l.V = self.V + other.V
        l.M = self.M + other.M
        return l

class ConMoment(Loading):
    def __init__(self, Mo, x, a):
        self.w = 0
        self.V = 0
        self.M = -Mo * bracket(x, a, 0)

class ConLoad(Loading):
    def __init__(self, P, x, a):
        self.w = 0
        self.V = -P * bracket(x, a, 0)
        self.M = -P * bracket(x, a, 1)

class UniLoad(Loading):
    def __init__(self, wo, x, a):
        self.w = wo * bracket(x, a, 0)
        self.V = -wo * bracket(x, a, 1)
        self.M = -0.5 * wo * bracket(x, a, 2)

class LinLoad(Loading):
    def __init__(self, k, x, a):
        self.w = k * bracket(x, a, 1)
        self.V = -0.5 * k * bracket(x, a, 2)
        self.M = -k / 6 * bracket(x, a, 3)