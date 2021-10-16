from pyplico.constants import ftp


class FTPUtils:
    @staticmethod
    def is_ftp(ip):
        ports = ftp.PORTS
        ftp_data = ip.data
        if ftp_data.dport in ports:
            return True
