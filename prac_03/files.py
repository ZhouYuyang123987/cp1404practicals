name = input("Enter your name：")
with open("name.txt", "w") as file:
    file.write(name)
    file.close()

with open("name.txt", "r") as file:
    name = file.read()
    file.close()
    print(f"Hi {name}!")


with open("numbers.txt", "r") as file:
    number_1 = int(file.readline())
    number_2 = int(file.readline())
    print(number_1 + number_2)


total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line)
print(total)