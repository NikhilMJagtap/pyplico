import unittest
from pyplico.packetReader import PacketReader
from pyplico.flowtable import FlowTable

class TestFlowTable(unittest.TestCase):
    def test_flow_table(self):
        pr = PacketReader("../src/data/sample.pcap", to_itr=False, to_list=True, sort=True)
        ft = FlowTable()
        for packet in pr.packets:
            try:
                ft.push(packet[0])
            except ValueError:
                pass

if __name__ == "__main__":
    unittest.main()