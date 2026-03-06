Repetition = int(input())
num_list = list(map(int, input().split()))

count = num_list[0]
s_count = num_list[0]

for i in num_list:
    
    if count < i:
        count = i

    if s_count > i:
        s_count = i


print(f"{s_count} {count}")