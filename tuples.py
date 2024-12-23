# dictionaries associate values with keys 

protocol_dict = {"FTP":21, "SMTP":25, "SSH":22, "HTTPS":443, "HTTP":80}

# several ways to create dicts in python
protocol_name = protocol_dict.keys()
protocol_port = protocol_dict.values()
print(protocol_name)
print(protocol_port)

protocol_dict_2 = dict( zip(protocol_name, protocol_port) )
print(protocol_dict_2)

http_port = protocol_dict.get("HTTP")
print(http_port)

icmp_port = protocol_dict.get("ICMP", "port information not found")
print(icmp_port)

protocol_dict["LDAP"] = 389
print(protocol_dict)

# looping through dicts and printing entries
for key, value in protocol_dict.items():
   print(f"Protocol: {key}, Port: {value}")

popped_protocol = protocol_dict.pop("LDAP", "value not present")
print(popped_protocol)

last_pop = protocol_dict.popitem()

print(last_pop)

