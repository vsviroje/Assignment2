import math;
n=int(input());
c=0;
d=0;
while n>0:
    d=n%10;
    c=c+d;
    n = math.floor(n / 10);
print(c);
