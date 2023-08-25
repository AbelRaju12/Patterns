n  = int(input())
student_marks = {}
for i in range(n):
    name, *line = input().split()
    # >>> a, b, *rest = range(5)
    # >>> a, b, rest
    # (0, 1, [2,3,4])
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
if query_name in student_marks.keys():
    l = student_marks[query_name]
    average = sum(l) / len(l)
print(format(average, ".2f"))
    