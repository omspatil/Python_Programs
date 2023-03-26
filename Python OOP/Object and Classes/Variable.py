# All class variable
class test:
    # class variable
    j = 0

    def __init__(self, x) -> None:
        # instance variable
        self.i = x
        # class variable
        test.j += 1

    def show(self):
        print(self.i, test.j)


t1 = test(10)
t2 = test(20)
t3 = test(30)
t1.show()
t2.show()
t3.show()
