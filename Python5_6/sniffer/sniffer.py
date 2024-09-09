from scapy.all import *

iPkt = 0

def process_packet(packet):
    global iPkt
    iPkt += 1
    print("Ho letto un okt nella tua macchina" + str(iPkt))
    
    if not packet.haslayer(IP):
        return 
    ip_layer = "IP_SRC: "+packet[IP].src+"IP_DST: "+packet[IP].dst + " "+str(packet[IP].proto)
    print(ip_layer)
 
    if str(packet[IP].proto == "6"):
        print("TCP_SRC: "+str(packet[TCP].dport) + " TCP_DST: "+str(packet[TCP].sport))
    
    if (packet[TCP].dport == 443 or packet[TCP].sport == 443):
        print("Questo è un pacchetto con protocollo TLS")

    if (packet[TCP].dport == 80 or packet[TCP].sport == 80):
        print("Protocollo HTTP")

    if (packet[TCP].dport == 80):
        print("Questa è una richiesta HTTP")
        if packet.haslayer(HTTPRequest):
            print(packet[HTTPRequest].show())

    if (packet[TCP].sport == 80):
        print("Questa è una risposta HTTP")
        if packet.haslayer(HTTPResponse):
            print(packet[HTTPResponse].show())

sniff(iface="eth0", filter="tcp", prn=process_packet)



#scrivere sul termine sudo python3 sniffer.py per farlo funzionare