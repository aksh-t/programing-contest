# https://atcoder.jp/contests/abc070/submissions/11164686
_,a,*l=map(int,open(0))
from fractions import*
for i in l:a*=i//gcd(a,i)
print(a)