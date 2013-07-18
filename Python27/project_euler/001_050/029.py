lisst = set()

for a in xrange(2,101):
    for b in xrange(2,101):
        lisst.update([pow(a,b)])

print len(lisst)
