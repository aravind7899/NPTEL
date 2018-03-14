players = {}
while(True):
    line = input()
    if line == '':
        break
    match = line.split(":")
    sets = match[2].split(",")
    if match[0] not in players:
        players[match[0]] = []
        for i in range(0, 6):
            players[match[0]].append(0)

    if match[1] not in players:
        players[match[1]] = []
        for i in range(0, 6):
            players[match[1]].append(0)
    if len(sets) > 3:
        players[match[0]][0] += 1
    else:
        players[match[0]][1] += 1
    for s in sets:
        s = s.split("-")
        if s[0] > s[1]:
            players[match[0]][2] += 1
            players[match[1]][4] += 1   
        else:
            players[match[1]][2] += 1
            players[match[0]][4] += 1   
        players[match[0]][3] += int(s[0])
        players[match[1]][5] += int(s[0])   
        players[match[1]][3] += int(s[1])
        players[match[0]][5] += int(s[1])   
result = sorted(players.items(), key=lambda a: a[1], reverse=True)
for i in result:
    print(i[0], " ".join(map(str, i[1])))
