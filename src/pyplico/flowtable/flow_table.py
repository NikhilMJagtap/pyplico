from bisect import insort
from pyplico.flowtable.flow_table_entity import FlowTableEntity
from pyplico.tcp_utils import TCPUtils
from pyplico.utils import ip_addr_to_str

class FlowTable:
    """
    Flow Table is an entity which tracks the IP packets sent between any two hosts on particular port mapping
    It has a map which stores key value pairs as follows:
    Key is a unique string formed by IP addresses and ports.
    Value is the array FlowTableEntities.
    """
    def __init__(self):
        self.table = dict()

    def push(self, ip):
        if not TCPUtils.is_tcp(ip):
            raise ValueError("Given packet is not TCP packet. Flow Table only supports TCP packets.")
        _key = self._get_lookup_key(ip)
        if _key in self.table:
            pass
        else:
            self.table[_key] = []
        _flow = self.table[_key]
        _entity = self._get_entity(ip, _key)
        _index = self._get_index_to_insert(_entity, _flow)
        _flow.insert(_index, _entity)
        self.table[_key] = _flow

    def _get_lookup_key(self, ip):
        tcp = ip.data
        src_first_key = ip_addr_to_str(ip.src) + '__' + ip_addr_to_str(ip.dst) + '__' + str(tcp.sport) + '__' + str(tcp.dport)
        dest_first_key = ip_addr_to_str(ip.dst) + '__' + ip_addr_to_str(ip.src) + '__' + str(tcp.dport) + '__' + str(tcp.sport)
        return min(src_first_key, dest_first_key)

    def _get_entity(self, ip, key):
        return FlowTableEntity(
            ip, key
        )

    def _get_index_to_insert(self, entity, flow):
        curr_ack = entity.tcp.ack
        curr_seq = entity.tcp.seq
        next_seq = entity.next_seq
        if len(flow) == 0:
            return 0
        for i in range(len(flow)):
            if flow[i].tcp.seq == curr_ack:
                return i+1
            elif flow[i].tcp.ack == next_seq:
                return i
        return len(flow)
