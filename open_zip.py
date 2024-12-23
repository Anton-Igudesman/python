import zipfile
import os


extension = ".zip"
filename=""
for path, folder, files in os.walk("."):
   for file in files:
      if file.endswith(extension):
         filename = file

print(filename)

# this will iterate through all items in zip folder and give info
with zipfile.ZipFile(filename) as myzip:
   for zipinfo in myzip.infolist():
      print(zipinfo.filename.split("/")[-1])