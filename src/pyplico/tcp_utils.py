from dpkt.tcp import TCP
from dpkt.ip import IP

class TCPUtils:
    @staticmethod
    def is_tcp(ip, verbose=False):
        if not isinstance(ip, IP):
            raise ValueError(f"Argument IP should be instance of dpkt.ip.IP")
        tcp = ip.data
        if isinstance(tcp, TCP):
            return True
        return False