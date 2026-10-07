# Example of packet crafting / sniffing

from scapy.all import sniff

def process_packet(packet):
    print(packet.summary())

from scapy.config import conf
conf.use_pcap = True
sniff(filter = "ip", prn = process_packet, count = 5)