
def convert_n_to_m(x,n,m):
    '''if(int(x) is False): return False'''
    n=int(n)
    m=int(m)
    x=int(x,n)
    l=[]
    while(x>=m):
        y=x%m
        l.append(str(y))
        x=x//m
    else:
        l.append(str(x))
    l1=l[::-1]

    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    l2=[]
    if(m>9):
        for i in l1:
            i=alphabet[int(i)]
            l2.append(i)
        s2=''.join(l2)
        return s2
    else:
        s1=''.join(l1)
        return s1

print(convert_n_to_m(input(),input(),input()))







