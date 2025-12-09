step = (input("Masukan elemen array: "))
array = list(map(int, step.split()))
k = int(input("Masukan nilai k: "))

k = k % len(array)
rotated = array[-k:] + array[:-k]
print(f"Elemen array:{array}")
print(f"Nilai k: {k}")
print(f"Hasil rotasi: {rotated}")
