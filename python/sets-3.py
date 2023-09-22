N = int(input())
set_N = set(map(int, input().split()))
M = int(input())
for i in range(M):
    n = set_N
    task = list(input().split())
    task_number = set(map(int, input().split()))
    len(task_number) == int(task[1])
    if task[0] == 'intersection_update':
        n.intersection_update(task_number)
    elif task[0] == 'update':
        n.update(task_number)
    elif task[0] == 'difference_update':
        n.difference_update(task_number)
    elif task[0] == 'symmetric_difference_update':
        n.symmetric_difference_update(task_number)
    else:
        print('Unknown command')

print(sum(n))