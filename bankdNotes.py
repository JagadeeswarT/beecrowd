value = float(input())
print("NOTAS:")
print("{} nota(s) de R$ 100.00".format(int(value / 100)))
rem = value % 100
print("{} nota(s) de R$ 50.00".format(int(rem / 50)))
rem = rem % 50
print("{} nota(s) de R$ 20.00".format(int(rem / 20)))
rem = rem % 20
print("{} nota(s) de R$ 10.00".format(int(rem / 10)))
rem = rem % 10
print("{} nota(s) de R$ 5.00".format(int(rem / 5)))
rem = rem % 5
print("{} nota(s) de R$ 2.00".format(int(rem / 2)))
rem = rem % 2
print("MOEDAS:")
print("{} moeda(s) de R$ 1.00".format(int(rem / 1)))
rem = rem % 1
print("{} moeda(s) de R$ 0.50".format(int(rem / 0.5)))
rem = rem % 0.5
print("{} moeda(s) de R$ 0.25".format(int(rem / 0.25)))
rem = rem % 0.25
print("{} moeda(s) de R$ 0.10".format(int(rem / 0.10)))
rem = rem % 0.10
print("{} moeda(s) de R$ 0.05".format(int(rem / 0.05)))
rem = rem % 0.05
print("{} moeda(s) de R$ 0.01".format(int(rem / 0.01)))
