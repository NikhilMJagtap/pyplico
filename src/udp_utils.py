from dpkt.ip import IP
from dpkt.udp import UDP
from dpkt.dns import DNS, DNS_QUERY
from dpkt.dpkt import UnpackError

# TODO: add some doc

class UdpUtils:

    @staticmethod
    def is_upd(ip, verbose=False):
        if not isinstance(ip, IP):
            raise ValueError(f"Argument IP should be instance of dpkt.ip.IP")
        udp = ip.data
        if isinstance(udp, UDP):
            return True
        return False

    @staticmethod
    def get_udp_details(ip):
        # checking the packet is UDP or no
        if not UdpUtils.is_upd(ip):
            raise ValueError("Given packet is not UDP packet")
        else:
            # getting UDP data in dictionary
            udp = ip.data
            udp_details = {}
            udp_details["src_port"] = udp.sport
            udp_details["dest_port"] = udp.dport
            udp_details["length"] = udp.ulen
            udp_details["sum"] = udp.sum
            return udp_details

    @staticmethod
    def is_dns(ip):
        if not UdpUtils.is_upd(ip):
            return False
        udp = ip.data
        if udp.sport == 53 or udp.dport == 53:
            return True
        return False


    @staticmethod
    def get_dns_queries(ip, verbose=False):
        # TODO: check flags in dpkt github
        if not UdpUtils.is_dns(ip):
            raise ValueError("Packet is not a DNS packet")
        udp = ip.data
        try:
            dns_ = DNS(udp.data)
            # dns is not a query
            if dns_.opcode != DNS_QUERY:
                raise ValueError("DNS is not a query")
            query = {
                'query' : [dns_.qd[i].name for i in range(len(dns_.qd))],    # query domain
                'server': [dns_.ns[i].nsname for i in range(len(dns_.ns))],  # name server
                'answer': [dns_.an[i].name for i in range(len(dns_.an))]     # answer
            }
            return query
        except (UnpackError, AttributeError):  # need fix on Attribute error
            if verbose:
                print("failed to unpack")
            return {}