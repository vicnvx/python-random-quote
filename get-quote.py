import random
import re

def first():
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  
  
  last = len(quotes) - 1
  print(adjust(quotes[rnd(last)]), adjust(quotes[rnd(last)]))

def rnd(x):
  return random.randint(0, x)

def adjust(x):
  result = re.sub('\\n', '', x)
  return result
  
if __name__== "__main__":
  first()
