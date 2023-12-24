#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def select_people(people, month):
    """Выбрать людей, родившихся в требуемом месяце."""

    born = []
    for human in people:
        human_month = human.get("birthday").split(".")
        if month == int(human_month[1]):
            born.append(human)
    return born
