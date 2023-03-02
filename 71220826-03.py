def ratarata(n1,n2,n3,n4,n5,n6,n7,n8):
    nilai=[n1,n2,n3,n4,n5,n6,n7,n8]
    nilai.sort()
    a=nilai[0]
    b=nilai[1]
    nilai.remove(a)
    nilai.remove(b)
    totalnilai=sum(nilai)
    rata_rata=totalnilai//6
    print(f'Rata rata dari 6 nilai terbaik adalah {rata_rata}')

n1=int(input('Masukan Nilai 1:'))
n2=int(input('Masukan Nilai 2:'))
n3=int(input('Masukan Nilai 3:'))
n4=int(input('Masukan Nilai 4:'))
n5=int(input('Masukan Nilai 5:'))
n6=int(input('Masukan Nilai 6:'))
n7=int(input('Masukan Nilai 7:'))
n8=int(input('Masukan Nilai 8:'))
ratarata(n1,n2,n3,n4,n5,n6,n7,n8)