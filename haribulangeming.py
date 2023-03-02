def jumlah_hari(nama_bulan):
    #freestyle
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
        
        #nonfreestyle
#     if nama_bulan == 'januari' or 'maret' or 'mei' or 'juli' or 'agustus' or 'oktober' or 'desember'
#         print('31 Hari')
#     elif nama_bulan == 'februari'
#         print('28 Hari')
#     elif nama_bulan == 'april' or 'juni' or 'september' or 'november'


nama_bulan=input('Masukan Nama Bulan:')
jumlah_hari(nama_bulan)
