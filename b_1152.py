# 입력 받을 문자형을 리스트로 만든다
first_list = list(input().split())

# 횟수 변수를 미리 만든다
count = 0

# 반복문을 사용해서 리스트 안에 있는 값들을 넣는다
for i in first_list:

    # 한번씩 반복할때마다 1씩 더한다
    count += 1


# 총 단어 횟수를 출력한다
print(count)
