with open('test.txt', 'w') as file:
    file.write("Hi this is David")
    
    
file = open('test2.txt', 'w')
try:
    file.write("Hi this is david vijay ")
    
finally:
    pass


class ManagedFile:
    
    def __init__(self, filename) -> None:
        print('init')
        self.filename = filename
        
    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit')
        if self.file:
            self.file.close()
        if exc_type is not None:
            print("execution has been handled")
        return True
        
        
with ManagedFile('notes.txt') as file:
    print('context')
    file.write("David Vijay")
    file.method()
print("continuing")


class ManagedFile:
    def __init__(self, filename) -> None:
        print('Init')
        self.filename = filename
        
    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, exctraceback):
        print('exit')
        if self.file:
            print('self.file')
            self.file.close()
            
with ManagedFile('testing.py') as file:
    print('context')
    file.write("")
                
                
class ManagedFile:
    def __init__(self, filename):
        self.filename = filename 
        
    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file               
                
    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass
        #self.file.close()           
                
with ManagedFile ('final.txt') as file:
    file.write("No mention")