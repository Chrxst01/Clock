zero = r"""
  __  
 /  \ 
| () |
 \__/ 

""".split("\n")
one = r"""
 _ 
/ |
| |
|_|
""".split("\n")
two = r"""
 ___ 
|_  )
 / / 
/___|
 
""".split("\n")
three = r"""
 ____
|__ /
 |_ \
|___/
 
""".split("\n")
four = r"""
 _ _  
| | | 
|_  _|
  |_| 
 
""".split("\n")
five = r"""
 ___ 
| __|
|__ \
|___/
 
""".split("\n")
six = r"""
  __  
 / /  
/ _ \ 
\___/ 
 
""".split("\n")
seven = r"""
 ____ 
|__  |
  / / 
 /_/  
 
""".split("\n")
eight = r"""
 ___  
( _ ) 
/ _ \ 
\___/ 
 
""".split("\n")
nine = r"""
 ___ 
/ _ \
\_, /
 /_/ 
 
""".split("\n")
colon = r"""  
(_)
   
 _ 
(_) 
""".split("\n")
import os, time
def clock():
  from datetime import datetime
  now = datetime.now()
  current_time = now.strftime("%H:%M")
  each = []
  for char in current_time:
    each.append(char)
  no1 = each[0]
  no2 = each[1]
  no3 = each[3]
  no4 = each[4]
  no1 = int(no1)
  if no1 == 1:
    first = one
  elif no1 == 2:
    first = two
  elif no1 == 3:
    first = three
  elif no1 == 4:
    first = four
  elif no1 == 5:
    first = five
  elif no1 == 6:
    first = six
  elif no1 == 7:
    first = seven
  elif no1 == 8:
    first = eight
  elif no1 == 9:
    first = nine
  elif no1 == 0:
    first = zero
  no2 = int(no2)
  if no2 == 1:
    second = one
  elif no2 == 2:
    second = two
  elif no2 == 3:
    second = three
  elif no2 == 4:
    second = four
  elif no2 == 5:
    second = five
  elif no2 == 6:
    second = six
  elif no2 == 7:
    second = seven
  elif no2 == 8:
    second = eight
  elif no2 == 9:
    second = nine
  elif no2 == 0:
    second = zero
  no3 = int(no3)
  if no3 == 1:
    third = one
  elif no3 == 2:
    third = two
  elif no3 == 3:
    third = three
  elif no3 == 4:
    third = four
  elif no3 == 5:
    third = five
  elif no3 == 6:
    third = six
  elif no3 == 7:
    third = seven
  elif no3 == 8:
    third = eight
  elif no3 == 9:
    third = nine
  elif no3 == 0:
    third = zero
  no4 = int(no4)
  if no4 == 1:
    fourth = one
  elif no4 == 2:
    fourth = two
  elif no4 == 3:
    fourth = three
  elif no4 == 4:
    fourth = four
  elif no4 == 5:
    fourth = five
  elif no4 == 6:
    fourth = six
  elif no4 == 7:
    fourth = seven
  elif no4 == 8:
    fourth = eight
  elif no4 == 9:
    fourth = nine
  elif no4 == 0:
    fourth = zero
  for row in zip(first, second, colon, third, fourth):
    print(row[0] + " " + row[1] + " " + row[2] + " " + row[3] + " " + row[4])