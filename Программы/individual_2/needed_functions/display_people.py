#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def display_people(people):
    """Отобразить список людей."""

    if people:
        # Заголовок таблицы.
        line = "├-{}-⫟-{}⫟-{}-⫟-{}-⫟-{}-┤".format(
            "-" * 5, "-" * 25, "-" * 25, "-" * 25, "-" * 18)
        print(line)
        print("| {:^5} | {:^24} | {:^25} | {:^25} | {:^18} |".format(
            "№", "Name", "Surname", "Telephone", "Birthday"))
        print(line)
        for number, human in enumerate(people, 1):
            print("| {:^5} | {:<24} | {:<25} | {:<25} | {:<18} |".format(number, human.get(
                "name", ""), human.get("surname", ""),
                human.get("telephone", ""), human.get("birthday", "")))
        print(line)
    else:
        print("There are no people in list!")
