N=int(raw_input())
K=int(raw_input())

a=[]
sum=0
if N>0:
        for i in range(N):
                p=int(raw_input())
                a.append(p)
        if K>0:
                for i in range(K):
                        sum+=a[i]
                print sum
        else:
                print "0"

        
else:
        print "0"



