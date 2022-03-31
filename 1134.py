alcohol = 0
gasoline = 0
diesel = 0

while True:
    N = int(input())
    if N == 1:
        alcohol += 1
    elif N == 2:
        gasoline += 1
    elif N == 3:
        diesel += 1
    elif N == 4:
        break
    else:
        pass
print("MUITO OBRIGADO")
print("Alcool: {}".format(alcohol))
print(f"Gasolina: {gasoline}")
print(f"Diesel: {diesel}")
