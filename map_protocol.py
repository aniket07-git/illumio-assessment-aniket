def get_protocol_name(protocol_number):
    protocol_map = {
        '0': 'HOPOPT',  # IPv6 Hop-by-Hop Option
        '1': 'ICMP',  # Internet Control Message Protocol
        '2': 'IGMP',  # Internet Group Management Protocol
        '3': 'GGP',  # Gateway-to-Gateway Protocol
        '4': 'IPv4',  # IPv4 encapsulation
        '5': 'ST',  # Stream Protocol
        '6': 'TCP',  # Transmission Control Protocol
        '7': 'CBT',  # CBT
        '8': 'EGP',  # Exterior Gateway Protocol
        '9': 'IGP',  # Interior Gateway Protocol
        '10': 'BBN-RCC-MON',  # BBN RCC Monitoring
        '11': 'NVP-II',  # Network Voice Protocol
        '12': 'PUP',  # PUP
        '13': 'ARGUS',  # ARGUS
        '14': 'EMCON',  # EMCON
        '15': 'XNET',  # Cross Net Debugger
        '16': 'CHAOS',  # Chaos
        '17': 'UDP',  # User Datagram Protocol
        '18': 'MUX',  # Multiplexing
        '19': 'DCN-MEAS',  # DCN Measurement Subsystems
        '20': 'HMP',  # Host Monitoring Protocol
        '21': 'PRM',  # Packet Radio Measurement
        '22': 'XNS-IDP',  # XEROX NS IDP
        '23': 'TRUNK-1',
        '24': 'TRUNK-2',
        '25': 'LEAF-1',
        '26': 'LEAF-2',
        '27': 'RDP',  # Reliable Data Protocol
        '28': 'IRTP',  # Internet Reliable Transaction Protocol
        '29': 'ISO-TP4',  # ISO Transport Protocol Class 4
        '30': 'NETBLT',  # Bulk Data Transfer Protocol
        '31': 'MFE-NSP',  # MFE Network Services Protocol
        '32': 'MERIT-INP',  # MERIT Internodal Protocol
        '33': 'DCCP',  # Datagram Congestion Control Protocol
        '34': '3PC',  # Third Party Connect Protocol
        '35': 'IDPR',  # Inter-Domain Policy Routing Protocol
        '36': 'XTP',  # XTP
        '37': 'DDP',  # Datagram Delivery Protocol
        '38': 'IDPR-CMTP',  # IDPR Control Message Transport Protocol
        '39': 'TP++',  # TP++ Transport Protocol
        '40': 'IL',  # IL Transport Protocol
        '41': 'IPv6',  # IPv6 encapsulation
        '42': 'SDRP',  # Source Demand Routing Protocol
        '43': 'IPv6-Route',  # Routing Header for IPv6
        '44': 'IPv6-Frag',  # Fragment Header for IPv6
        '45': 'IDRP',  # Inter-Domain Routing Protocol
        '46': 'RSVP',  # Reservation Protocol
        '47': 'GRE',  # Generic Routing Encapsulation
        '48': 'DSR',  # Dynamic Source Routing Protocol
        '49': 'BNA',  # BNA
        '50': 'ESP',  # Encap Security Payload
        '51': 'AH',  # Authentication Header
        '52': 'I-NLSP',  # Integrated Net Layer Security Protocol
        '53': 'SWIPE',  # IP with Encryption
        '54': 'NARP',  # NBMA Address Resolution Protocol
        '55': 'MOBILE',  # IP Mobility
        '56': 'TLSP',  # Transport Layer Security Protocol
        '57': 'SKIP',  # SKIP
        '58': 'ICMPv6',  # ICMP for IPv6
        '59': 'IPv6-NoNxt',  # No Next Header for IPv6
        '60': 'IPv6-Opts',  # Destination Options for IPv6
        '61': 'Host Internal Protocol',
        '62': 'CFTP',  # CFTP
        '63': 'Local Network',
        '64': 'SAT-EXPAK',  # SATNET and Backroom EXPAK
        '65': 'KRYPTOLAN',  # Kryptolan
        '66': 'RVD',  # MIT Remote Virtual Disk Protocol
        '67': 'IPPC',  # Internet Pluribus Packet Core
        '68': 'Distributed File System',
        '69': 'SAT-MON',  # SATNET Monitoring
        '70': 'VISA',  # VISA Protocol
        '71': 'IPCV',  # Internet Packet Core Utility
        '72': 'CPNX',  # Computer Protocol Network Executive
        '73': 'CPHB',  # Computer Protocol Heart Beat
        '74': 'WSN',  # Wang Span Network
        '75': 'PVP',  # Packet Video Protocol
        '76': 'BR-SAT-MON',  # Backroom SATNET Monitoring
        '77': 'SUN-ND',  # SUN ND PROTOCOL-Temporary
        '78': 'WB-MON',  # WIDEBAND Monitoring
        '79': 'WB-EXPAK',  # WIDEBAND EXPAK
        '80': 'ISO-IP',  # ISO Internet Protocol
        '81': 'VMTP',  # Versatile Message Transaction Protocol
        '82': 'SECURE-VMTP',  # Secure VMTP
        '83': 'VINES',  # VINES
        '84': 'TTP',  # TTP or IPTM
        '85': 'NSFNET-IGP',  # NSFNET-IGP
        '86': 'DGP',  # Dissimilar Gateway Protocol
        '87': 'TCF',  # TCF
        '88': 'EIGRP',  # EIGRP
        '89': 'OSPFIGP',  # OSPFIGP
        '90': 'Sprite-RPC',  # Sprite RPC Protocol
        '91': 'LARP',  # Locus Address Resolution Protocol
        '92': 'MTP',  # Multicast Transport Protocol
        '93': 'AX.25',  # AX.25 Frames
        '94': 'IPIP',  # IP-within-IP Encapsulation Protocol
        '95': 'MICP',  # Mobile Internetworking Control Protocol
        '96': 'SCC-SP',  # Semaphore Communications Sec. Protocol
        '97': 'ETHERIP',  # Ethernet-within-IP Encapsulation
        '98': 'ENCAP',  # Encapsulation Header
        '99': 'Private Encryption Scheme',
        '100': 'GMTP',  # GMTP
        '101': 'IFMP',  # Ipsilon Flow Management Protocol
        '102': 'PNNI',  # PNNI over IP
        '103': 'PIM',  # Protocol Independent Multicast
        '104': 'ARIS',  # ARIS
        '105': 'SCPS',  # SCPS
        '106': 'QNX',  # QNX
        '107': 'A/N',  # Active Networks
        '108': 'IPComp',  # IP Payload Compression Protocol
        '109': 'SNP',  # Sitara Networks Protocol
        '110': 'Compaq-Peer',  # Compaq Peer Protocol
        '111': 'IPX-in-IP',  # IPX in IP
        '112': 'VRRP',  # Virtual Router Redundancy Protocol
        '113': 'PGM',  # PGM Reliable Transport Protocol
        '114': '0-Hop Protocol',
        '115': 'L2TP',  # Layer Two Tunneling Protocol
        '116': 'DDX',  # D-II Data Exchange (DDX)
        '117': 'IATP',  # Interactive Agent Transfer Protocol
        '118': 'STP',  # Schedule Transfer Protocol
        '119': 'SRP',  # SpectraLink Radio Protocol
        '120': 'UTI',  # UTI
        '121': 'SMP',  # Simple Message Protocol
        '122': 'SM',  # Simple Multicast Protocol
        '123': 'PTP',  # Performance Transparency Protocol
        '124': 'ISIS over IPv4',  # IS-IS over IPv4
        '125': 'FIRE',  # Flexible Intra-AS Routing Environment
        '126': 'CRTP',  # Combat Radio Transport Protocol
        '127': 'CRUDP',  # Combat Radio User Datagram
        '128': 'SSCOPMCE',  # SSCOPMCE
        '129': 'IPLT',
        '130': 'SPS',  # Secure Packet Shield
        '131': 'PIPE',  # Private IP Encapsulation within IP
        '132': 'SCTP',  # Stream Control Transmission Protocol
        '133': 'FC',  # Fibre Channel
        '134': 'RSVP-E2E-IGNORE',  # RSVP-E2E-IGNORE
        '135': 'Mobility Header',  # Mobility Extension Header for IPv6
        '136': 'UDPLite',  # UDP-Lite
        '137': 'MPLS-in-IP',  # MPLS-in-IP
        '138': 'manet',  # MANET Protocols
        '139': 'HIP',  # Host Identity Protocol
        '140': 'Shim6',  # Shim6 Protocol
        '141': 'WESP',  # Wrapped Encapsulating Security Payload
        '142': 'ROHC',  # Robust Header Compression
        '143': 'Ethernet',  # Ethernet
        '144': 'AGGFRAG',  # AGGFRAG encapsulation payload for ESP
        '145': 'NSH',  # Network Service Header
        '146': 'Homa',  # Homa Protocol
        # Protocol numbers 147-252 are Unassigned
    }

    # Add 'Unassigned' protocols
    for unassigned_protocol in range(147, 255):
        protocol_map[str(unassigned_protocol)] = 'Unassigned'

    # Protocols 253 and 254 are for experimentation and testing
    protocol_map['253'] = 'Experimentation and Testing'
    protocol_map['254'] = 'Experimentation and Testing'
    # Protocol 255 is Reserved
    protocol_map['255'] = 'Reserved'

    # Normalize the protocol number to a string
    protocol_number = str(protocol_number)

    # Return the protocol name in lowercase to ensure case-insensitive matching
    return protocol_map.get(protocol_number, 'unknown').lower()
