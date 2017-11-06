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
    abbr = e[0]
    while abbr in D.keys():
        oldkey = abbr
        oldval = D.pop(abbr)
        newkey = oldkey + oldval[len(abbr)]
        D[newkey] = oldval
        abbr += e[len(abbr)]
    D[abbr] = e
print(D)
