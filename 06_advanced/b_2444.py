# 숫자 입력받기
user = int(input())

# 각 함수 숫자 지정
total_stars = 1
stars = 1
add_stars = 0

# 띄어쓰기 먼저 지정, 들어 온 값의 -1로 시작

# 반복문으로 띄어쓰기 하나씩 빼기
for i in range(user-1 , -1,  -1):

    # 띄어쓰기 지정
    space = " " * i
    
    # 출력
    print(space + ("*" * int(total_stars)))

    # 마지막 줄(i=0)에서는 별 증가 방지 (줄어들때를 위해)
    if i != 0:

        # 추가될 별 지정
        add_stars += 2

        # 다음에 출력할 별들 +2씩
        total_stars = stars + add_stars    


for _ in range(1, user):

    # 별 숫자 2개 빼면서 시작
    total_stars -= 2
    
    # 띄어쓰기 저장
    space = " " * _

    # 출력
    print(space+ ("*" * int(total_stars)))

# 깔끔한 정답 -------
# n = int(input())

# # 위쪽
# for i in range(n):
#     space = " " * (n - i - 1)
#     stars = "*" * (2 * i + 1)
#     print(space + stars)

# # 아래쪽
# for i in range(n - 2, -1, -1):
#     space = " " * (n - i - 1)
#     stars = "*" * (2 * i + 1)
#     print(space + stars)