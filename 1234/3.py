import random

print("Правила гри: ")
print("Я загадую число")
print("А ви намагаєтесь вгадати.")

random_number = random.randint(1, 100)

count = 0

number=101

while not  number == random_number:
    number = int(input("Вгадайте число від 1 до 100 :) \n"))
    count += 1

    if number < random_number:
        print("Замало! Спробуйте ще!")
    else:
        print("Забагато! Спробуйте ще!")

print("Вітаю з перемогою!")
print(f"Загадане число - {random_number}.")
print(f"Ви зробили {count} спроб.")


