import scapy.all as scapy
import optparse

            #------> Yapılacaklar <------
                    #İstek
                    #Yayin
                    #cevap

def kullanci_girdi():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--ip",dest="ip_adresi",help="ip Adresini giriniz !")

    (user_input,arguments) = parse_object.parse_args()
    return user_input

def tarama(ip):
    arp_istek = scapy.ARP(pdst=ip)
    yayin_paketi = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    paket_birlestir = yayin_paketi / arp_istek
    (cevaplanan_paketler,cevaplanmayan_paketler) = scapy.srp(paket_birlestir,timeout = 1)
    cevaplanan_paketler.summary()

taranacak_ip = kullanci_girdi()
tarama(taranacak_ip.ip_adresi)
