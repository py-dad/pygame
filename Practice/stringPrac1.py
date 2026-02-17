

output = """Gi1/0/1  connected  41  a-full  a-100  10/100/1000BaseTX CONNECTED_TO_SOMETHING 
          Gi1/0/2 notconnect 41 a-full a-100 10/100/1000BaseTX CONNECTED_TO_PRINTER"""

vlan_ports = {}

for line in output.splitlines():
    fields = line.split() # Splits line into words (fields)
    if len(fields) >= 3 and fields[2] == "41":
        iface = fields[0]
        status = fields[1]
        vlan = fields[2]
        desc = fields[6]

    print(iface)
    print(status)
    print(vlan)

        
    vlan_ports[iface] = {    # Value in bracket is key
           #"interface": iface,
           "status": status,
           "vlan": vlan,
           "description": desc
       }


print(vlan_ports)