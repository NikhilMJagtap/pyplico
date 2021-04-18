import unittest
from pyplico.packetReader import PacketReader
from pyplico.smtp_utils import SMTPUtils

class TestSMTP(unittest.TestCase):
    def test_smtp_details(self):
        pr = PacketReader("../src/data/smtp.pcap", to_itr=False, to_list=True)
        for packet in pr.packets:
            try:
                SMTPUtils.get_smtp_details(packet[0])
            except ValueError:
                pass

        

if __name__ == "__main__":
    unittest.main()