# example of raising exception in the subprocess arguments

import subprocess 
import os
import sys 

try:
   process = subprocess.run( 
      ('cmd', '/C', 'dir /S /B open_zip.py'), 
      stdout = subprocess.PIPE,
      check = True)
   
   directory, filename = os.path.split(process.stdout)

   print( directory.decode() )
except subprocess.CalledProcessError as error:
   print("Error: ", error)

"*** Now we can try executing a child process ***"
print(sys.platform)

print("Listing the files in this directory:")
print(subprocess.call(['ls', '-la']))

print("*** Sending ping with subprocess module ***")

command_ping = "ping"
ipv4 = "-4"
ping_parameter = "-w 2"
domain = "espn.com"

p = subprocess.Popen(
   [command_ping, ipv4, domain],
   shell = False,
   stderr = subprocess.PIPE
)

out = p.stderr.read(1)
sys.stdout.write( out.decode() )
sys.stdout.flush()

print("Now scanning a range of IP addresses...")

for ip in range(1, 255):
   ip_address = f"10.10.10.{ip}"
   print(f"Scanning {ip_address}")

   p = subprocess.Popen(
      [command_ping, "-c", "1", "-w", "4", ip_address],
      stdin=subprocess.PIPE,
      stdout=subprocess.PIPE,
      stderr=subprocess.PIPE,
   )

   stdout, stderr = p.communicate()
   print( stdout.decode('utf-8') )

   if b"bytes from " in stdout:
      print(f"{ip_address} has responded with an ECHO_REPLY!!")


