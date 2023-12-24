#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from needed_functions import *
import sys


def main():
    """Главная функция программы."""

    print("Good day!, please, enter your command: ('help' will list all of them)")
    people = []
    while True:
        command = input(">>> ").lower()
        if command == "exit":
            break
        elif command == "add":
            human = new_human.new_human()
            people.append(human)
            # Сортировка идёт по фамилиям. Если фамилии одинаковые, то рассматриваются имена
            people.sort(key=lambda person: (person.get(
                "surname", ""), person.get("name", "")))
        elif command == "list":
            display_people.display_people(people)
        elif command.startswith("select "):
            which_month = command.split(" ", maxsplit=1)
            user_month = int(which_month[1])
            same_month = select_people.select_people(people, user_month)
            display_people.display_people(same_month)
        elif command == "help":
            list_commands.list_commands()
        else:
            print(f"Unknown command! - {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
