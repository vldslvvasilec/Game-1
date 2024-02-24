from .exceptions import GameOver
from .models import Enemy
from .score import ScoreHandler
from .settings import WIN, LOSE

class Game:
    def __init__(self, player, mode) -> None:
        self.player = player
        self.mode = mode
        self.enemy = None

    def play(self) -> None:
        self.enemy = Enemy(self.player.level, self.mode)
        while self.player.is_alive() and self.enemy.is_alive():
            self.fight()
        self.handle_fight_result()
        self.save_score()

    def fight(self) -> None:
        print("Выберите вашу атаку:")
        player_attack = self.player.select_attack()
        enemy_attack = self.enemy.select_attack()
        self.determine_fight_outcome(player_attack, enemy_attack)

    def determine_fight_outcome(self, player_attack: str, enemy_attack: str) -> None:
        outcome = self.player.determine_attack_outcome(player_attack, enemy_attack)
        self.process_fight_outcome(outcome)

    def process_fight_outcome(self, outcome: int) -> None:
        if outcome == WIN:
            print("Победа! Получено очков за убийство.")
            print(f"Ваши текущие очки: {self.player.score}")  # Вывод текущих очков
        elif outcome == LOSE:
            print("Поражение. Потеряно жизней.")
            print(f"Ваши текущие жизни: {self.player.lives}")  # Вывод текущего количества жизней
            self.player.decrease_lives()
        else:
            print("Ничья. Получено 0 очков за бой.")
            print(f"Ваши текущие очки: {self.player.score}")  # Вывод текущих очков

    def handle_fight_result(self) -> None:
        try:
            if not self.player.is_alive():
                raise GameOver("Игра окончена! Закончились жизни игрока.")
            elif not self.enemy.is_alive():
                raise GameOver("Поздравляем! Вы победили врага.")
        except GameOver as e:
            print(e)
            pass

    def save_score(self) -> None:
        score_handler = ScoreHandler()
        score_handler.add_score(self.player.name, self.mode, self.player.score)
        score_handler.save()
        score_handler.display()
