from Task.task_1 import task_1
from Task.task_2 import task_2
from Task.task_3 import task_3
from Task.task_4 import task_4
from Task.task_5 import task_5
from Task.task_6 import task_6
from Task.task_7 import task_7
from Task.task_8 import task_8
from Task.task_9 import task_9
from Task.task_10 import task_10
from Task.task_11 import task_11

class Terminal:
    def __init__(self):
        self.commands = {
            "-help": self.show_help,
            "-exit": self.exit_terminal,
            "-task1": task_1,
            "-task2": task_2,
            "-task3": task_3,
            "-task4": task_4,
            "-task5": task_5,
            "-task6": task_6,
            "-task7": task_7,
            "-task8": task_8,
            "-task9": task_9,
            "-task10": task_10,
            "-task11": task_11,
        }



    def start(self):
        print("Добро пожаловать в терминал! Введите '-help' для получения списка команд.")
        while True:
            command = input("> ")
            self.execute_command(command)

    def execute_command(self, command):
        command = command.strip().lower()
        if command in self.commands:
            self.commands[command]()
        else:
            print(f"Неизвестная команда: {command}. Введите '-help' для получения списка доступных команд.")

    def show_help(self):
        print("Доступные команды:")
        print("  -help - показать список доступных команд")
        print("  -exit - выйти из терминала")
        print("  -task<1-10> - выводит необходимое задание")


    def exit_terminal(self):
        print("Выход из терминала. Всего доброго!")
        exit()
