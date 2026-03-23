print("selamat di pulau harta karun!!!")
print("misi kamu adalah menemukan harta karun")
pilihan_1 = input("kamu ada di persimpangan jalan,kemana kamu akan pergi? ketik 'kiri' atau 'kanan'.").lower()
if pilihan_1 == 'kanan':
    pilihan_2 = input("kamu menemukan sungai,di tengah sungai itu ada pulau, "
                      "ketik 'tunggu' untuk menunggu perahu,ketik 'berenang' untuk berenang")
    if pilihan_2 ==  'tunggu' :
        pilihan_3 = input("kamu tiba di pulau ini tanpa terluka,disana ada tiga pintu merah,kuning dan biru,pintu yang kmu pilih?")

        if pilihan_3 == 'kuning':
            print("ruangan ini terisi api game over")
        elif pilihan_3 == 'biru':
            print("selamat kamu menemukan harta karun")
        elif pilihan_3 == 'merah':
            print("di dalam ruangan ini ada binatang buas yaitu tuyul game over")
        else:
            print("kma memilih pintu yang tidak ada Game Over")
    else:
        print("kamu di serang oleh buaya yang lapar,Game Over")
else :
    print("kamu terjun ke jurang,Game Over!!!")
