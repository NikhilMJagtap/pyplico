class FlowTableEntity:
    def __init__(self, ip, key):
        self.ip = ip
        self.key = key
        self.tcp = ip.data
        self.seq = self.tcp.seq
        self.ack = self.tcp.ack
        self.next_seq = self.get_next_seq_num()

    def get_next_seq_num(self):
        next_seq_number = self.seq
        if len(self.tcp.data) == 0:
            next_seq_number += 1
        else:
            next_seq_number += len(self.tcp.data)
        return next_seq_number

    def __lt__(self, other):
        if self.key != other.key:
            raise ValueError("Invalid comparison of Flow Table Entities.")
        return self.seq < other.seq

    def __gt__(self, other):
        if self.key != other.key:
            raise ValueError("Invalid comparison of Flow Table Entities.")
        return self.seq > other.seq

    def __le__(self, other):
        if self.key != other.key:
            raise ValueError("Invalid comparison of Flow Table Entities.")
        return self.seq <= other.seq

    def __ge__(self, other):
        if self.key != other.key:
            raise ValueError("Invalid comparison of Flow Table Entities.")
        return self.seq >= other.seq