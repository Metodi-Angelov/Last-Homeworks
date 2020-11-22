# The class's name is in snake case, because of the condition of the task.

class sequence_repeat:
    def __init__(self, sequence, number: int):
        self.sequence = sequence
        self.number = number
        self.length = len(sequence)
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == self.length:
            self.current = 0
        if self.current < self.length and self.number:
            i = self.current
            self.current += 1
            self.number -= 1
            return self.sequence[i]

        raise StopIteration


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
