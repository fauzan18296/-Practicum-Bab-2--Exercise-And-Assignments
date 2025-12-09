print("Pattern 1")
for i in range(1, 11):

    print(" " * (10 - i) * 2, end="")

    number = 1
    for j in range(1, 2*i):
        print(number % 10, end=" ")
        number += 1

    print()

print("\nPattern 2")
for i in range(10, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

print("\nPattern 3")
for i in range(1, 11):
    for j in range(i):
        print(i, end=" ")
    print()

print("\nPattern 4")
for i in range(10, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()