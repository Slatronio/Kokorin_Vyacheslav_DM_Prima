a=[[0,4,0,3,6,1,0],[4,0,2,3,7,6,1],[0,2,0,0,4,0,2],[3,3,0,1,1,5,3],[3,7,4,1,0,3,6],[1,6,0,5,3,0,7],[0,1,2,3,6,7,0]]
for o in range(2):
    for i in range(len(a)):
        print(a[i])
    print()
    t=[]
    t.append(0)
    ssum=0
    spis=[]
    fik=[0,1,2,3,4,5,6]
    spis.append(0)
    while (sorted(spis)!=fik):
        c=[]
        for m in t:
            for n in range(len(a[m])):
                if n in t:
                    a[m][n]=0
        for i in t:
            k=(min(enumerate(a[i]), key=lambda x: x[1] if ((a[i].index(x[1]) not in spis) and x[1]!=0) else float('Inf'))[0])
            if k!=0:
                c.append(a[i][k])
                c.append(k)
        l=100000
        z=0
        for  i in range(0,len(c),2):
                       if (c[i]<l):
                           l=c[i]
                           z=c[i+1]
        ssum+=l
        spis.append(z)
        t.append(z)
        t=sorted(t)
    print(ssum)
    print()
    a=[[0,15,0,23,14,0,0,0,0],[14,0,19,16,15,0,0,0,0],[0,19,0,0,14,26,0,0,0],[23,16,0,0,25,0,23,20,0],[14,15,14,25,0,24,0,27,18],[0,0,26,0,24,0,0,0,0],[0,0,0,23,0,0,0,14,0],[0,0,0,20,27,0,14,0,18],[0,0,0,0,18,0,0,18]]
