x = input()
y = input()
z = input()

v = "vertebrado"
a = "ave"
m = "mamifero"
i = "invertebrado"
k = "inseto"
m = "anelideo"
if x == v:
    print("yes")
if y == m:
    print("yes")
else:
    print("no")
if z == "onivoro":
    print("yes")
if x == v and y == a and z == "carnivoro":
    animal = "aguia"
elif x == v and y == a and z == "onivoro":
    animal = "pomboa"
elif x == v and y == m and z == "onivoro":
    animal = "homem"
elif x == v and y == m and z == "herbivoro":
    animal = "vaca"
elif x == i and y == k and z == "hematofago":
    print("pulga")
elif x == i and y == k and z == "herbivoro":
    print("lagarta")
elif x == i and y == m and z == "hematofago":
    print("sanguessuga")
elif x == i and y == m and z == "onivoro":
    print("minhoca")

# print(animal)
