
def becon(a):
    l=list()
    a=a.replace(' ', '')
    print(a)
    for k in a:
        if(k.isupper()):
            k='b'
            l.append(k)
        else:
            k='a'
            l.append(k)
    l=''.join(l)
    print(l)
    c=[l[i:i+5] for i in range(0,len(l),5)]
    print(c)

    key='aaaaabbbbbabbbaabbababbaaababaab'
    alp='abcdefghijklmnopqrstuvwxyz'
    for m in range(0, len(c)):
        if(c[m] in key):
            print (alp[key.index(c[m])])


print(becon(input()))
