import argparse

def parse_ports(port_list):
   parsed_ports = set() # will store single ports in a set to remove duplicates

   ports = port_list.split(',')

   for port in ports:

      # handle port ranges and add each individually
      if '-' in port:
         first_port, last_port = map( int, port.split('-') )

         # validating entries
         if first_port > last_port:
            raise argparse.ArgumentTypeError(
               f"Invalid range: {port} - must be ascending"
               )
         
         parsed_ports.update( range(first_port, last_port + 1) )

      else: # handling single port entries
         parsed_ports.add( int(port) )
   
   return sorted(parsed_ports)
         # add each port number in the range to the port set

description = """
Use Cases:
   + Basic scan:
      -t 127.0.0.1
   
   + Specific port:
      -t 127.0.0.1 -p 21
   
   + Port list:
      -t 127.0.0.1 -p 21,22
         --- or ---
      -t 127.0.0.1 -p 21-24,26,29,36-49
   
   + Only show open ports:
      -t 127.0.0.1 --open
      """
parser = argparse.ArgumentParser(
   description="Port scanning",
   epilog=description,
   formatter_class=argparse.RawDescriptionHelpFormatter
)

parser.add_argument(
   "-t", "--target",
   metavar="TARGET ADDRESS",
   help="Target to scan",
   required=True
)

parser.add_argument(
   "-p", "--ports",
   help="Specify target ports separated by comma or dashed range",
   default="80,8080",
   type=parse_ports
)

parser.add_argument(
   "-o", "--open",
   action="store_true",
   help="Display only open ports"
)

# parse the arguments added
params = parser.parse_args()

print(params.ports)