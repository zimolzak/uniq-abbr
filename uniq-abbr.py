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

def string_heads(L):
    H = []
    for e in L:
        while len(e) > 1:
            e = e[0:-1]
            H += [e]
    return H

D = {}
for e in P:
    #print(e.upper())
    abbr = e[0]
    forbidden_abbrs = list(D.keys()) + string_heads(D.keys())
    while abbr in forbidden_abbrs:
        if abbr in D.keys():
            oldkey = abbr
            oldval = D.pop(abbr)
            newkey = oldkey + oldval[len(abbr)]
            D[newkey] = oldval
            #print("extended", oldval, "to", newkey)
        # else abbr was in the list of forbidden substrs, not real keys
        abbr += e[len(abbr)]
        #print("and extended", e, "to", abbr)
        forbidden_abbrs = list(D.keys()) + string_heads(D.keys()) #update
    D[abbr] = e
    #print("good:", abbr)

assert(len(D) == len(P))
k = list(D.keys())
k.sort()
for e in k:
    print(e + '\t' + D[e])
