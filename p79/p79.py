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
    c1 = [log[0], log[1]]
    c2 = [log[0], log[2]]
    c3 = [log[1], log[2]]
    constraints.append(c1)
    constraints.append(c2)
    constraints.append(c3)
print constraints
