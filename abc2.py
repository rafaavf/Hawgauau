inp = []
for i in range (3):
    inp.append(int(input()))

carim = []
fig = []
for i in range(inp[1]):
    carim.append(int(input()))
for i in range(inp[2]):
    fig.append(int(input()))

def ver_carim(c,f):
    r = 0
    for i in c:
        if i not in f:
            r += 1
        else:
            pass
    return r

print(ver_carim(carim, fig))
