class FlowTableEntity:
    def __init__(self, ip, key):
        self.ip = ip
        self.key = key
        self.tcp = ip.data
        self.seq = self.tcp.seq

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