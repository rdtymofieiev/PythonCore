class User:
    WORLD = "OUTSIDE"
    __count = 0
    
    
    
    def __init__(self,firstname=None,lastname=None,age=None):
        User.__count +=1
        self.__firstname = firstname
        self.__lastname = lastname
        self.__age = age
        
        
    def __getFirstname(self):
        print("Running the getter")
        return self.__firstname
        
    def __setFirstname(self,firstname):
        if User.__checkData(age):
            self.__firstname = firstname
            print("Running the setter")
        else:
            raise ValueError('Input the correct information for your credentials')
    
    def __delCredentials(self):
        print("Deleting the attributes")
        del self.__firstname
    
    firstname_cred = property(__getFirstname, __setFirstname, __delCredentials)




user1 = User("Roman", "Tymofieiev", 21)
user1.firstname_cred = "Hero"
firstname = user1.firstname_cred