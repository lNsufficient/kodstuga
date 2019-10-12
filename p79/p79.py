f =open("keylog.txt")
print f
logs = []
for line in f:
    print line
    tmp = [int(line[0]), int(line[1]), int(line[2])]
    logs.append(tmp)
print logs

constraints = []

for log in logs:
    c1 = (log[0], log[1])
    c2 = (log[0], log[2])
    c3 = (log[1], log[2])
    constraints.append(c1)
    constraints.append(c2)
    constraints.append(c3)

constraints = list(set(constraints))
print constraints


before = { i : [] for i in range(10)}
after = { i : [] for i in range(10)}

for c in constraints:
    before_key = c[1]
    if c[0] not in before[before_key]:
        before[before_key].append(c[0])

    after_key = c[0]
    if c[1] not in after[after_key]:
        after[after_key].append(c[1])

print before
print after
answer = []
i = 0
while(i < 10):
    if not before[i]:
        print i
        answer.append(i)
        before[i] = [-1]
        for j in range(10):
            if i in before[j]:
                before[j].remove(i)
                print before[j]
        i = 0
        continue
    else:
        i+=1
print answer
