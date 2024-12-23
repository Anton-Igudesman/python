import argparse
import os
from time import sleep

MAX_VERBOSITY = 2
MIN_VERBOSITY = 1

def raise_to_power(base: int, exp: int):
   result = base

   for i in range(1,exp):
      result *= base

   return result

def compute_visual():
   print(".", end="", flush=True)
   sleep(.4)
   print(".", end="", flush=True)
   sleep(.4)
   print(".", end="", flush=True)
   sleep(.4)
   print(".", end="", flush=True)
   sleep(.4)
   print(".", flush=True)



# setting up parser object
parser = argparse.ArgumentParser(
   description = "Will take x and raise to the power of Y"
)
logging_group = parser.add_mutually_exclusive_group()
logging_group.add_argument(
   "-v", "--verbose", 
   help="display detailed logging info", 
   action="count",
   )
logging_group.add_argument(
   "-q", "--quiet",
   help="minimal logging info - this flag takes no arguments",
   action="store_true"
)

"""
adding  command-line options the program will accept
- these will now show on the help screen 
"""

# this is our only required positional argument so far
parser.add_argument(
   "x", 
   type=int, 
   help="the base", 
   )

parser.add_argument(
   "y",
   type=int,
   help="the exponent"
)

parser.add_argument(
   "-e", "--echo", 
   help="echo the string you use here"
   )



args = parser.parse_args()
answer = raise_to_power(args.x, args.y)

# we are defining the optional and positional arguments here 
if args.echo:
   print(args.echo)

# if args.square:
   # args.square *= args.square
   # print(args.square)

if args.verbose and args.verbose > MAX_VERBOSITY:
   string = (
      f"The max verbosity level available is {MAX_VERBOSITY}\n"
      f"Logging at this level\n"
   )
   print(string)

   # change verbose to match MAX_VERBOSITY
   args.verbose = MAX_VERBOSITY

if args.verbose == MAX_VERBOSITY:
   print(f"***Max logging enabled***\n")
   print(f"Running: '{os.path.basename(__file__)}'", end="")
   compute_visual()
   print(f"{args.x} raised to the power {args.y} is {answer}")

if args.verbose == MIN_VERBOSITY:
   print(f"{args.x}^{args.y} = {answer}")

if args.quiet:
   print(answer)
   

