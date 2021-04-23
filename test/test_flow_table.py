import unittest
from pyplico.packetReader import PacketReader
from pyplico.flowtable import FlowTable
from pyplico.smtp_utils import SMTPUtils

class TestFlowTable(unittest.TestCase):
    def test_flow_table(self):
        pr = PacketReader("../src/data/smtp.pcap", to_itr=False, to_list=True, sort=True)
        ft = FlowTable()
        for packet in pr.packets:
            try:
                ft.push(packet[0])
            except ValueError:
                pass

        SMTPUtils.hunt_credentials(ft, connection="192.168.1.4__217.12.11.66__1470__587")

if __name__ == "__main__":
    unittest.main()