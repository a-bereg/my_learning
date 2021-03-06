# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
month = 1
total_expenses = expenses
while month < 10:
    print('Месяц', month, ':', total_expenses)
    expenses = expenses + expenses * 0.03
    total_expenses += expenses
    month += 1

print('Все расходы:', round(total_expenses, 2))
parents_money = total_expenses - educational_grant * 10
print('Студенту надо попросить', round(parents_money, 2), 'рублей')
