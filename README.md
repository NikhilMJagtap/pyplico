## A python port of Xplico using dpkt.
This repo is still under development. Please look at "developement" branch for latest work.

### Why pyplico
There are many tools available to do stuff with pcap files. I felt the need of a tool which can analyse packets in both code as well as GUI. While playing CTFs I knew that a good CTF tool like CyberChef is also needed. (Honestly, CyberChef is much better than what I am doing. xD)

### Components
- pyplico - A python package
- venom - A react app for my cryptographic needs
- API to catch pyplico from venom (Planning)


### Installation
```
virtualenv env
source env/bin/activate
pip install -r requirements
cd src
python setup.py install
```

### Example

Reading PCAP file and extracting SMTP Credentials
``` python
from pyplico.packetReader import PacketReader
pr = PacketReader("../src/data/smtp.pcap", to_itr=False, to_list=True)
ft = pr.get_flow_table()
creds = SMTPUtils.hunt_credentials(ft)
```