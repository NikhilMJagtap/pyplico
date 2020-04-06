import dpkt
from utils import get_headers

"""
PacketReader : Reads packets from specified file or interface. 
If file is specified, packets from .pcap files will be read.
If interface is specified, live packet will be captured from the interface.
Function stop_capture() must be called manually to stop the live packet capture.
"""
class PacketReader():

	"""
	parameters:
		- file (str) : .pcap file to read from 
		- interface (str) : interface ID to capture live packet from
		- to_itr (bool) : store packets in iterator
		- to_list (bool) : store packets in python list
		- verbose : print status to stdout

	"""

	def __init__(self, file=None, interface=None, to_itr=True, to_list=False, verbose=False):
		self.file = file
		self.interface = interface
		self.to_itr = to_itr
		self.to_list = to_list
		self.verbose = verbose
		if not file and not interface:
			raise ValueError("File or Network interface is required")
		elif file and interface:
			raise ValueError(f"Both file {file} and Network Interface {interface} specified.")
		elif file:
			try:
				f = open(file, 'rb')
			except:
				raise FileNotFoundError("File {file} not found!")
			if to_itr:
				pass
			elif to_list:
				self.packets = packets = self.read_packets(f)
			f.close()
		elif interface:
			# TODO: Live packet capture
			raise NotImplementedError("Live packet capture not implemented")
	

	"""
	parameters:
		- f : File (.pcap) reader
	return:
		- Python list of tuples. Each tuple has IP packet and timestamp
	"""

	def read_packets(self, f):
		packets = []
		pcaps = dpkt.pcap.Reader(f)
		total, skipped = 0, 0
		for timestamp, packet in pcaps:
			try:
				eth = dpkt.ethernet.Ethernet(packet)
				if not isinstance(eth.data, dpkt.ip.IP):
					skipped += 1
				else:
					ip = eth.data
					packets.append((ip, timestamp))
				total += 1
			except:
				# TODO:
				pass
		if self.verbose:
			print(f"Total {total} packets found. Using {total - skipped}.")
		return packets

	"""
	parameters:
		- f : File (.pcap) reader
	return:
		- iterator to IP packets
	"""
	# TODO: implement iterator for reading packets
	def read_itr(self, f):
		pass



def test():
	r = PacketReader(file="./data/sample.pcap", to_itr=False, to_list=True)
	print(get_headers(r.packets[0][0]))


if __name__ == "__main__":
	test() 
