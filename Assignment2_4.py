import math;

n=int(input());

c=math.ceil((n/2)+1);

for i in range(1,c,1):
    if n%i==0:
        print(i,end=' ');
