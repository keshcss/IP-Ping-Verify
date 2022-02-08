#  A ping verifier for Class C IP networks

import os

x1 = int(input("Enter 1st bit: "))
x2 = int(input("Enter 2nd bit: "))
x3 = int(input("Enter 3rd bit: "))
x4 = int(input("Enter 4th bit: "))

X01 = str(x1)
X02 = str(x2)
X03 = str(x3)
X04 = str(x4)

print(X01+'.'+X02+'.'+X03+'.'+X04)

ips = [X01+'.'+X02+'.'+X03+'.'+X04,]


for i in range (1,255):
    x4 = x4 +1
    X04 = str(x4)
    ips.append(X01+'.'+X02+'.'+X03+'.'+X04)

print('list : ', ips)

for ip in ips:
    response = os.popen(f"ping {ip}").read()
    #  This line suggest that packets are exchanged, ping successful
    if "Minimum" in response:
        print(f"UP {ip} Ping Successful")
    #  This line suggest that there has been a request timeout, meaning target machine has firewall
    elif "Lost = 4" in response:
        print(f"UP {ip} Firewall UP")
    #  This line suggest that machine does not exist, ping unsuccessful
    else:
        print(f"DOWN {ip} PING FAILURE")