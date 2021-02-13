const sidebaroptions = [
    {
        name: 'pyPlico',
        selected: true,
        logoURL: "https://www.flaticon.com/svg/static/icons/svg/2406/2406415.svg",
        suboptions: ['pcap', 'FTP', 'DNS', 'UDP', 'Sniffer']
    },
    {
        name: 'Crypto', 
        selected: false, 
        logoURL: "https://www.flaticon.com/svg/static/icons/svg/748/748150.svg",
        suboptions:['Base64 Decode', 'Base64 Encode', 'Vigenere Decode', 'Vigenere Encode', 'DES', 'AES']
    },
    {
        name: 'Hash', 
        selected: false,
        logoURL: "https://www.flaticon.com/svg/static/icons/svg/1296/1296416.svg",
        suboptions:['MDX', 'SHA Family', 'RIPEMD', 'BCrypt']
    },
    {
        name: 'SQL', 
        selected: false,
        logoURL: "https://www.flaticon.com/svg/static/icons/svg/957/957811.svg",
        suboptions:['Injection', 'Scan', 'Query']
    },
    {
        name: 'Stegano', 
        selected: false,
        logoURL: "https://www.flaticon.com/premium-icon/icons/svg/1674/1674726.svg"
    },
    {
        name: 'Tools',
        selected: false,
        logoURL: "https://www.flaticon.com/svg/static/icons/svg/3747/3747894.svg",
        suboptions:['Traceroute', 'DNS-Lookup']
    },
]

export default sidebaroptions;