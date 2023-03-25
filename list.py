#list

class score:
    def __init__(self):
        self.scores = [90,70,60,50,80]
        self.friends=["frank","andrew","raymond","ignacio","ivory"]
    
    def my_print(self):
        print(self.scores)
        print(self.friends)
    
    def print_native_number(self):
        print(self.scores[-1])
        print(self.friends[-1])

    def print_range(self):
        print(self.scores[0:4])
        print(self.friends[0:4])
    
    def sort_and_print(self):
        self.scores.sort()
        print(self.scores)


def main():
    myclass=score()
    myclass.my_print()
    myclass.print_native_number()
    myclass.print_range()
    myclass.sort_and_print()


main()