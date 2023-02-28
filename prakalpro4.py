# def luasPersegi(panjang,lebar,tinggi):
#     hari=jang*lebar*tinggi
#     return hari
# a=int(input('Masukan Panjang:'))
# b=int(input('Masukan Lebar:'))
# c=int(input('Masukan Tinggi:'))

# # print(luasPersegi(a,b))

# def tagihan (pemakaian, golongan = 3):
#     bayar=0
#     pemakaian_100 = 100 if pemakaian > 100 else pemakaian
#     pemakaian_100_lebih = pemakaian - pemakaian_100
#     if golongan == 1:
#         bayar=pemakaian_100*1500+ pemakaian_100_lebih*2000
#     elif golongan == 2:
#         bayar=pemakaian_100*2500+ pemakaian_100_lebih *3000
#     elif golongan == 3:
#         bayar= pemakaian_100*4000



# def palingkiri(a,b,c):

# a=int(input('Masukan Bilangan:'))
# b=int(input('Masukan Bilangan:'))
# c=int(input('Masukan Bilangan:'))
# kanan1= a % 10
# kanan2 = b % 10
# kanan3 = c % 10
# if kanan1==kanan2 and kanan2==kanan3:
#     print('semua sama')


# def hitunghari(sekarang,n):
#     hari=n%7
    
#     if sekarang=="senin":
#         if hari==0:
#             print("senin")
#         elif hari==1:
#             print("selasa")
#         elif hari ==2:

def runner_up(a,b,c,d,e):
    pelari=[a,b,c,d,e]
    terendah=min(pelari)
    terendah=pelari.remove(terendah)
    terendah=min(pelari)
    print(terendah)

pelari_a=5.56
pelari_b=3.67
pelari_c=2.35
pelari_d=6.6
pelari_e=9.57


runner_up(pelari_a,pelari_b,pelari_c,pelari_d,pelari_e)