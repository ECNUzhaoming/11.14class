
# coding: utf-8

# In[3]:

class Calculator:
    def calculate(self,expression):
        return eval(expression)
    
class Talker:
    def talk(self,value):
        print("My value is",value)
    
class TalkingCalculator(Calculator):
    def __init__(self):
        self.__talker=Talker()
        self.__value=None
        
    def talk(self):
        self.__talker.talk(self.__value)
        
    def calculate(self,expression):
        self.__value=Calculator.calculate(self,expression)
        
        
tc=TalkingCalculator()
tc.calculate("1+2+3")
tc.talk()


# In[9]:

class Screwdriver:
    def screw(self):
        print("screwing...")
        
class knife:
    def cut(self):
        print("cutting")
        
class SwissKnife(Screwdriver,knife):
    pass

sk=SwissKnife()
sk.screw()
sk.cut()


# In[8]:

class Screwdriver:
    def __init__(self,size):
        self.size=size
    def screw(self):
        print("screwing{}".format(self.size))
        
class knife:
    def cut(self):
        print("cutting")
        
class SwissKnife(Screwdriver,knife):
    def __init__(self,size):
        Screwdriver.__init__(self,size)
        knife.__init__(self)

sk=SwissKnife(4)
sk.screw()
sk.cut()


# In[10]:

class Screwdriver:
    def __init__(self,size):
        self.size=size
    def screw(self):
        print("screwing{}".format(self.size))
        
class knife:
    def cut(self):
        print("cutting")
        
class SwissKnife(Screwdriver,knife):
    def __init__(self,Screwdriver_size):
        Screwdriver.__init__(self,Screwdriver_size)
        knife.__init__(self)

sk=SwissKnife(4)
sk.screw()
sk.cut()


# In[19]:

class Screwdriver:
    def __init__(self,size):
        self.size=size
        
    def screw(self):
        print("screwing{}".format(self.size))
        
class knife:
    def cut(self):
        print("cutting")
        
class SwissKnife(Screwdriver,knife):
    def __init__(self):
        self.tools={}
        
    def add_tool(self,name,tool):
        self.tools[name]=tool
        
    def use_tool(self,name):
        pass
    
    

sk=SwissKnife()
sk.add_tool("knife",knife())
sk.add_tool("big_screwdriver",Screwdriver(2))
sk.add_tool("small_screwdriver",Screwdriver(3))
sk.use_tool("knife")
sk.use_tool("big_screwdriver")
sk.use_tool("small_screwdriver")


# In[20]:

knife=knife()
hasattr(knife,"work")


# In[21]:

#鉴别是不是函数
callable(getattr(knife,"cut"))


# In[22]:

setattr(knife,"work",None)
hasattr(knife,"work")


# In[23]:

callable(getattr(knife,"work"))


# In[24]:

#abc模块
from abc import ABC,abstractmethod

class Tool(ABC):
    @abstractmethod
    def work(selk):
        pass
tool=Tool()


# In[28]:

from time import sleep
import random

class Bar:
    __empty="-"
    def __init__(self,length=80):
        self.bar=list()
        for i in range(0,length):
            self.bar.append(Bar.__empty)
            
    def reset(self):
        for i in range(len(self.bar)):
            self.bar[i]=Bar.__empty
            
    def update(self,ants):
        self.reset()
        for ant in ants:
            if 0<=ant.position<len(self.bar):
                self.bar[ant.positon]=ant.symbol
                
    def is_empty(self):
        for item in self.bar:
            if not item==Bar.__empty:
                return False
        else:
            return True
    
    def  show(self):
        for ch in self.bar:
            print(ch,sep="",end="")
        print("",end="/r")
            
class Ant:
    symbols="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    count=0
    def __init__(self,position,direction,symbol="*"):
        self.position=position
        self.direction=direction
        if symbol is None:
            self.symbol=Ant.symbols[Ant.count]
            count+=1
        else:
            self.symbol=symbol
        
    def move(self):
        self.positon+=self.direction
        
    def creat_random_ant(length=80):#工厂方法，用来生成类的对象
        position=random.randint(0,length-1)#前后都是闭区间
        direction=random.choice([1,-1])
        return Ant(position,direction)

    def get_ant(self):
        return set.ants
    
bar=Bar(80)
ants=Ants(5)

bar.update(ants.get_ants())
bar.show()

while not bar.is_empty():
    sleep(0.25)
    ants.move()
    bar.update(ants.get_ants())
    bar.show()


# In[29]:

1/0


# In[30]:

raise Exception


# In[31]:

raise Exception("system false")


# In[33]:

class MyException(Exception):pass

raise MyException()


# In[36]:

try:
    x=int(input("Please input a number"))
    y=int(input("Please input a number"))
    print("{}/{}={}".format(x,y,x/y))
except ZeroDivisionError:
    print("The second number can't be 0")


# In[43]:

def calc(expression,no_throw=False):
    try:
        return eval(expression)
    except ZeroDivisionError:
        if no_throw:
            print("Division by Zero")
        else: raise
            
calc("3/0",True)
    


# In[46]:

try:
    x=int(input("Please input a number"))
    y=int(input("Please input a number"))
    print("{}/{}={}".format(x,y,x/y))
except ZeroDivisionError:
    print("The second number can't be 0")
except ValueError:
    print("Invaild number")


# In[48]:

try:
    x=int(input("Please input a number"))
    y=int(input("Please input a number"))
    print("{}/{}={}".format(x,y,x/y))
except (ZeroDivisionError,ValueError)as e:
    print(e)

    


# In[50]:

while True:
    try:
        x=int(input("Please input a number"))
        y=int(input("Please input a number"))
        print("{}/{}={}".format(x,y,x/y))
    except (ZeroDivisionError,ValueError)as e:
        print(e)
    else:break#如果发生异常就一直重新输入，直到没有异常


# In[51]:

x=None
try:
    x=1/0
finally:#不管对还是错都会执行的
    print("cleaning up")
    del x


# In[52]:

x


# In[53]:

def  inner():
    print("innner...")
    raise Exception
    
def  outer():
    print("outer..before innner")
    inner()
    print("outer..after inner")

outer()


# In[ ]:



