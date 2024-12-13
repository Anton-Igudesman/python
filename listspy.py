protocol_list = []
protocol_list.append("SFTP")
protocol_list.append("SMTP")
protocol_list.append("HTTPS")
protocol_list.append("Modbus")

# get index value of a list item
https_index = protocol_list.index("HTTPS")

print(f"This is my list {protocol_list}")

print(f"The HTTPS protocol is listed at index: {https_index}")

# printing all items in a list
for protocol in protocol_list:
   print(f"my favorite protocol might be {protocol}")

#adding many values at once
protocol_list.extend(["DNS", "FTP", "ICMP"])

print(f"new protocol list: {protocol_list}")

# adding at a specific location
protocol_list.insert(3, "DNP3")

print(protocol_list)

# 2 ways to reverse a list
protocol_list.reverse()

print(protocol_list)


protocol_list.reverse()
print(protocol_list)

# 2nd way will not mutate the actual list

print(protocol_list[::-1])
print(protocol_list)

# finding an element's index in a list 
element_to_find = "DNP3"
for i in range( len(protocol_list) ):
   if protocol_list[i] == element_to_find:
      print(f"{element_to_find} located at index: {i}")