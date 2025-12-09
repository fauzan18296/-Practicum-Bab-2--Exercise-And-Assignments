number_series_begin = int(input("Masukan angka awal deret bilangan: "))
number_series_end = int(input("Masukan angka akhir deret bilangan: "))
numbers_series = []
numbers = []
number_series = ""
for i in range(number_series_begin, number_series_end + 1):
                    numbers_series.append(i)
for number in numbers_series:
          if number % 2 == 0 and number % 4 != 0:
                    numbers.append(number)
          else:
                    number_series = f"Jumlah bilangan genap dari {number_series_begin} sampai {number_series_end} yang bukan kelipatan 4 adalah {len(numbers)}"
result_number_series = " ".join(list(map(str,numbers)))
print(result_number_series)
print(number_series)