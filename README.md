# Disclaimer
Please do not perform this action if unauthorized! This might get you in serious trouble! This is for educational purposes only. Enjoy programming!

# IP-Ping-Verify
Want to know every device which is connected to the Router (Class C network) ? and that using Python Language? Well I've got you covered here. 

Libraries Used : os

## How It Works
- Enter the Network's IP bit by bit in 4 parts. Example :
    - Enter 1st bit : 192
    - Enter 2nd bit : 168
    - Enter 3rd bit : 1
    - Enter 4th bit : 1
    - Final Output : 192.168.1.1
- After this , a list is created.
- Since we want all the devices IP connected to the particular router or network, set the for loop range(1,255)
- What it means : It will append IPs starting from 192.168.1.2 to 192.168.1.255 to the list automatically
- Great! Now we have all the available IPs to Ping. Whats next?
- This program will ping all the given IPs in the List and will give you 1 in 3 outcomes for each line.
    - Outcome 1 : A successful ping
        - When a ping is successful, the outcome will often be this :
        - Ping statistics for 192.168.1.1:
          Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
          Approximate round trip times in milli-seconds:
          Minimum = 7ms, Maximum = 31ms, Average = 15ms
        - If the word minimum is included, the ping is successful
    - Outcome 2 : Request Timeout
        - When Request Timeout on the network that you are on, this means that there is no response.
        - No response doesnt mean the IP address is vacant! This just means that there are firewalls in place on the machine occupying this IP.
        - The outcome will look like this:
          Ping statistics for 192.168.50.42:
          Packets: Sent = 4, Received = 0, Lost = 4 (100% loss),
        - In this case, if Loss = 4, Machine is up with an active Firewall
    - Outcome 3 : Host is unreachable
        - When host is unreachable, it means that the address does not exist. Or in simple words, no machone is occupying the address. The outcome will look like this:
        - Ping statistics for 192.168.50.2:
          Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
        - In this case if Loss = 0, Host is unreachable
- Now that we have gotten all the outcome, we can do a "arp-a" command in our command prompt/terminal/windows powershell.
- This will list the IPs discovered (Successful Ping and Request Timeout) , and its subsequent MAC address       
