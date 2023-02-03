import os
import sys

def command_handler():
    host = sys.argv[2]

    if sys.argv[1] == "-P":
        ping(host)
    elif sys.argv[1] == '-Ps':
        packet_size(host)
    else:
        print("Command Not Found")

def ping(host):
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

def packet_size(host):
    for i in range(0,5000, 100):
        get_size = os.popen(f"ping {host} -l {i}").read().split()
        ip = get_size[2]
        time = get_size[12]
        timeout = get_size[13]
        
        if timeout == 'out.':
            print(f"\nEnd Sending Packet in {i}Byte")
            break
        else:
            print(f"{ip}   PACKET SZIE = {i}Byte   {time}")

if __name__ == '__main__':
    try:
        command_handler()
    except KeyboardInterrupt:
        print('\nGoodBy...')