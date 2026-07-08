class student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem 
        self.math=math
        
    #def calpercentage(self):
     #   self.percentage =str((self.phy+self.chem+self.math)/3)  
  
    @property
    def percentage (self):
        return str((self.phy+self.chem+self.math)/3) 
    
    
s1=student(89,98,97)
print(s1.percentage)

s1.phy=100
print(s1.percentage)
       