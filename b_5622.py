# 알파벳별 숫자를 지정 해주기 위한 리스트 생성
alpha = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
point = 0
# 받은 영어 갯수만큼 반복
in_call = input()
for i in in_call:

# 반복문으로 리스트 안에 값들 넣기
    for _ in alpha:

# 입력 받은 영어가 리스트 안에 있으면
        if i in _ :

        # 리스트 인덱스 위치에서 +3
            point += alpha.index(_) + 3


# 출력
print(point)