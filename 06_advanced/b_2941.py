# 크로아티아 알파벳
alpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]


# 사용자에게 단어 입력 받기
word = input()

# 반복문으로 크로아티아 알파벳 하나씩 넣기
for i in alpha:

# 하나의 문자로 변환
    word = word.replace(i, "*")


# 총 갯수 출력
print(len(word))