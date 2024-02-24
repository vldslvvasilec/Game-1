

# from random import randint

# def play_game():
#     choices = ["rock", "paper", "scissors"]
#
#     user_choice = input("Choose: rock, paper, or scissors: ").lower()
#     computer_choice = random.choice(choices)
#
#     print(f"You chose {user_choice}.")
#     print(f"Computer chose {computer_choice}.")
#
#     if user_choice == computer_choice:
#         return "It's a tie!"
#     elif (user_choice == "rock" and computer_choice == "scissors") or \
#          (user_choice == "paper" and computer_choice == "rock") or \
#          (user_choice == "scissors" and computer_choice == "paper"):
#         return "You win!"
#     else:
#         return "Computer wins!"
#
# result = play_game()
# print(result)

# class Enemy:
#     def enemy_value(self):
#         return randint(1, 3)
#
# class UserGame:
#     def user_input(self):
#         user_input_list = ["камень", "ножницы", "бумага"]
#         user_selection = input("Ваш ход. Выберите: 1 - Камень, 2 - Ножницы, 3 - Бумага: ")
#         if user_selection == range(1, 3) or user_selection.lower() == user_input_list:
#             print(user_selection)
#
# class StartMenu:
#     def start_menu(self):
#         start_menu_input = input("Выберите действие (1 - Играть, 2 - Посмотреть результат, 3 - Выйти): ").lower()
#         if start_menu_input == "1" or start_menu_input == "играть":
#             user_game = UserGame()
#             user_game.user_input()
#             print("play")
#         elif start_menu_input == "2" or start_menu_input == "посмотреть результат":
#             print("Посмотреть результат")
#         elif start_menu_input == "3" or start_menu_input == "выйти":
#             print("Вы вышли из игры, возвращайтесь снова")
#             return "game exit"
#
#
#
# while True:
#     start_menu = StartMenu()
#     start_menu_values = start_menu.start_menu()
#     if start_menu_values == "game exit":
#         break