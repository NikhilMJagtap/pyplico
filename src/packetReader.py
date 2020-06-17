import dpkt
import types
from smtp_utils import SMTPUtils
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
				self.packets_itr = packets_itr = self.read_itr(f)
			elif to_list:
				self.packets = packets = self.read_packets(f)
				f.close()

		# TODO: Live packet capture
		elif interface:
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
			except dpkt.dpkt.UnpackError:
				continue

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
		pcaps = dpkt.pcap.Reader(f)
		try:
			for timestamp, packet in pcaps:
				try:
					eth = dpkt.ethernet.Ethernet(packet)
					if not isinstance(eth.data, dpkt.ip.IP):
						continue
					else:
						ip = eth.data
						yield (ip, timestamp)

				except dpkt.dpkt.UnpackError:
					if self.verbose:
						print("Failed to Unpack the packet. Sending next packet.")
					continue

		# This try catch is to supress the ValueError raised in dpkt. Specifically in dpkt/pcap.py
		# while reading. The error says 'read from closed file'. Checked GitHub repo of dpkt. 
		# Will try to fix this.
		
		except ValueError:
			pass
	
	"""
	Getter function for packet generator
	parameters:
		-
	returns:
		- Generator if found else None
	"""
	def get_itr(self):
		try:
			if isinstance(self.packets_itr, types.GeneratorType):
				return self.packets_itr
			else:
				return None
		except AttributeError:
			raise ValueError(f"{self.__class__.__name__} was not initialised using to_itr")
		


"""
Test function
"""

def test():
	r = PacketReader(file="./data/sample.pcap", to_itr=False, to_list=True)
	for packet in r.packets:
		if SMTPUtils.is_smtp(packet[0]):
			print("SMTP")
			break



if __name__ == "__main__":
	test() 
	# tested for udp utils
	# tested for iter
	# tested for utils
	# tested for packet reader