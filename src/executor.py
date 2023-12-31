"""
This module contains a class for executing user commands.
"""

import os
import datetime


class Executor:
    """Executes the user commands."""

    def __init__(self, config: dict) -> None:
        self._config = config
        self._commands = {
            "e": self._exit,
            "exit": self._exit,
            "c": self._clear,
            "clear": self._clear,
            "h": self._help,
            "help": self._help,
            "w": self._week,
            "week": self._week,
            "l": self._lessons,
            "lessons": self._lessons,
            "b": self._bells,
            "bells": self._bells,
            "t": self._time,
            "time": self._time
        }

        print(
            "Console Ficus\n"
            'Напишите "h" или "help" для получения дополнительной информации.'
        )

        self.exec(self._config["autoexec"])

    def exec(self, commands: str) -> None:
        """Executes commands."""
        for command in commands.split("&&"):
            command = command.strip()

            if command:
                if command in self._commands:
                    self._commands[command]()

                else:
                    print(f"{command}: команда не найдена")
                    break

    def _exit(self) -> None:
        """Exits the application."""
        raise SystemExit

    def _clear(self) -> None:
        """Clears the console."""
        if os.name == "nt":  # Windows.
            os.system("cls")

        else:  # Non Windows.
            os.system("clear")

    def _help(self) -> None:
        """Prints an application manual."""
        print(
            '&& - логическое "и" для объединения команд\n'
            "e или exit - выйти\n"
            "c или clear - очистить консоль\n"
            "h или help - вывести это руководство\n"
            "w или week - вывести тип текущей недели\n"
            "l или lessons - вывести расписание пар\n"
            "b или bells - вывести расписание звонков\n"
            "t или time - вывести время до начала или конца текущей пары"
        )

    def _week(self) -> None:
        """Prints the current week type."""
        if datetime.datetime.today().isocalendar().week % 2 == 0:
            print("Знаменатель")

        else:
            print("Числитель")

    def _lessons(self) -> None:
        """Prints the lessons schedule."""
        days = iter(
            ("Понедельник:", "\nВторник:", "\nСреда:",
             "\nЧетверг:", "\nПятница:", "\nСуббота:")
        )

        for day_info in self._config["lessons"].values():
            print(next(days))

            for lesson_num, lesson_info in day_info.items():
                print(f"{lesson_num}: {lesson_info}")

    def _bells(self) -> None:
        """Prints the bells schedule."""
        print("Основное:")

        for bell_num, bell_info in self._config["bells"]["main"].items():
            print(f"{bell_num}: {bell_info['1']} | {bell_info['2']}")

        print("\nСубботнее:")

        for bell_num, bell_info in self._config["bells"]["sat"].items():
            print(f"{bell_num}: {bell_info}")

    def _time(self) -> None:
        """Prints the time before the start or end of current lesson."""
        current_datetime = datetime.datetime.today()
        current_weekday = current_datetime.weekday()

        if current_weekday == 6:  # Sunday.
            print("Сегодня не учебный день")
            return

        current_time = current_datetime.time()
        current_td = datetime.timedelta(
            seconds=current_time.second,
            minutes=current_time.minute,
            hours=current_time.hour
        )

        if current_weekday < 5:  # Weekdays.
            for bell_num, bell_info in self._config["bells"]["main"].items():
                bell_start_td = datetime.timedelta(
                    hours=int(bell_info["1"][:2]),
                    minutes=int(bell_info["1"][3:5])
                )

                if current_td < bell_start_td:  # Non lessons time.
                    print(
                        f"Начало {bell_num} пары через "
                        f"{bell_start_td - current_td}"
                    )
                    return

                bell_end_td = datetime.timedelta(
                    hours=int(bell_info["2"][6:8]),
                    minutes=int(bell_info["2"][9:])
                )

                if current_td < bell_end_td:  # Lessons time.
                    print(
                        f"Конец {bell_num} пары через "
                        f"{bell_end_td - current_td}"
                    )

                    for bell_half_num, bell_half_info in bell_info.items():
                        bell_half_start_td = datetime.timedelta(
                            hours=int(bell_half_info[:2]),
                            minutes=int(bell_half_info[3:5])
                        )

                        if current_td < bell_half_start_td:
                            print(
                                f"Начало {bell_half_num} половины через "
                                f"{bell_half_start_td - current_td}"
                            )
                            return

                        bell_half_end_td = datetime.timedelta(
                            hours=int(bell_half_info[6:8]),
                            minutes=int(bell_half_info[9:])
                        )

                        if current_td < bell_half_end_td < bell_end_td:
                            print(
                                f"Конец {bell_half_num} половины через "
                                f"{bell_half_end_td - current_td}"
                            )
                            return

                    return

        else:  # Saturday.
            for bell_num, bell_info in self._config["bells"]["sat"].items():
                bell_start_td = datetime.timedelta(
                    hours=int(bell_info[:2]),
                    minutes=int(bell_info[3:5])
                )

                if current_td < bell_start_td:
                    print(
                        f"Начало {bell_num} пары через "
                        f"{bell_start_td - current_td}"
                    )
                    return

                bell_end_td = datetime.timedelta(
                    hours=int(bell_info[6:8]),
                    minutes=int(bell_info[9:])
                )

                if current_td < bell_end_td:
                    print(
                        f"Конец {bell_num} пары через "
                        f"{bell_end_td - current_td}"
                    )
                    return

        print("Пары закончились")
