from dpkt.tcp import TCP
from dpkt.ip import IP
from pyplico.udp_utils import UdpUtils
from pyplico.tcp_utils import TCPUtils
from pyplico.constants import smtp

#  TODO: add docs 

class SMTPUtils:

    """
    As SMTP is application layer protocol and it has dedicated ports of 25, 465 and 587, we need to check
    the transport protocol of the packet. The TCP and UDP are used in SMTP, UDP is very very rare, at
    least in industrial use.
    """
    @staticmethod
    def is_smtp(ip, verbose=False):
        """
            This function returns whether the packet is SMTP or not

            parameters:
                - ip : packet of IP type. Instance of dpkt.ip.IP
                - verbose : print details or no
            
            returns:
                - bool: true if ip is SMTP else false
        """
        ports = [25, 465, 587]
        if TCPUtils.is_tcp(ip) or UdpUtils.is_udp(ip):
            tcp = ip.data
            if tcp.sport in ports or tcp.dport in ports:
                return True
            return False
        else:
            if verbose:
                print(f"ip is neither TCP nor UDP.")
            return False

    @staticmethod
    def get_smtp_details(ip, verbose=False):
        """
        This method returns the details of SMTP packet.
            parameters:
            - ip : packet of IP type. Instance of dpkt.ip.IP
            - verbose : print details or no
        
        returns:
            - 
        """
        if not SMTPUtils.is_smtp(ip):
            raise ValueError("Given packet is not SMTP packet.")
        tcp = ip.data
        if len(tcp.data):
            print(repr(tcp.data), len(tcp.data))
            # ON HOLD  till flow table gets done

    @staticmethod
    def hunt_credentials(ft, connection="all", verbose=False):
        """
        A very basic credentials miner from TCP/SMTP packet flow. Works on non SSL connections.
        parameters:
            - ft : FlowTable created from pyplico.flowtable
            - connection: String or List of Strings
                str  : key for connection in FlowTable
                list : list of keys in connection in FlowTable
                all  : default value mines all connections
            - verbose: bool
        """
        
        def _index_password_helper(__index, __flow):
            __creds = []
            for i in range(index, 0, -1):
                _flow_entity = __flow[i]
                if _flow_entity.tcp.data == smtp.PASSWORD_334:
                    _pass_flow_entity = __flow[i+1]
                    cred = dict()
                    _pass = _pass_flow_entity.tcp.data
                    _pass = _pass.decode()
                    _pass = _pass.replace("\n", "")
                    _pass = _pass.replace("\r", "")
                    cred["password"] = _pass
                    
                    for j in range(i, 0, -1):
                        _user_flow_entity = __flow[j]
                        if _user_flow_entity.tcp.data == smtp.USERNAME_334:
                            _user = __flow[j+1].tcp.data
                            _user = _user.decode()
                            _user = _user.replace("\n", "")
                            _user = _user.replace("\r", "")
                            cred["username"] = _user
                
                    __creds.append(cred)

            return __creds
        
        connections = ft.table.keys()
        if connection != "all":
            if isinstance(connection, list):
                connection = connection
            elif isinstance(connection, str):
                connection = [connection]
        credentials = []
        for _con in connections:
            _flow = ft.table.get(_con)
            if not _flow:
                continue
            for index in range(len(_flow)):
                if(_flow[index].tcp.data == smtp.AUTH_SUCCESS_235):
                    credentials.append(_index_password_helper(index, _flow))
        return credentials