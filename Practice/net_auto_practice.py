#this is a dict nested in a list

import ipaddress

interfaces = [ {"Interface": "Gi0/1", 
              "Status": "Up", 
              "Descripton": "HR-PC"
              },

              {"Interface": "Gi0/2",
               "Status": "Down",
               "Description": "Sales-PC"
              }
]



#retrieves first dict from list
print(interfaces[0])

#retrieves second dict from list
print(interfaces[1])

#ipaddress module 

my_ip = ipaddress.ip_address("192.168.254.33")


print(my_ip)