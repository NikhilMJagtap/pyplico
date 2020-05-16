from dpkt.ip import IP
from dpkt.udp import UDP
from dpkt.dns import DNS, DNS_QUERY

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
    def get_dns_queries(ip):
        # TODO: check flags in dpkt github
        if not UdpUtils.is_dns(ip):
            raise ValueError("Packet is not a DNS packet")
        udp = ip.data
        dns_ = DNS(udp.data)
        # dns is not a query
        if dns_.opcode != DNS_QUERY:
            raise ValueError("DNS is not a query")
        print(dns_.qd[0].name)
        print(dns_.an[0].name)
        print(dns_.an[0].ptrname)
        print(dns_.ns[0].nsname)
        print(len(dns_.ns))
        # TODO: complete DNS queries and responses