# 상근이에게 2개의 숫자를 입력받는다
num_1, num_2 = input().split()


# 입력받은 값의 맨 앞, 뒤 자리를 바꾼다
# 인덱스를 자리값을 이용
num_1 = num_1[::-1]
num_2 = num_2[::-1]

# 바꾼 숫자를 비교한다
if int(num_1) > int(num_2):
    print(num_1)

# 비교 한 뒤 더 큰 숫자를 출력한다
else:
    print(num_2)