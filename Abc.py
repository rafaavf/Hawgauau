a = int(input())
notas = []

for i in range(a):
    notas.append(int(input()))

def count_notas(n):
    x = []
    y = []

    for i in range (len(n)):
        x.append([i, n.count(n[i]), n[i]])


    for i in x:
        if y == []:
            y.append(i)
        elif i[1] > y[0][1]:
            y[0] = i
        elif i[1] == y[0][1] and i[2] > y[0][2]:
            y[0] = i
        else:
            pass

    return n[y[0][0]]

count_notas(notas)
