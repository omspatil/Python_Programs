# All methods in class
class test:
    def instance_method(self):
        print("Instance method demo")

    @classmethod
    def class_method(cls):
        print("Class method demo")

    @staticmethod
    def static_method():
        print("Static method demo")


t1 = test()
t1.instance_method()
test.class_method()
test.static_method()
