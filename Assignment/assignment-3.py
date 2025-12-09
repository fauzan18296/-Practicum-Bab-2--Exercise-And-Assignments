N = int(input("Masukan nilai N: "))
factorial_result = 1
for i in range(1, N + 1):
          factorial_result *= i
print(f"Hasil dari {N} faktorial adalah {factorial_result}")