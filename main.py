from math import add
from person import Person

name = ""


def hello(rest: str):
    print(rest.upper())


def hello2(test: str):
    print(test.lower())


if __name__ == '__main__':
    # todo: Fix Bug
    # todo: Implement Tests
    print("Pycharm is Awesome")
answer = 6 / 2 * (1 + 2)
print(answer)
print(add(2, 2))
Fred = Person("Fred")

print(Fred)
name = "Dan"


def alexmethod():
    print(name)


alexmethod()
