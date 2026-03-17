# 첫번째 열 숫자 받기
first_n = int(input())

# 첫번째에 입력받은 숫자만큼 반복하기 
for i in range(first_n):
    s_n, s_w = input().split()

# 반복 입력받은 문자를 첫번째 숫자랑 곱하기
    for _ in s_w:
        print(_ * int(s_n), end="")
    # 줄 띄우기
    print()
