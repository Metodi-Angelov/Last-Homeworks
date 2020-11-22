# The class's name is in snake case, because of the condition of the task.

class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.dictionary):
            i = self.index
            self.index += 1
            return list(self.dictionary.items())[i]

        raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
