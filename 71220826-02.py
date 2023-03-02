def selisih_hari(tanggal1, bulan1, tanggal2, bulan2):
    hari_bulan = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    hari_tahun=sum(hari_bulan)
    sisa_awaltahun=sum(hari_bulan[bulan1:])-tanggal1
    sisa_akhirtahun=sum(hari_bulan[:bulan2])+tanggal2
    
    selisih=hari_tahun-sisa_akhirtahun-sisa_awaltahun

    print(f"Selisih Harinya adalah : {selisih}")
    


tanggal1=int(input("Masukan Tanggal Awal:"))
bulan1=int(input("Masukan Bulan Awal:"))
tanggal2=int(input("Masukan Tanggal Akhir:"))
bulan2=int(input("Masukan Bulan Akhir:"))
selisih_hari(tanggal1, bulan1, tanggal2, bulan2)    