import unittest
from pyplico.packetReader import PacketReader
from pyplico.smtp_utils import SMTPUtils

class TestFlowTable(unittest.TestCase):
    def test_flow_table(self):
        pr = PacketReader("../src/data/smtp.pcap", to_itr=False, to_list=True, to_ft=True, sort=True)
        ft = pr.get_flow_table()

if __name__ == "__main__":
    unittest.main()