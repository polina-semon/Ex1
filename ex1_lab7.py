import math
from abc import ABC, abstractmethod


class Base:

    def __init__(self, data, result):
        self.data = data
        self.result = result

    def get_answer(self):
        return [int(x >= 0.5) for x in self.data]

    @abstractmethod
    def get_score(self, ans):
        ans = self.get_answer()


class A(Base):

    def get_score(self, ans):
        super().get_score(ans)
        return sum([int(x == y) for (x, y) in zip(ans, self.result)]) / len(ans)

    def get_loss(self):
        return sum([(x - y) * (x - y) for (x, y) in zip(self.data, self.result)])


class B(Base):

    def get_loss(self):
        return -sum([y * math.log(x) + (1 - y) * math.log(1 - x) for (x, y) in zip(self.data, self.result)])

    def get_pre(self, ans):
        super().get_score(ans)
        res = [int(x == 1 and y == 1) for (x, y) in zip(ans, self.result)]
        return sum(res) / sum(ans)

    def get_rec(self, ans):
        super().get_score(ans)
        res = [int(x == 1 and y == 1) for (x, y) in zip(ans, self.result)]
        return sum(res) / sum(self.result)

    def get_score(self, ans):
        pre = self.get_pre(ans)
        rec = self.get_rec(ans)
        return 2 * pre * rec / (pre + rec)


class C(Base):

    def get_score(self, ans):
        super().get_score(ans)
        return sum([int(x == y) for (x, y) in zip(ans, self.result)]) / len(ans)

    def get_loss(self):
        return sum([abs(x - y) for (x, y) in zip(self.data, self.result)])