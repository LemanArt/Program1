from view.view_nilai import *

while True:
    c = input("\nT)ambah, U)bah, C)ari, H)apus, L)ihat, K)eluar: ")

    if c.lower() == 't':
        tambah()

    elif c.lower() == 'u':
        ubah()

    elif c.lower() == 'c':
        cari()

    elif c.lower() == 'h':
        hapus()

    elif c.lower() == 'l':
        lihat()

    elif c.lower() == 'k':
        print("====Anda keluar dari Program====")
        break

    else:
        print("Menu yang anda maksud tidak tersedia, Silahkan pilih menu yang tersedia")