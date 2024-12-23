import sys
import os 
import time
from collections import Counter

num_args = len(sys.argv)

"""
if num_args > 2:
   print("You have entered too many arguments...")
   exit(0)

if num_args < 2:
   print("You need to enter the filename you are checking")
   exit(0)
"""
try:
   filename = sys.argv[1]

   if not os.path.isfile(filename):
      print(f"[-] {filename} doesn't exist in this directory")
      exit(0)

   if not os.access(filename, os.R_OK):
      print(f"[-] {filename} has permission levels you don't have")

   print(f"'{filename}' is in the current working directory")

except:
   pass

pwd = os.getcwd()

# this will get both filenames and directories in the cwd
list_directory = os.listdir(pwd)

print(f"Your current directory is: {pwd}")
for item in list_directory:
   print(f"[+] {item}")

counts = Counter()

for currentdir, dirnames, filenames in os.walk("."):
   for filename in filenames:
      first_part, extension = os.path.splitext(filename)
      counts[extension] += 1

   for extension, count in counts.items():
      # print(f"running count: {counts.items()}")
      print(f"{extension:8}{count}")

path = os.getenv("PATH").split(";")
subgroups = {}
for item in path:
   parent_dir = item.split("\\")[1]

   if parent_dir in subgroups:
      subgroups[parent_dir] += 1
      continue

   subgroups[parent_dir] = 1

print(subgroups)

print("******* Now we will get some info on a file ********\n\n")

file = "port_scan.py"
file_stats = os.stat(file)

mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime = file_stats

print(f"Filename: {file}")
print(f"Created: {time.ctime(ctime)}")
print(f"File owner: \n\tgroup: {gid}\n\tuser: {uid}")
print(f"Mode: {oct(mode)}\n")

print("***** Checking file extension names ****\n\n")
extensions = [".jpeg", ".py", ".sample", ".git"]

for extension in extensions:
   print(f"Files with extension: {extension}:")

   for path, folder, files in os.walk("."):
      for file in files:
         if file.endswith(extension):
            print(os.path.join(path, file))