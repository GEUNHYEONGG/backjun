# 사용자에게 영어 입력받기
user_input = list(input())

# 앞 뒤를 바꿔도 같으면 1 출력
if user_input[::] == user_input[::-1]:
    print(1)

# 아니면 0 출력
else:
    print(0)