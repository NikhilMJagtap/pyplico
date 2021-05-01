import unittest
from pyplico.packetReader import PacketReader
from pyplico.smtp_utils import SMTPUtils

class TestSMTP(unittest.TestCase):

    pr = PacketReader("../src/data/smtp.pcap", to_itr=False, to_list=True, to_ft=True)

    def test_smtp_details(self):
        pr = self.pr
        for packet in pr.packets:
            try:
                SMTPUtils.get_smtp_details(packet[0])
            except ValueError:
                pass

    def test_smtp_hunt_credentials(self):
        pr = self.pr
        ft = pr.get_flow_table()
        creds = SMTPUtils.hunt_credentials(ft, connection="192.168.1.4__217.12.11.66__1470__587")
        assert len(creds) == 1
        assert creds[0]['password'] == 'V1v1tr0n'
        assert creds[0]['username'] == 'galunt'

    def test_smtp_hunt_address(self):
        pr = self.pr
        ft = pr.get_flow_table()
        
        addresses = SMTPUtils.hunt_mail_address(ft, connection="192.168.1.4__217.12.11.66__1470__587")
        assert 'from' in addresses.keys()
        assert 'to' in addresses.keys()
        assert 'xxxxxx@xxxxx.co.uk' in addresses['from']
        assert 'xxxxxx.xxxx@xxxxx.com' in addresses['to']

        

if __name__ == "__main__":
    unittest.main()