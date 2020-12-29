import re
import time
from time import sleep
from PIL import Image
import sys

image = Image.open("resume.jpg")
image2 = Image.open("Pollo.JPG")
image3 = Image.open("load.JPG")
image4 = Image.open("congrats.jpg")
image2.show()


app = "Employment Application please fill what is needed in the bottom with other information needed!"

"""
pattern = re.compile(r"\w+ \w+ \w+ \w+ \w+ \w+ \w+")

matches = pattern.finditer(app)

for match in matches:
    print(match.group())
print("")

"""

print(''.join(re.findall("\w+ ", app)))


       
def decor(write):
    def wrap():
        print("-El Pollo Loco-")
        write()
        print("-Reno,Nv-")
    return wrap()
    
def print_text():
    print("Employment Application")
decorated = decor(print_text)
print("")


def decor(write):
    def wrap():
        print("Please see below!")   
        write()
        print("to upload resume please tap button if not proceed to type in resume manually")
    return wrap()
    
def print_text():
    print("Read instructions first!")
decorated = decor(print_text)
print("")



    
        
	
app = input('Would you want to upload your resume Yes/No?')	

def resume():
    if app == 'Yes':
    	print("Okay resume has been uploaded!")
    	image.show()
    	sys.exit()
    
    	
def name():
    if app == "No":
    	name = input("Input name here:")
    	return("Welcome sir we also request your age " + name + ".")
    
       
def number():
     number = input("Input age number here please to proceed:")
     print(number + " Age Verified proceed to input your social")
    
def social():
     social = input("Input SS number here please to complete first step:")
     print(social + " Thank you for your information please wait for step 2.")
     

       
def decor(write):
    def wrap():
        print("~~~Please complete first step~~~")
        write()
        print("~~~Please complete second step~~~")
    return wrap()
    
def print_text():
    print("~~~Thank you~~~")
decorated = decor(print_text)
print("")



    
#Function call
resume()
print("")
name()
print("")
number()
print("")
social()
print("")
#apply()




string_text = "Please fill out step."
print(' '.join(re.findall("\w+", string_text)))
print("")

employment = input("Please put your current or previous job here.")
print(employment + " - Add date from Start date till end date.")

class Mock():
    def __init__(self, app):
        self.app = app
        
    def template(self):
        employment_date = input(":")

mock = Mock("video")
mock.template()

class Mock2(Mock):
    def template2(self):
            print("Employment history verified please go ahead and put down any references")
        
mockk = Mock2("Game")
mockk.template2()

class Next(Mock):
    
    def template3(self):
        next = input(":")
    
x = Next("FallOut")
x.template3()
print("Wait for information to load...")
print("")

       
def decor(write):
    def wrap():
        print("---LOADING....---")
        write()
        print("---LOADING....---")
        image3.show()
    return wrap()
    
    
def print_text():
    print("~~~Thank you for your time applying~~~")
decorated = decor(print_text)
print("")

for i in range(0,5):
    print(5-i)
    sleep(1)
    if i == 5:
        print("Proceed to last step")
print("")
        
        
class Signature:
    
    def __init__(self,signature):
        self.signature = signature

     
    def LastStep(self):
        self.signature = input("Sign and date and applaction results vary on the information you put in thank you again for applying: ")
        print(self.signature)
        

        

laststep = Signature("RPM")
laststep.LastStep()
print("")


def decor(write):
    def wrap():
        print("Application complete")
        write()
        print("Thank you!")
        image4.show()
    return wrap()
    
def print_text():
    print("~~~ Application completed results may vary on the information you have inputted~~~")
decorated = decor(print_text)


        
        
    
        
        
        

        
    

        
    










    


