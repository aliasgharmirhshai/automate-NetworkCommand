import os
import sys

host = sys.argv[1]

if 'http' in host:
    print("Dont Enter Https or Http")
else:
    for i in range(1,54):
        get_ttl = os.popen(f"ping {host} -i {i} -n 1").read().split()
        ping = get_ttl[12]
        ip = get_ttl[2]
        expire_ip = get_ttl[10]
        
        if 'in' in get_ttl[13]:
            print(f"EXPIERD = {i} * On = {expire_ip}")
        elif 'for' in get_ttl[13]:
            print("TIMEOUT = ", i)
        elif 'TTL' in get_ttl[13]:
            print(f'\nPacket Time To Live(TTL) = {i} * PING = {ping} * IP = {ip}')
            break
        else:  
            print(get_ttl[13])
  