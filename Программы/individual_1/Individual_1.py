#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import calculation


"""Внутренняя функция увеличивает полученное значение на 3."""

if __name__ == '__main__':
    cnt = calculation.calculaion()
    k = int(input("Good day! Please, enter value: "))
    print("According to our calculations, answer is - ", cnt(k))
