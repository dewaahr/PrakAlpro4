def cek_angka(bilangan_satu,bilangan_dua,bilangan_tiga):
    if bilangan_satu!=bilangan_dua and bilangan_satu!=bilangan_tiga and bilangan_dua!=bilangan_tiga:
        if bilangan_satu+bilangan_dua==bilangan_tiga or bilangan_satu+bilangan_tiga==bilangan_dua or bilangan_dua+bilangan_tiga==bilangan_satu:
            print('True')
        else: print('False')
    else: print('False')

#Tes Case - Jika True
print('Tes Case 30,10,20')
cek_angka(30,10,20)
#Tes Case - Jika False
print('Tes Case 11,4,2')
cek_angka(11,4,2)