#Writed by AxReal (Alexey Axenov) https://www.sololearn.com/Profile/5698359/?ref=app
"""
EasyPy_by_AxReal
To make it easy, save code to easypy.py and paste to top of your code: 'import easypy.py as easy'
Usage: easy.<method>, easy.<var>

**************************

Version 0.1.1:
*Added 3 input checks - float, int, bool.
*Added test method


"""

def test():
    print(intInput())
    print(floatInput())
    print(boolInput())
  
 
def intInput(msg='Enter Integer Number: ', err='Non-Integer value'):
  while True:
   try:
    inp = int(input(msg))
   except:
    print("\n"+err)
    continue 
   return inp
   
def floatInput(msg='Enter Float Number: ', err='Non-Float value'):
  while True:
   try:
    inp = float(input(msg))
   except:
    print(err)
    continue 
   return inp
   
def boolInput(msg='Enter Boolean value(true/false)(y/n): ', err='Unknown value'):
  while True:
   try:
    inp = input(msg)
    if inp.lower() == "true" or inp.lower() == 'y' or inp.lower() == "yes":
      return True
    elif inp.lower() == "false" or inp.lower() == 'n' or inp.lower() == "no":
      return False
    else:
      raise ValueError(err)
   except:
    print("\n"+err)
    continue 


if __name__=="__main__":
    test()
    