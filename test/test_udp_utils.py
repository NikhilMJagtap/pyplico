import unittest
from pyplico.packetReader import PacketReader
from pyplico.udp_utils import UdpUtils

class TestUDP(unittest.TestCase):

    def test_is_dns(self):
        count = 0
        pr = PacketReader("../src/data/dns.cap", to_itr=False, to_list=True)
        for packet in pr.packets:
            if UdpUtils.is_dns(packet[0]):
                count += 1
        assert count == 707

    def test_is_udp(self):
        count = 0
        pr = PacketReader("../src/data/sample.pcap", to_itr=False, to_list=True)
        for packet in pr.packets:
            if UdpUtils.is_udp(packet[0]):
                count += 1
        assert count == 2

    def test_udp_details(self):
        pr = PacketReader("../src/data/sample.pcap", to_itr=False, to_list=True)
        udp_packets = list()
        for packet in pr.packets:
            if UdpUtils.is_udp(packet[0]):
                udp_packets.append(packet[0])
        assert len(udp_packets) == 2
        packet = udp_packets[0]
        packet_details = UdpUtils.get_udp_details(packet)
        assert packet_details['src_port'] == 8000
        assert packet_details['dest_port'] == 3801
        assert packet_details['length'] == 3320

if __name__ == "__main__":
    unittest.main()