l = []
for line in open('keys.txt', 'r'):
    l.append(line.strip('\n'))

a = [0,1,2,3,6,7,8,9]
b = dict()
for num in a:
    ll = []
    for code in l:
        for i in range(len(str(code))):
            if int(code[i]) == num and i > 0:
                if code[i-1] not in ll:
                    ll.append(code[i-1])
                if i == 2 and code[i-2] not in ll:
                    ll.append(code[i-2])
    b[num] = ll

for k in sorted(b, key=lambda k: len(b[k]), reverse=False):
        print(k, end='')
print('')
