# The class's name is in snake case, because of the condition of the task.


class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.current = 0
        self.counter = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter <= self.count:
            temp_var = self.current
            self.current += self.step
            self.counter += 1
            return temp_var

        raise StopIteration


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
