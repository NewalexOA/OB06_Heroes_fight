import random

# Класс Hero
class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        # Добавляем случайное отклонение силы атаки в пределах ±10%
        attack_modifier = random.uniform(0.9, 1.1)  # Генерируем случайное число от 0.9 до 1.1
        actual_attack_power = int(self.attack_power * attack_modifier)  # Округляем силу атаки до целого числа

        # Герой атакует другого героя и отнимает здоровье с учетом случайного отклонения
        other.health -= actual_attack_power
        print(f"{self.name} атакует {other.name} и наносит {actual_attack_power} урона!")

    def is_alive(self):
        # Проверка на жизнь героя
        return self.health > 0

# Класс Game
class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("Начало игры!")
        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока
            self.player_turn()
            if not self.computer.is_alive():
                print(f"{self.player.name} победил!")
                break

            # Ход компьютера
            self.computer_turn()
            if not self.player.is_alive():
                print(f"{self.computer.name} победил!")
                break

    def player_turn(self):
        # Атака игрока
        self.player.attack(self.computer)
        print(f"У {self.computer.name} осталось {self.computer.health} здоровья.\n")

    def computer_turn(self):
        # Атака компьютера
        self.computer.attack(self.player)
        print(f"У {self.player.name} осталось {self.player.health} здоровья.\n")


# Запуск игры
if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()
