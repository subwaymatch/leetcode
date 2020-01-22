from threading import Event

class FooBar:
    def __init__(self, n):
        self.n = n
        self.canPrintFoo = Event()
        self.canPrintBar = Event()
        
        self.canPrintFoo.set()


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.canPrintFoo.wait()
            
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            
            self.canPrintFoo.clear()
            self.canPrintBar.set()
            

    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.canPrintBar.wait()
            
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            
            self.canPrintBar.clear()
            self.canPrintFoo.set()
