class bird:
    def fly(self):
        print("bird can fly")
    
class penguin(bird):
    def fly(self):
        print("penguin can not fly")
        
a=bird()
b=penguin()

a.fly()
b.fly()
        