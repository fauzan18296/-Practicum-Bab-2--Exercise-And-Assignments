average = input("Masukan bilangan rata-rata: ")
average_numbers = list(map(int, average.split()))
averange_result = 0
for j in range(0, len(average_numbers)):
          averange_result = averange_result + average_numbers[j] / len(average_numbers)
my_averange_result = f"Angka yang di rata-rata:\n{average_numbers}" f"\nRata-rata dari {len(average_numbers)} bilangan adalah {averange_result:.2f}"
print(my_averange_result)
