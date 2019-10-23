import math;

n=int(input());

c=math.ceil((n/2)+1);

i=0;

for i in range(2,c,1):
    if n%i==0:
        break;


if(i==(c-1)):
    print("prime");
else:
    print("not prime");