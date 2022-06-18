# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import hashlib
import random
import time

Stamp=time.time()
print(Stamp)
block=[]
# initializing string
str = "1"
block.append(Stamp)
block.append(int(str))
print(sum(block))
giving_input="{}".format(sum(block))

# encoding GeeksforGeeks using encode()
# then sending to SHA256()
result = hashlib.sha256(giving_input.encode())
  
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA256 is : ")
print(result.hexdigest())
random.seed(result.hexdigest())
print(random.random())
