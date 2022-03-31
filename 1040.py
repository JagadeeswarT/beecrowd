N1, N2, N3, N4 = map(float, input().split())
A = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 10
print(f"Media: {A:.1f}")

if A >= 7:
    print("Aluno aprovado.")
elif A < 5:
    print("Aluno reprovado.")
elif A >= 5 and A <= 6.9:
    print("Aluno em exame.")
    N = float(input())
    print(f"Nota do exame: {N:.1f}")
    N = (N + A) / 2
    if N >= 5.0:
        print("Aluno aprovado.")
        print(f"Media final: {N:.1f}")
    else:
        print("Aluno reprovado.")
        print(f"Media final: {N:.1f}")
