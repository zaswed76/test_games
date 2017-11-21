

class Task:
    def __init__(self):
        pass

class Game:
    def __init__(self, name):
        self.name = name

class Games:
    def __init__(self):
        self.games = {}
        self.current_game = None

    def add_game(self, game):
        self.games[game.name] = game

    def next_task(self):
        return self.current_game.task


if __name__ == '__main__':
    games = Games()


    game_1 = Game("game_1")
    games.add_game(game_1)
    games.current_game = "game_1"
    games.next_task()
