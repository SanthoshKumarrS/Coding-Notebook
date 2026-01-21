'''
LEGB
Local,Enclosing,Global, Built-In
'''

x = 'global x' # global variable

def test():
    #global x     #This will change the global variable
    x = 'local x' # local variable
    print(x)

#test() 

m = min([1,2,7,8,9,5])
print(m)