list =[]
mark = []
for i in range(int(input())):
    name = input()
    score = float(input())
    list.append([name, score])
    mark.append(score)
mark.sort()
second_min = 0
minim = mark[0]
list.sort()
for i in mark:
    if i != minim:
        second_min = i
        break
for i in list:
    if i[1] == second_min:
        print(i[0])
