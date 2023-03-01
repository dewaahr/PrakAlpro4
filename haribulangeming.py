def jumlah_hari(nama_bulan):
    bulan_31=['januari','maret','mei','juli','agustus','oktober','desember']
    bulan_28=['februari']
    bulan_30=['april','juni','september','november']
    if nama_bulan in bulan_31:
        print('31 Hari')
    elif nama_bulan in bulan_28:
        print('28 Hari')
    elif nama_bulan in bulan_30:
        print('30 Hari')
    else:print('Tidak Valid')


nama_bulan=input('Masukan Nama Bulan:')
jumlah_hari(nama_bulan)