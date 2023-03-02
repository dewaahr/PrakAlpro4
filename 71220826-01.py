def jumlah_hari(nama_bulan):
    bulan_31=['januari','maret','mei','juli','agustus','oktober','desember']
    bulan_30=['april','juni','september','november']
    if nama_bulan in bulan_31:
        print(f'Jumlah hari dalam bulan {nama_bulan} adalah : 31 Hari')
    elif nama_bulan in bulan_30:
        print(f'Jumlah hari dalam bulan {nama_bulan} adalah : 30 Hari')
    elif nama_bulan=='februari':
        print(f'Jumlah hari dalam bulan {nama_bulan} adalah : 28 Hari')
    else : print(f'Tidak Valid')


nama_bulan=input('Masukan Nama Bulan:')
nama_bulan=nama_bulan.lower()
jumlah_hari(nama_bulan)

