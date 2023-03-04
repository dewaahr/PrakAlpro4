def cek_digit_belakang(bilangan_satu,bilangan_dua,bilangan_tiga):
 
    bilangan_satu=bilangan_satu % 10
    bilangan_dua=bilangan_dua%10
    bilangan_tiga=bilangan_tiga%10

    if bilangan_satu==bilangan_dua or bilangan_satu==bilangan_tiga or bilangan_tiga==bilangan_dua:
        print('True')
    else: print('False')

a=int(input('Masukan Bilangan Pertama:'))
b=int(input('Masukan Bilangan Kedua:'))
c=int(input('Masukan Bilangan Ketiga:'))
cek_digit_belakang(a,b,c)

#Tes Case

cek_digit_belakang(30,20,18)
cek_digit_belakang(145,5,100)
cek_digit_belakang(71,187,18)
cek_digit_belakang(1024,14,94)
cek_digit_belakang(53,8900,658)