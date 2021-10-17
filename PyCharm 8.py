
class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, x):
        if int(x) > 0:
            super().append(x)
        else:
            raise NonPositiveError

a = PositiveList()
a.append(-7)

print(a)

