T = """knight
miller
reeve
cook
man of law
wife of bath
friar
summoner
clerk
merchant
squire
franklin
physician
pardoner
shipman
prioress
sir thopas
melibee
monk
nun's priest
second nun
canon's yeoman
manciple
parson"""

P = T.split('\n')
P.sort()
#print(P)

D = {}
for e in P:
    if e[0] not in D.keys():
        D[e[0]] = e
    else:
        D[e] = e
print(D)


