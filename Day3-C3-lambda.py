# lambda - anonymous

def areaCircle(rad):
    return 22*rad*rad/7

print(areaCircle(21))


A = lambda rad: rad * rad * 22 / 7
print(A(21))

R = lambda hei, len : len * hei

print(R(10,20))
print(R(15,25))


Q1 = lambda a,b,c : -(-b + (b**2 - 4*a*c)**0.5) / (2*a)
Q2 = lambda a,b,c : -(-b - (b**2 - 4*a*c)**0.5) / (2*a)


print(f'a,b,c values is 1,5,6  {Q1(1,5,6)}, {Q2(1,5,6)}')
print(f'a,b,c values is 1,6,9  {Q1(1,8,12)}, {Q2(1,8,12)}')