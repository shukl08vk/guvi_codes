a=int(raw_input())
sum=0
if a<0:
        a=abs(a)
while a>0:
        c=a%10
        sum+=c
        a=a/10

print sum




