from random import randint

# 중복 허용 안됨
# 0이상의 자연수만 허용됨

print("*" * 30)
print("⭐ Welcome to Cows & Bulls ⭐")
print("*" * 30)

# 컴퓨터가 만든 3자리 랜덤 숫자
target_num = []

while len(target_num) < 3:
    random_num = randint(1, 9)
    if str(random_num) in target_num:
        continue
    else:
        target_num.append(str(random_num))
print(target_num)
strike = 0
# 사용자에게 받는 3자리 숫자
while strike != 3:
    user_num = input("👽 세자리 숫자를 입력하세요 ➡  ")

    if user_num.isdecimal() == True and "0" not in user_num and len(user_num) == 3:
        user_num = list(user_num)
    else:
        print(" 🖐 다시 입력해주세요")
        continue
    print(user_num)
    if len(set(user_num)) != 3:
        print(" 🖐 다시 입력해주세요")
        continue

    strike = 0
    ball = 0
    out = 3
    for i, target in enumerate(target_num):
        for j, user in enumerate(user_num):
            if target == user and i == j:
                strike += 1
                out = out - 1
                break
            elif target == user and i != j:
                ball += 1
                out = out - 1
                break
    print(f"{strike} strike , {ball} ball , {out} out")

print("*" * 30)
print(" " * 8 + "🤘 You Win 🤘")
print("*" * 30)
