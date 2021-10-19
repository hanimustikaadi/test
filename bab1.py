
x = input('Apakaah ada susu?(Yes/No)')
if x== 'Yes' :
    y= input(r'Apakah ada telor?(Yes\No)')
    if y=='Yes':
        z = int(input(r'Berapa jumlah telor'))
        if z >=6:
            print('anda mengambil 6 telor')
            print('anda membawa 1 botol susu dan 6 telor')
        else:
            print('tidak jadi beli telor')
            print('hanya mebawa 1 botol susu untuk pulang')
    if y=='No':
        print('Pulang hanya membawa 1 botol susu')

if x =='No':
    print('Saatnya pulang dengan tangan kosong')