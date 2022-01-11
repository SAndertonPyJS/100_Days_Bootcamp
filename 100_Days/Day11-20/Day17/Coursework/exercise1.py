#!usr/bin/env/python

#an example of creating ones own class. The class must be able to print hello world!

#first we create our class
class Hello:
    #now we make our init file. This will have 0 attributes
    def __init__(self) -> None:
        pass

    #now for our methods, we only want one method and that's to print hello world
    #we use a self argument to let the method know that it's part of the class and this allows it
    #to use and be used globally.
    def hello_world(self):
        return "Hello, World!"
        

#Now we create our object
statement = Hello()

#and finally call our method
print(statement.hello_world())
