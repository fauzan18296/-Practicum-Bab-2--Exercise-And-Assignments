numbers = [12, 45, 2, 10, 7]
max = numbers[0]
min = numbers[0]

for i in numbers:
          if i > max:
                    max = i
          
          if i < min:
                    min = i
print(f"Angka terbesar: {max}")
print(f"Angka terkecil: {min}")