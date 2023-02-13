money = float(input("Введите сумму,которую планируете положить под проценты: "))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
per_cent_val = list(per_cent.values())
deposit = [i/100*money for i in per_cent_val]
print("deposit =", list(map(round, deposit)))
print("Максимальная сумма, которую вы можете заработать - ", max(list(map(round, deposit))))