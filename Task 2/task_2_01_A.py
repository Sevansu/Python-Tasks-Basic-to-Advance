#1. Create two python files. say 'task_2_01_A.py' and 'task_2_01_B.py'. Create a class in the 'task_2_01_A.py' having some attributes and functions and constructor defined in the class. Create a method outside that class in the file 'task_2_01_A.py'. Use that class and its attributes and mehtods and the method that is defined outside the class in the file 'task_2_01_B.py'.

class SimpleInterest:  
    #variables 
    m = "" 
    p = 0  
    r = 0 
    t = 0 
      
    #constructor  
    def __init__(self, Message, PrincipleAmount, RateOfInterest, Time):  
        self.m = Message
        self.p = PrincipleAmount  
        self.r = RateOfInterest
        self.t = Time
 
    #class methods 
    def showMessage(self):  
        print(self.m) 
    def InterestGenerator(self):
        x = (self.p*self.r*self.t)/100
        print(x)  

person1 = SimpleInterest(Message="seva", PrincipleAmount=60000, RateOfInterest=2, Time=2)
person2 = SimpleInterest(Message="nsu", PrincipleAmount=100000, RateOfInterest=3, Time=5) 
person1.showMessage()
person1.InterestGenerator()
person2.showMessage()
person2.InterestGenerator()