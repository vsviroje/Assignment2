import math;
n=int(input());
c=0
while n>0:
    n=math.floor(n/10);
    c=c+1;
print(c);
