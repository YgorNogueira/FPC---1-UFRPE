#mdc
def mdc(f1, f2):
    if f2 == 0:
        return f1
    resto = f1 % f2
    f1 = f2
    f2 = resto
    return mdc(f1, f2)


#entrada
n = int(input())
for i in range(n):
    f1, f2 = map(int, input().split())
    print(mdc(f1, f2)) 

    
