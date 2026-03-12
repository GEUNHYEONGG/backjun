total = 0
# 과목 개수 입력받기
Subject = int(input())
# 점수 입력 받기
Score = list(map(int, input().split()))
# 입력 받은 점수 중에 제일 큰 숫자 선택
big_n = max(Score)
# 선택한 숫자를 나머지 수랑 나눠서 *100하기
for i in range(Subject):
    a = Score[i] / big_n * 100
# 곱한 수를 더해서 과목 수 만큼 나누기
    total += a
    last = total / Subject
# 출력
print(last)