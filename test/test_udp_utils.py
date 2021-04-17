from pyplico.packetReader import PacketReader
from pyplico.udp_utils import UdpUtils

def test_is_dns():
    count = 0
    pr = PacketReader("../src/data/dns.cap", to_itr=False, to_list=True)
    for packet in pr.packets:
        if UdpUtils.is_dns(packet[0]):
            count += 1
    assert count == 707

def test_is_udp():
    count = 0
    pr = PacketReader("../src/data/sample.pcap", to_itr=False, to_list=True)
    for packet in pr.packets:
        if UdpUtils.is_udp(packet[0]):
            count += 1
    assert count == 2

if __name__ == "__main__":
    test_is_udp()