# 사용자에게 단어 갯수 입력 받기
word_num = int(input())

# 단어 갯수 지정 (그룹 단어가 아닐시 -1씩 차감용)
num = word_num

# 입력 받은 갯수만큼 반복
for _ in range(word_num):

# 단어 입력 받기
    word = input()

    # 인덱스에 넣기 위한 반복
    for i in range(0, len(word)-1):

    # 만약 현재 단어랑 다음 단어가 중복이면 상관없으니 패스
        if word[i] == word[i + 1]:
            pass

    # 만약 다음 단어를 건너 같은 단어가 있으면 그룹 단어가 아니니 count -1 
        elif word[i] in word[i + 1 : ]:
            num -= 1
            break

# 총 카운트 출력
print(num)