year = int(input("Masukkan tahun (1800 - 2020): "))

if year >= 1800 and year <= 2020:
          leap_year = f"{year} adalah tahun kabisat." if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) else f"{year} bukan tahun kabisat."
          print(leap_year)
else:
          print("Tahun yang anda tidak boleh lebih dari 1800 dan 2020!!.")