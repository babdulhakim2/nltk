
def cleandata(rec):
    new = []
    l=[]
    for i in rec:
        new.append(list(i))
    for n in new:
        if n[6]=='Exam':
            del(n[7])
        elif n[6]=='CA':
            del(n[8])
    for a in new:
        l.append(tuple(a))
    return l

