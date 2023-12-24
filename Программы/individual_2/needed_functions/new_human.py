#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def new_human():
    """Запросить данные о человеке."""

    name = input("Name - ")
    surname = input("Surname - ")
    telephone = input("Telephone number - ")
    happy_birthday = input("Date of birth (Day.Month.Year) - ")
    # Создать словарь.
    return {
        "name": name,
        "surname": surname,
        "telephone": telephone,
        "birthday": happy_birthday
    }
