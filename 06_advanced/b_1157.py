# 값을 저장하기 위한 변수 지정
plus = 0
same = False
max_bar = ""
# 사용자로부터 입력값 받기
user = input()
# 대소문자 통일하기
user = user.upper()

# 중복된 문자들 없애기
    # 반복문으로 문자들 하나씩 받아서 갯수 새기
for i in set(user):
    count_num = user.count(i)

    # 갯수 비교
    if count_num > plus:
    # 다른 함수에 갯수 저장
        plus = count_num
        max_bar = i
        same = False

    elif count_num == plus:
        same = True

# 만약 중복되면 ? 출력
if same:
    print("?")
# 아니면 제일 많은 글자 출력
else:
    print(max_bar)