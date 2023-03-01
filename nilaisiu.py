def ratarata(n1,n2,n3,n4,n5,n6,n7,n8):
    #pake subslist+sort+remove
    nilai=[n1,n2,n3,n4,n5,n6,n7,n8]
    nilai.sort()
    # print(nilai)
    # a=nilai[0]
    # b=nilai[1]
    # nilai.remove(a)
    # nilai.remove(b)
    # # print(nilai)
    # totalnilai=sum(nilai)
    # rata_rata=totalnilai//6
    # print(rata_rata)

    #2 min remove
    a=min(nilai)
    nilai.remove(a)
    b=min(nilai)
    nilai.remove(b)
    totalnilai=sum(nilai)
    rata_rata=totalnilai/6
    print(round(rata_rata))
    
#PAKEK // GA SESUAI TEST CASE. PAKEK / BARU DI ROUND BARU SESUAI

# print(nilai)
# # nilai=[5,3,67,983,462]
# nilai.sort()
# print(nilai)

# n1=50
# n2=70
# n3=75
# n4=20
# n5=25
# n6=64
# n7=83
# n8=65

n1=int(input('n1:'))
n2=int(input('n2:'))
n3=int(input('n3:'))
n4=int(input('n4:'))
n5=int(input('n5:'))
n6=int(input('n6:'))
n7=int(input('n7:'))
n8=int(input('n8:'))
ratarata(n1,n2,n3,n4,n5,n6,n7,n8)