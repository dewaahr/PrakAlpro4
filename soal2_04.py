def cek_digit_belakang(a,b,c):
    a=a % 10
    b=b%10
    c=c%10
    if a==b or a==c or c==b:
        print('True')
    else: print('False')

# print(a,b,c)
a=int(input('Masukan Bilangan 1:'))
b=int(input('Masukan Bilangan 2:'))
c=int(input('Masukan Bilangan 3:'))
cek_digit_belakang(a,b,c)