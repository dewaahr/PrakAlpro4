def selisih_hari(tanggal1,bulan1,tanggal2,bulan2):
    hari = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    haridalamtahun=sum(hari)
    tgl_awal=sum(hari[bulan1:])-tanggal1
    tgl_akhir=sum(hari[:bulan2])+tanggal2
    # print(tgl_awal,tgl_akhir)
    selisih=haridalamtahun-tgl_awal-tgl_akhir
    print(abs(selisih))
    # haridalamtahun=sum(hari)
    # tgl_akhir=sum(hari[:])
    # print(tgl_akhir)
        # if selisih<0:
        #     print("Tidak valid")
        # else:print(selisih)

tanggal1=int(input('tgl 1:'))
bulan1=int(input('bln 1:'))
tanggal2=int(input('tgl 2:'))
bulan2=int(input('bln 2:'))


selisih_hari(tanggal1,bulan1,tanggal2,bulan2)