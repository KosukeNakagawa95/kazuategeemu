import random
select_number = random.randint(1, 101)

print("1から100までの数を当てよう！")
guess = int(input())

while True:
    if guess < select_number:
        print("あなたの推定値は小さいです！")
    elif guess > select_number:
        print("あなたの推定値は大きいです！")
    else:
        break

if guess == select_number:
    print("おめでとう！")
