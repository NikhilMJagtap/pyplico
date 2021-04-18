"""
Utilities to wrap various use cases of dpkt
"""


import dpkt
from dpkt.http import Message
import socket


"""
Convert mac address to str. Adopted from dpkt docs
	parameters:
		- mac () MAC address
	return:
		- (str) string representation of mac 
"""
def mac_addr_to_str(mac):
	return ':'.join('%02x' % dpkt.compat.compat_ord(b) for b in mac)


"""
Convert IP address to str. Adopted from dpkt docs
	parameters:
		- ip (IP) IP address
	return:
		- (str) string representation of ip
"""
def ip_addr_to_str(ip):
	try:
		return socket.inet_ntop(socket.AF_INET, ip)
	except ValueError:
		return socket.inet_ntop(socket.AF_INET6, ip)


"""
This function returns headers from the packet
	parameters:
		- ip (dpkt.ip.IP) : Packet of IP type. Instance of dpkt.ip.IP
		- verbose (bool) : Print headers to stdout
	return:
		- headers (dict) : Headers of the packet
"""
def get_headers(ip, verbose=False):
	if not isinstance(ip, dpkt.ip.IP):
		raise ValueError("Packet should be instance of dpkt.ip.IP")
	if not isinstance(ip.data, dpkt.tcp.TCP):
		raise ValueError("Packet is not TCP")
	# packet is marked as Do not Fragment 
	do_not_fragment = bool(ip.off & dpkt.ip.IP_DF)
	# Packet has more fragments i.e. not a last fragment
	more_fragments = bool(ip.off & dpkt.ip.IP_MF)
	# fragment offset
	fragment_offset = ip.off & dpkt.ip.IP_OFFMASK
	headers = {}
	headers["src_ip"] = ip_addr_to_str(ip.src)
	headers["dest_ip"] = ip_addr_to_str(ip.dst) 
	headers["len"] = ip.len
	headers["ttl"] = ip.ttl
	headers["dnf"] = do_not_fragment
	headers["mf"] = more_fragments
	headers["fo"] = fragment_offset
	if verbose:
		print(f"Source IP: {ip_addr_to_str(ip.src)}")
		print(f"Destintaion IP: {ip_addr_to_str(ip.dst)}")
		print(f"Length: {ip.len}  Time To Live: {ip.ttl}")
		print(f"DNF: {do_not_fragment}  MF: {more_fragments}  Fragment Offset: {fragment_offset}")
	return headers


"""
This function returns HTTP request of given package
	parameters:
		- ip (dpkt.ip.IP) : Packet of IP type. Instance of dpkt.ip.IP
		- verbose (bool) : Print headers to stdout
	return:
		- request (dict) : request of the packet
"""
def get_http_request(ip, verbose=False):
	if not isinstance(ip, dpkt.ip.IP):
		raise ValueError("Packet should be instance of dpkt.ip.IP")
	if not isinstance(ip.data, dpkt.tcp.TCP):
		raise ValueError("Packet is not TCP")
	tcp = ip.data
	# extracting request from TCP
	try: 
		request = dpkt.http.Request(tcp.data)
	except dpkt.dpkt.UnpackError:
		raise ValueError("Malformed packet. Failed to extract request")
	request_dict = {}
	request_dict["method"] = request.method
	request_dict["uri"] = request.uri
	request_dict["version"] = request.version
	request_dict["protocol"] = "HTTP"
	msg = Message.__str__(request)
	request_dict["message"] = msg
	if verbose:
		print(f"Protocol: HTTP  Version: {request.version}")
		print(f"URI: {request.uri}")
		print(f"Method: {request.method}")
		print(f"Message: {msg}")
	return request_dict


def test():
	pass

if __name__ == "__main__":
	test()