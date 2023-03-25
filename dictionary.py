#storage key and value
#similar c++ map structure
class Test:
    def __init__(self):
        self.dic={"蘋果":"apple","香蕉":"banana","貓":"cat","狗":"dog"}
    
    def my_print(self):
        print(self.dic["蘋果"])

diction=Test()
diction.my_print()