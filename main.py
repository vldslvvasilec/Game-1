from Game.game import Game
from Game.score import ScoreHandler
from Game.models import Player

from Game.settings import MODES


def main() -> None:
    """Функция для запуска игры."""
    while True:
        print("1. Начать игру\n2. Показать очки\n3. Выйти")
        choice = input("Выберите опцию: ")

        if choice == '1':
            play_game()
        elif choice == '2':
            show_scores()
        elif choice == '3':
            exit_game()
        else:
            print("Неверный выбор. Пожалуйста, введите 1, 2 или 3.")


def play_game() -> None:
    """Функция для начала игры."""
    player_name = input("Введите ваше имя: ")
    print("Выберите уровень сложности:")
    for key, value in MODES.items():
        print(f"{key}. {value}")

    difficulty_choice = input("Выберите уровень сложности (1 или 2): ")
    if difficulty_choice not in MODES:
        print("Неверный выбор. Игра заканчивается.")
        return

    difficulty = MODES[difficulty_choice]
    player = create_player(player_name, difficulty)
    game = Game(player, difficulty)
    game.play()


def create_player(name: str, difficulty: str) -> Player:
    """
    Функция для создания объекта игрока.

    :param name: Имя игрока
    :param difficulty: Уровень сложности (Normal или Hard)

    :return: Объект игрока
    """
    return Player(name, difficulty)


def show_scores() -> None:
    """Функция для отображения записей об игроках."""
    score_handler = ScoreHandler()
    score_handler.display()


def exit_game() -> None:
    """Функция для выхода из игры."""
    print("Выход из игры. До свидания!")
    exit()


if __name__ == "__main__":
    main()
