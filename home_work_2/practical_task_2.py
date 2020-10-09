pull_list = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    num = input()
    pull_list.append(num)

print(f'Got a list or elements:, {pull_list}')

if len(pull_list) % 2 == 0:
    i = 0
    while i < len(pull_list):
        sin_elem = pull_list[i]
        pull_list[i] = pull_list[i+1]
        pull_list[i+1] = sin_elem
        i += 2
else:
    i = 0
    while i < len(pull_list) - 1:
        sin_elem = pull_list[i]
        pull_list[i] = pull_list[i + 1]
        pull_list[i + 1] = sin_elem
        i += 2

print(f'Changed nearby elements: {pull_list}')