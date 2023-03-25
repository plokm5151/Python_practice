#跟list差在一旦新增就不能修改
class Test:
    def __init__(self):
        self.scores=(90,80,60,70,50)
    

    def my_print(self):
        print(self.scores)


Test().__init__()
Test().my_print()