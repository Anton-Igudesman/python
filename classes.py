class Protocol:

   # constructor
   def __init__(self, name, port, description):
      self.name = name
      self.port = port 
      self.description = description 

   # string representation of the protocol
   def __str__(self):
      result = (f"Protocol: {self.name}\n"
                f"Port: {self.port}\n"
                f"Description: {self.description}"
      )
      return result

   # getters
   @property
   def name(self):
      return self.__name
   @property
   def port(self):
      return self.__port
   @property
   def description(self):
      return self.__description
   
   # setters
   @name.setter
   def name(self, name):
      # making sure protocol name is one work
      if " " in name:
         raise ValueError("Protocol must be one word")
      
      self.__name = name

   @port.setter
   def port(self, port):
      if not (0 <= port <= 65535):
         raise ValueError("This is not a valid port number")
      
      self.__port = port
      
   @description.setter
   def description(self, description):
      if len(description) > 1000:
         raise ValueError("Please provide a shorter description")
      
      self.__description = description

valid_protocol = False

try:
   http = Protocol("HTTP", 80, "This is a basic web browsing protocol")
   valid_protocol = True

except ValueError as e:
   print(f"You've got an error bro: {e}")

if valid_protocol:
   print(http)


   

