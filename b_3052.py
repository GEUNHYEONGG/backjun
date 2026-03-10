# 입력받을 자연수 10개
all = []
new_list = []
for _ in range(10):
    input_list = input()
    

# 입력 받은 수를 42로 나눈 나머지를 구한다.
    all_list = (int(input_list)) % 42

# 새로운 리스트에 나눈 나머지를 저장한다.
    all.append(all_list)

# 새로운 리스트에서 중복된 값을 제거한다. 
    if all[_] not in new_list:
        new_list.append(all[_])

# 중복이 제거된 리스트의 길이를 출력한다.
print(len(new_list))
