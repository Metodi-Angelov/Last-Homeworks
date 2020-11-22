# The class's name is in snake case, because of the condition of the task.


class countdown_iterator:
    def __init__(self, count: int):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        # Zero is included
        if self.count >= 0:
            temp_var = self.count
            self.count -= 1
            return temp_var

        raise StopIteration


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
