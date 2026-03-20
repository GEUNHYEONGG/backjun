# # 원래 있어야 하는 체스 말 갯수
chess = [1, 1, 2, 2, 2, 8]
need_chess = []
# # 킹 퀸 룩 비숍 나이트 폰 순으로 갯수 입력받기
chess_input = input().split()

# 원래 있어야 하는 갯수랑 비교
for i in range(len(chess)):

    #빼서 필요한 수 확인하고 추가
        need_chess.append(int(chess[i]) - int(chess_input[i]))

# 총 값 출력
print(*need_chess)


# 백준 정답------
# need_chess = [int(c) - int(ci) for c, ci in zip(chess, chess_input)]
# print(need_chess)