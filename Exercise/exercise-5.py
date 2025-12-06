numbers = [4, 5, 6, 4, 4, 5]
result = {}

# TODO: Cara 1 yang sederhana
for i in range(0, len(numbers)):
          # ? result[numbers[i]] -> mengakses key dari dictionary simpel nya variabel result mengakses elemen dari list numbers pada index i untuk dijadikan key
          # ? result.get(numbers[i], 0) -> mengakses value dari dictionary, jika key tidak ada maka mengembalikan nilai 0 jika key ada maka mengembalikan value dari key tersebut
          # ? + 1 -> menambahkan nilai 1 pada value dari key tersebut
          result[numbers[i]] = result.get(numbers[i], 0) + 1 

# TODO: Cara 2 yang lebih panjang (Logic nya lebih eksplisit)
# for i in range (0, len(numbers)):
#           if numbers[i] not in result:
#                     result[numbers[i]] = 1
#           else:
#                     result[numbers[i]] += 1

for key, value in result.items():
          print(f"Angka {key} muncul sebanyak {value} kali.")