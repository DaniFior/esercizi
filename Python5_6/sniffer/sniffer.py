from scapy.all import *

iPkt = 0

def process_packet(pkt):
    global iPkt
    iPkt += 1
    print("Ho letto un okt nella tua macchina" + str(iPkt))

sniff(iface="eth0", filter="tcp", prn=process_packet)

#scrivere sul termine sudo python3 sniffer.py per farlo funzionare