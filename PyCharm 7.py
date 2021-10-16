class TooShortNameException(Exception):
    pass

def some_func(name):
    if len(name) < 3:
        raise TooShortNameException('Имя слишком короткое!')