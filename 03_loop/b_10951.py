# 두 변수 입력받기
while True:
    try:
        num1, num2 = map(int,input().split())

    # 더하기
        print(num1+num2)
        # 입력 없으면 끝
    except:
        break
