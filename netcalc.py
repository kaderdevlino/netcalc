#!/usr/bin/python3

#requirements: pip3 install termcolor ipaddress

import ipaddress

from netaddr import *

from termcolor import colored

 

# Computing the Network Addresses:

# Calculate the network address (@network ?)

# Calculate the broadcast address (@broadcast ?)

# calculate the first address (@first ?)

# calculate the last address (@last ?)

# Total addresses number (@ntotal ?)

# Addressable addresses (@addr)

# Division to subnets

# ..

 

IP = input(colored('Give IP Address with netmask like 192.168.1.2/24 to Calculate Network Addresses: ','blue'))

ip = IPNetwork(IP)

 

print (colored('Your IP is:','green'))

print (ip.ip,"=",ip.ip.bits())

 

print (colored('IP version is:','green'))

print ("IPv",ip.version)

 

print (colored('Is it Unicast?','green'))

print (ip.ip.is_unicast())

 

print (colored('Is it Multicast?','green'))

print (ip.ip.is_multicast())

 

print (colored('Is it Private?','green'))

print (ip.ip.is_private())

 

print (colored('Is it Public?','green'))

print (ip.ip.is_unicast() and not ip.ip.is_private())

 

print(colored('@Netmask is:','green'))

print(ip.netmask,"=",ip.netmask.bits())

 

print (colored('@Hostmask is:','green'))

print (ip.hostmask,"=",ip.hostmask.bits())

 

print (colored('@Network is:','green'))

print (ip.network,"=",ip.network.bits())

 

print (colored('@Broadcast is:','green'))

print (ip.broadcast,"=",ip.broadcast.bits())

 

print (colored('First address is:','green'))

print (ip[1],"=",ip[1].bits())

 

print (colored('Last address is:','green'))

print (ip[-2],"=",ip[-2].bits())

 

print (colored('Number of hosts:(Total addresses Number)','green'))

print (ip.size,"=",bin(ip.size))

 

print (colored('Addressable addresses:','green'))

print (ip.size-2,"=",bin(ip.size-2))

 

print (colored('@Subnets:','green'))

subnets=ip.subnet(26)

j=0

for i in subnets:

 j = j + 1

 print ('subnet',j,'is',i)

 

print (colored('Reverse IP lookups for DNS:','green'))

print (ip.ip.reverse_dns)
