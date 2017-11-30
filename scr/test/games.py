

class Task:
    def __init__(self):
        pass

class Game:
    def __init__(self, name):
        self.name = name

    def next_task(self) ->Task:
        return

    def reset(self):
        return

    def create_tasks(self, **kwargs):
        pass


class Games:
    def __init__(self):
        self.games = {}
        self._current_game = None

    def add_game(self, game):
        self.games[game.name] = game

    def next_task(self):
        return self._current_game.task

    @property
    def current_game(self):
        return self._current_game

    @current_game.setter
    def current_game(self, game):
        self._current_game = game

if __name__ == '__main__':
    games = Games()


    game_1 = Game("game_1")
    games.add_game(game_1)
    games.current_game = "game_1"

