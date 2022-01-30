from socket import timeout
import scapy.all as scapy 

#Yapilacaklar
#
#ARP isteği (arp reques)
#Yayın (broadcast)
#Cevap(response)

ip_istek = input("Taramak İstediginiz ip adresini giriniz: ")

arp_istek = scapy.ARP(pdst = ip_istek + "/24")
broadcast_yayin = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
combined_packet = broadcast_yayin/arp_istek
(answered_list,unaswered_list) = scapy.srp(combined_packet,timeout=1)
answered_list.summary()
