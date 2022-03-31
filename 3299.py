N = input()
newArr = list(N)
unlucky = False
for i in range(len(newArr) - 1):
    if int(newArr[i]) == 1:
        if int(newArr[i + 1]) == 3:
            unlucky = True
            break


print("{} es de Mala Suerte".format(N)) if unlucky else print(
    "{} NO  es de Mala Suerte".format(N)
)
