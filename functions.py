dictionary = {1:100, 2:200, 3:300, 4:400}

def find_item(dict, item):
   for key, value in dict.items():
      if item == value:
         print(f"key is {key} and it goes with {item}")

find_item(dictionary, 200)