#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Расставьте знаки операций "плюс", "минус", "умножение" и скобки
# между числами "1 2 3 4 5" так, что бы получилось число "25".
#
# Использовать нужно только указанные знаки операций, но не обязательно все перечесленные.
# Порядок чисел нужно сохранить.
import itertools


# Пример для чисел "1 2 3" и "9"
def task_3():
    result = (1 + 2) * 3
    print(result)

# TODO написать формулу для 1 2 3 4 5 и вывести значение на консоль



    numbers = [1, 2, 3, 4, 5]

    operators = ['+', '-', '*']
    result_ope = 25

    combinations = itertools.product(operators, repeat=(len(numbers) - 1))

    def generate_expression(numbers, ops):
        expression = f"{numbers[0]} {ops[0]} {numbers[1]} {ops[1]} {numbers[2]} {ops[2]} {numbers[3]} {ops[3]} {numbers[4]}"
        return expression


    for ops in combinations:
        expression = generate_expression(numbers, ops)
        try:
            result = eval(expression)
            if result == result_ope:
                print(f"Expression: {expression} = {result}")
        except:
            continue

        expressions_with_brackets = [
            f"({numbers[0]} {ops[0]} {numbers[1]}) {ops[1]} {numbers[2]} {ops[2]} {numbers[3]} {ops[3]} {numbers[4]}",
            f"{numbers[0]} {ops[0]} ({numbers[1]} {ops[1]} {numbers[2]}) {ops[2]} {numbers[3]} {ops[3]} {numbers[4]}",
            f"{numbers[0]} {ops[0]} {numbers[1]} {ops[1]} ({numbers[2]} {ops[2]} {numbers[3]}) {ops[3]} {numbers[4]}",
            f"{numbers[0]} {ops[0]} {numbers[1]} {ops[1]} {numbers[2]} {ops[2]} ({numbers[3]} {ops[3]} {numbers[4]})",
            f"({numbers[0]} {ops[0]} {numbers[1]} {ops[1]} {numbers[2]}) {ops[2]} ({numbers[3]} {ops[3]} {numbers[4]})"
        ]

        for expr in expressions_with_brackets:
            try:
                result = eval(expr)
                if result == result_ope:
                    print(f"Expression: {expr} = {result}")
            except:
                continue