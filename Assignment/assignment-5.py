amount_pair_number = int(input("Masukan jumlah angka pasangan: "))
pair = 0
result = None
while pair < amount_pair_number:
          pair_number = input("Masukan angka pasangan: ")
          pair_numbers = list(map(int, pair_number.split()))
          print(f"Elemen: {pair_numbers}")
          print("\n")
          for i in range(0, len(pair_numbers)):
                    for j in range(i + 1, len(pair_numbers)):
                              if pair_numbers[i] + pair_numbers[j] == amount_pair_number:
                                        result = f"({pair_numbers[i]}, {pair_numbers[j]})"
                                        print(f"Output: {result}")
          continue_option = input("Apakah masih ingin melanjutkan pencocokan pasangan angka? (y/n): ") if len(pair_numbers) == amount_pair_number else pair + 1
          if continue_option == 'n':
                    print("Terimakasih telah menggunakan program sederhana untuk pencocokan pasangan angka.")
                    break                 