import operator
import random

class Operator():
    Add = "add"
    Sub = "sub"
    Mul = "mul"
    operations = dict(
        add={"sign": "+", "meth": operator.add},
        sub={"sign": "-", "meth": operator.sub},
        mul={"sign": "*", "meth": operator.mul}
    )

    def __init__(self, operator_line: str):
        self.operator_line = operator_line

    def sign(self):
        return self.operations[self.operator_line]["sign"]

    def method(self, *args):
        return self.operations[self.operator_line]["meth"](*args)

class AutoTask:
    def __init__(self, level, term, operator_line: str):
        self.operator = Operator(operator_line)
        self.term = term
        self.level = level

    @property
    def text(self):
        return "{}    {}    {}".format(self.level,
                                       self.operator.sign(),
                                       self.term)

    @property
    def answer(self):
        return self.operator.method(self.level, self.term)

    def __repr__(self):
        return "{}: ({} {} {})".format(self.__class__.__name__, self.level,
                                self.operator.sign(), self.term)

class Task:
    def __init__(self, task_line):
        self.task_line = task_line

    def __repr__(self):
        return "{} - {}".format(self.__class__.__name__, self.task_line)


class Tasks:
    def __init__(self, *args):
        self.tasks = []

    def mix(self):
        random.shuffle(self.tasks)

    def increase(self, multiplier):
        if multiplier > 0:
            self.tasks*=multiplier


class UserTasks(Tasks):
    def __init__(self, task_list, *args):
        super().__init__(*args)
        self.task_list = task_list
        self.tasks = []

    def create_tasks(self):
        for task in self.task_list:
            self.tasks.append(Task(task))

    def __repr__(self):
        return "{} - {}".format(
            self.__class__.__name__, self.tasks.__class__.__name__)

class AutoTasks(Tasks):
    def __init__(self, level, operand, *args):
        super().__init__(*args)
        self.operand = operand
        self.level = level
        self.tasks = []

    def __repr__(self):
        return "{}\n{}".format(self.operand, self.level)

    def __str__(self):
        return "{}\n{}".format(self.operand, self.level)

    def create_tasks(self):

        self.tasks.clear()

        seq = range(1, 11)

        for t in seq:
            if self.operand in [Operator.Add, Operator.Mul]:
                self.tasks.append(AutoTask(self.level, t, self.operand))
            elif self.level >= t:
                self.tasks.append(AutoTask(self.level, t, self.operand))


class Game:
    def __init__(self, task_object):

        self.task_object = task_object
        self.task_object.create_tasks()

    def mix_tasks(self):
        self.task_object.mix()

    def tasks_increase(self, multiplier):
        self.task_object.increase(multiplier)

    def __repr__(self):
        return str(self.task_object.tasks)




if __name__ == '__main__':


    game = Game(AutoTasks(7, "mul"))
    game.tasks_increase(3)
    game.mix_tasks()

    print(game)