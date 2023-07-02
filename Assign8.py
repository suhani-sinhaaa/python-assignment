class A:
    def __init__(self,a,b,c):
        self.__a=a
        self._b=b
        self.c=c 
    def display(self):
        print(f"a: {self.__a} b: {self._b} c: {self.c}")
class B(A):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)
    def display(self):
        super().display()
try:
    a=A(20,40,60)
    print("The values in A:")
    a.display()
    b=B(200,400,600)
    print("The values in B:")
    b.display()
    print(a.__a)
except AttributeError:
    print("ERROR:Cannot access private member a.")
