import random
select_number = random.randint(1, 101)

print("1から100までの数を当てよう！")

while True:
    print("1から100までの数を入力してください。")
    guess = int(input())
    
    if guess < select_number:
        print("あなたの推定値は小さいです！")
    elif guess > select_number:
        print("あなたの推定値は大きいです！")
    else:
        break

if guess == select_number:
    print("おめでとう！")
