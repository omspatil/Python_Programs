# Create a class Mydate to show an date and check the date is valid or not.
class Mydate:
    def __init__(self, d, m, y):
        self.day = d
        self.month = m
        self.year = y

    def show(self):
        print(f"{self.day}/{self.month}/{self.year}")

    @staticmethod
    def check(d, m, y):
        if d >= 1 and d <= 31:
            return True
        else:
            return False

    @classmethod
    def From_string(cls, s):
        arr = list(map(int, s.split("-")))
        t1 = cls(arr[0], arr[1], arr[2])
        return t1


d1 = Mydate(10, 2, 2023)
d1.show()

d2 = Mydate.From_string("24-3-2023")
d2.show()

if Mydate.check(23, 3, 2023):
    print("Valid Date")
else:
    print("Invalid Date")
