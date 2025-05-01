class GameStats:
    def __init__(self, ai_game):
        self.game_active = True
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        self.lives = self.settings.lives
        self.last_advance = 0