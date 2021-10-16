import dpkt


class HTTPUtils:

    @staticmethod
    def is_http(ip, verbose=False):
        """
            This function returns whether the packet was an HTTP request packet or not

            parameters:
                - ip : packet of IP type. Instance of dpkt.ip.IP
                - verbose : print details or no

            returns:
                - bool: true if ip is HTTP else false
        """

        tcp = ip.data

        # See if we can parse the contents as a HTTP request
        try:
            request = dpkt.http.Request(tcp.data)
        except (dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError):
            return False

        return True

    @staticmethod
    def get_user_agent(ip):
        """
        This function returns the user-agent/browser-info if request is http

        :param ip:
        :return: user-agent/browser-info

        """
        if HTTPUtils.is_http(ip):
            tcp = ip.data
            request = dpkt.http.Request(tcp.data)
            headers = request.headers
            user_agent = headers.get('user-agent')

            return user_agent

        else:
            return None


