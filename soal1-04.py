def cek_angka(a,b,c):
    if a!=b and a!=c and b!=c:
        if a+b==c or a+c==b or b+c==a:
            print('True')
        else: print('False')
    else: print('False')

a=3
b=2
c=5
cek_angka(a,b,c)