students = []
last = []
# 1부터 30까지 출석 번호를 만든다
all_s = list(range(1, 31))
# 반복문으로
# 28명의 출석번호를 입력받는다
for i in range(28):

    n = int(input())
    students.append(n)


for t in all_s:
    if t not in students:

        last.append(t)


# 다만 없는 숫자는 작은 순서대로 출력한다
if last[0] <  last[1]:
    print(last[0])
    print(last[1])
else:
    print(last[1])
    print(last[0])