
class ATasks:
    def __init__(self, *args):
        self.tasks = []




class UserTasks(ATasks):
    def __init__(self, task_list, *args):
        super().__init__(*args)
        self.task_list = task_list
        self.tasks = []


    def __repr__(self):
        return str(self.task_list)

    def create_task(self):
        self.tasks.extend(self.task_list)


class AutoTasks(ATasks):
    def __init__(self, level, operand, *args):
        super().__init__(*args)
        self.operand = operand
        self.level = level
        self.tasks = []


    def __repr__(self):
        return "{}\n{}".format(self.operand, self.level)

    def create_task(self):
        self.tasks.extend([self.operand, self.level])

class Game:
    def __init__(self, tasks):
        self.tasks = tasks
        self.tasks.create_task()

    def __repr__(self):
        return str(self.tasks)




if __name__ == '__main__':
    g = Game(UserTasks(["2+3"]))
    print(g)

    g2 = Game(AutoTasks(1, "add"))
    print(g2)