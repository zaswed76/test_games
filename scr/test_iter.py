from collections import  Iterator

class Game(Iterator):

    def __init__(self, tasks=None):
        if tasks is not None:
             self.tasks = tasks
        self.cursor = -1


    def __iter__(self):
        return self



    def __next__(self):
        if self.cursor < len(self.tasks):
            self.cursor += 1
            return self.tasks[self.cursor]
        else:
            raise StopIteration

if __name__ == '__main__':
    g = Game([1, 2, 3])
    for t in g:
        print(t)