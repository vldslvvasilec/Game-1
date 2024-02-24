import random
from .settings import PLAYER_LIVES, ALLOWED_ATTACKS
from .exceptions import GameOver, EnemyDown

class PlayerRecord:
    def __init__(self, name: str, mode: str, score: int) -> None:
        self.name = name
        self.mode = mode
        self.score = score

    def __eq__(self, other: "PlayerRecord") -> bool:
        return self.name == other.name and self.mode == other.mode

    def __gt__(self, other: "PlayerRecord") -> bool:
        return self.score > other.score

    def __str__(self) -> str:
        return f"| {self.name} | {self.mode} | {self.score} |"

class Player:
    def __init__(self, name: str, difficulty: str) -> None:
        self.name = name
        self.lives = PLAYER_LIVES
        self.score = 0
        self.difficulty = difficulty
        self.level = 1

    def select_attack(self) -> str:
        while True:
            for key, value in ALLOWED_ATTACKS.items():
                print(f"{key}. {value}")

            print("Q. Quit")  # Добавили опцию выхода
            choice = input("Введите 1, 2, 3 или Q: ")

            if choice.upper() == 'Q':  # Добавили проверку на выход
                print(f"Выход из игры. Ваши текущие очки: {self.score}")
                exit()

            if choice in ALLOWED_ATTACKS:
                return ALLOWED_ATTACKS[choice]

            print("Неверный выбор. Пожалуйста, попробуйте снова.")

    def decrease_lives(self) -> None:
        self.lives -= 1
        if self.lives == 0:
            raise GameOver("Игра окончена! У вас закончились жизни.")

    def add_points(self, points: int) -> None:
        self.score += points

    def determine_attack_outcome(self, player_attack: str, enemy_attack: str) -> int:
        if player_attack == enemy_attack:
            return 0
        elif (
            (player_attack == "Paper" and enemy_attack == "Stone") or
            (player_attack == "Stone" and enemy_attack == "Scissors") or
            (player_attack == "Scissors" and enemy_attack == "Paper")
        ):
            return 1
        else:
            return -1

    def is_alive(self) -> bool:
        return self.lives > 0

    def get_record(self) -> PlayerRecord:
        return PlayerRecord(self.name, self.difficulty, self.score)

class Enemy:
    def __init__(self, level: int, difficulty: str) -> None:
        self.lives = (level + 1) * PLAYER_LIVES
        self.level = level
        self.difficulty = difficulty

    def select_attack(self) -> str:
        return random.choice(list(ALLOWED_ATTACKS.values()))

    def decrease_lives(self) -> None:
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown("Вы победили врага.")

    def is_alive(self) -> bool:
        return self.lives > 0
