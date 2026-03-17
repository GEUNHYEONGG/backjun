# 알파벳을 지정해준다
alpha = "abcdefghijklmnopqrstuvwxyz"
# 입력 받는다
your = input()


# 알바펫을 하나씩 반복문으로 넣는다
for i in alpha:

# -1을 출력하기위한 불린형
    found = False    
    
    # 입력받은 값도 하나씩 반복한다
    for _ in range(len(your)):
        # 만약 입력받은 값이 알파벳에 있으면 처음 등장한 위치를 출력한다
        if your[_] == i:
            print(_, end=" ")
            found = True
            # 출력되면 탈출
            break

    # 만약 못 찾으면 -1 출력
    if found == False:
        print(-1, end=" ")