import netifaces
import ipaddress


"""Last login: Thu Mar  9 16:15:04 on ttys001
harrennix@Harrens-MacBook ~ % ifconfig -a
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
	options=1203<RXCSUM,TXCSUM,TXSTATUS,SW_TIMESTAMP>
	inet 127.0.0.1 netmask 0xff000000 
	inet6 ::1 prefixlen 128 
	inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1 
	nd6 options=201<PERFORMNUD,DAD>
gif0: flags=8010<POINTOPOINT,MULTICAST> mtu 1280
stf0: flags=0<> mtu 1280
en5: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	ether ac:de:48:00:11:22 
	inet6 fe80::aede:48ff:fe00:1122%en5 prefixlen 64 scopeid 0x4 
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect (100baseTX <full-duplex>)
	status: active
ap1: flags=8802<BROADCAST,SIMPLEX,MULTICAST> mtu 1500
	options=400<CHANNEL_IO>
	ether 36:7d:da:39:b5:36 
	media: autoselect
en1: flags=8963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1500
	options=460<TSO4,TSO6,CHANNEL_IO>
	ether 82:af:ec:24:c4:01 
	media: autoselect <full-duplex>
	status: inactive
en2: flags=8963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1500
	options=460<TSO4,TSO6,CHANNEL_IO>
	ether 82:af:ec:24:c4:00 
	media: autoselect <full-duplex>
	status: inactive
en4: flags=8963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1500
	options=460<TSO4,TSO6,CHANNEL_IO>
	ether 82:af:ec:24:c4:04 
	media: autoselect <full-duplex>
	status: inactive
en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=6463<RXCSUM,TXCSUM,TSO4,TSO6,CHANNEL_IO,PARTIAL_CSUM,ZEROINVERT_CSUM>
	ether 14:7d:da:39:b5:36 
	inet6 fe80::1004:de41:2852:c2%en0 prefixlen 64 secured scopeid 0x9 
	inet 192.168.10.193 netmask 0xffffff00 broadcast 192.168.10.255
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect
	status: active
en3: flags=8963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1500
	options=460<TSO4,TSO6,CHANNEL_IO>
	ether 82:af:ec:24:c4:05 
	media: autoselect <full-duplex>
	status: inactive
awdl0: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=6463<RXCSUM,TXCSUM,TSO4,TSO6,CHANNEL_IO,PARTIAL_CSUM,ZEROINVERT_CSUM>
	ether 06:19:8b:3e:e8:c0 
	inet6 fe80::419:8bff:fe3e:e8c0%awdl0 prefixlen 64 scopeid 0xb 
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect
	status: active
bridge0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=63<RXCSUM,TXCSUM,TSO4,TSO6>
	ether 82:af:ec:24:c4:01 
	Configuration:
		id 0:0:0:0:0:0 priority 0 hellotime 0 fwddelay 0
		maxage 0 holdcnt 0 proto stp maxaddr 100 timeout 1200
		root id 0:0:0:0:0:0 priority 0 ifcost 0 port 0
		ipfilter disabled flags 0x0
	member: en1 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 6 priority 0 path cost 0
	member: en2 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 7 priority 0 path cost 0
	member: en3 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 10 priority 0 path cost 0
	member: en4 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 8 priority 0 path cost 0
	nd6 options=201<PERFORMNUD,DAD>
	media: <unknown type>
	status: inactive
llw0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=400<CHANNEL_IO>
	ether 06:19:8b:3e:e8:c0 
	inet6 fe80::419:8bff:fe3e:e8c0%llw0 prefixlen 64 scopeid 0xd 
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect
	status: inactive
utun0: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 1380
	inet6 fe80::8140:9e48:58b8:6d50%utun0 prefixlen 64 scopeid 0xe 
	nd6 options=201<PERFORMNUD,DAD>
utun1: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 2000
	inet6 fe80::1f44:e74:d00c:7b7f%utun1 prefixlen 64 scopeid 0xf 
	nd6 options=201<PERFORMNUD,DAD>
utun2: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 1000
	inet6 fe80::ce81:b1c:bd2c:69e%utun2 prefixlen 64 scopeid 0x10 
	nd6 options=201<PERFORMNUD,DAD>
utun3: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 1380
	inet6 fe80::1e53:f57d:71ce:d66e%utun3 prefixlen 64 scopeid 0x11 
	nd6 options=201<PERFORMNUD,DAD>
utun4: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 1380
	inet6 fe80::2fe2:f2c:2aa9:b932%utun4 prefixlen 64 scopeid 0x12 
	nd6 options=201<PERFORMNUD,DAD>
utun5: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 1380
	inet6 fe80::f5a3:f80b:4a1f:86b7%utun5 prefixlen 64 scopeid 0x15 
	nd6 options=201<PERFORMNUD,DAD>
utun6: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 1380
	inet6 fe80::d2ca:84f3:6a62:af45%utun6 prefixlen 64 scopeid 0x16 
	nd6 options=201<PERFORMNUD,DAD>
en7: flags=8822<BROADCAST,SMART,SIMPLEX,MULTICAST> mtu 1500 constrained
	options=400<CHANNEL_IO>
	ether ea:5f:02:88:e3:6b 
	media: autoselect <full-duplex>
	status: inactive
en6: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=400<CHANNEL_IO>
	ether ea:5f:02:88:e3:94 
	inet6 fe80::459:1d51:b99c:4070%en6 prefixlen 64 secured scopeid 0x18 
	inet 169.254.29.245 netmask 0xffff0000 broadcast 169.254.255.255
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect (100baseTX <full-duplex>)
	status: active
en8: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=400<CHANNEL_IO>
	ether 2e:8c:66:6b:36:c3 
	inet6 fe80::2c8c:66ff:fe6b:36c3%en8 prefixlen 64 scopeid 0x19 
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect
	status: active
harrennix@Harrens-MacBook ~ % 
"""
netiface = netifaces.interfaces()
keys = {}

#all interfaces on host
def get_interfaces():
    print('The interfaces are : \n')
    return netifaces.interfaces()


def get_mac(interface):
    getMacAdd= {}
    for i in netiface:
        addrs = netifaces.ifaddresses(i)
        getMacAdd = addrs[netifaces.AF_LINK][0]['addr']
        if getMacAdd== "":
            pass
        else:
            getMacAdd[i] = keys

    addrs = netifaces.ifaddresses(interface)

    print('the mac adress of' + interface + 'is: ' + mkeys[interface])

def get_ips(interface):
    ip_dict = {}
    try:

        addrs = netifaces.ifaddresses(interface)
        ipv4 = addrs[netifaces.AF_INET]
        ipv4i = ipv4[0]['addr']
        # print(ipv4i)
        ip_dict['v4'] = ipv4i
    except:
        print('does not have ipv4')

    try:
        addrs = netifaces.ifaddresses(interface)
        ipv6 = addrs[netifaces.AF_INET6]
        ipv6i = ipv6[0]['addr']
        ip_dict['v6'] = ipv6i
    except:
        print('does not have ipv6')

    print("the ip addresses are: ")
    print(ip_dict)


# netmask
def get_netmask(interface):
    netmask = {}
    addrs = netifaces.ifaddresses(interface)
    try:

        addrs = netifaces.ifaddresses(interface)
        print('does not have ipv6')
        print("the ip addresses are: ")

        ipv4 = addrs[netifaces.AF_INET]
        ipv4i = ipv4[0]['netmask']
        netmask['v4'] = ipv4i
    except:
        print()

    try:
        addrs = netifaces.ifaddresses(interface)
        ipv6 = addrs[netifaces.AF_INET6]
        ipv6i = ipv6[0]['netmask']
        netmask['v6'] = ipv6i
    except:
        print()
    print("the netmasks are; ")
    print(netmask)

def get_network(interface):
    network = {}
    addrs = netifaces.ifaddresses(interface)
    try:

        addrs = netifaces.ifaddresses(interface)
        ipv4 = addrs[netifaces.AF_INET]
        ipv4i = ipv4[0]['netmask']
        # print(ipv4i)
        network['v4'] = ipv4i
    except:
        print()

    try:
        addrs = netifaces.ifaddresses(interface)
        ipv6 = addrs[netifaces.AF_INET6]
        ipv6i = ipv6[0]['broadcast']
        network['v6'] = ipv6i
    except:
        print()

    print(network)


print(get_interfaces())

net = input("which one would you like to examine:")

get_mac(net)

get_ips(net)

get_netmask(net)

get_network(net)