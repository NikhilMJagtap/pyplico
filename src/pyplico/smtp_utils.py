from dpkt.tcp import TCP
from dpkt.ip import IP
from pyplico.udp_utils import UdpUtils

#  TODO: shift is_tcp function to staticscope of tcp_utils
def is_tcp(ip, verbose=False):
    if not isinstance(ip, IP):
        raise ValueError(f"Argument IP should be instance of dpkt.ip.IP")
    tcp = ip.data
    if isinstance(tcp, TCP):
        return True
    return False


#  TODO: add docs 

class SMTPUtils:

    """
    As SMTP is application layer protocol and it has dedicated ports of 25, 465 and 587, we need to check
    the transport protocol of the packet. The TCP and UDP are used in SMTP, UDP is very very rare, at
    least in industrial use.
    This function returns whether the packet is SMTP or not

    parameters:
        - ip : packet of IP type. Instance of dpkt.ip.IP
        - verbose : print details or no
    
    returns:
        - bool: true if ip is SMTP else false

    """
    @staticmethod
    def is_smtp(ip, verbose=False):
        ports = [25, 465, 587]
        # change is_tcp to TCPUtils.is_tcp() after smtp staging
        if is_tcp(ip) or UdpUtils.is_udp(ip):
            tcp = ip.data
            if tcp.sport in ports or tcp.dport in ports:
                print(tcp.data)
                return True
            return False
        else:
            if verbose:
                print(f"ip is neither TCP nor UDP.")
            return False