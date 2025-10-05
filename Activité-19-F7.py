
def F7(n):
    R=1
    if n == 1 or n == 2:
        return 1
    else:
        R=F7(n-1)+F7(n-2)
        return R

n=int(input("Entrez un nombre (different à 0):"))
while n == 0:
    n=int(input("Entrez un nombre (different à 0):"))
for i in range(n):
    print(F7(i+1))