def hitung_data_di_list(data_dalam_list):
    n = len(data_dalam_list)
    return n

def kalikan_angka_dalam_list(data_dalam_list,jumlah_data_dalam_list):
    list_new = []
    for i in range(jumlah_data_dalam_list):
        list_new.append(jumlah_data_dalam_list*data_dalam_list[i])
    return list_new

def jumlah_data_di_list(list_baru):
    hasil_akhir = sum(list_baru)
    return hasil_akhir