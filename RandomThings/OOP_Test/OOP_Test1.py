class User:
    __count = 0
    __instance = None
    WORLD = "OUTSIDE"
    
    #! For that type of controlling you have to delete overloaded methods
    #__slots__ = ["firstname","lastname","age","__email","__password"]
            
    def __init__(self,firstname=None,lastname=None,age=None,email=None,password=None):
        User.__count +=1
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.__email = email
        self.__password = password
        #self.visual_password = len(self.__password)*'*'
    
    def __checkData(item):
        if isinstance(item,int) or isinstance(item, float):
            return True
        return False
    
    
    
    def __setCredentials(self,firstname,lastname,age,email,password):
        if User.__checkData(age):
            self.firstname = firstname
            self.lastname = lastname
            self.age = age
            self.email = email
            self.password = password
            #TODO: To hide the password in output
            #self.visual_password = len(self.__password)*'*'
        else:
            raise ValueError('Input the correct information for your credentials')
            
    def __getCredentials(self):
        return self.firstname, self.lastname, self.age, self.email, self.password   
    
    def __delCredentials(self):
        print("Deleting the attributes")
        del self.password
    
    credentials = property(__getCredentials, __setCredentials, __delCredentials)
    
    
    def displayInfo(self):
        print(f'User {self.firstname} {self.lastname} is logged now by email: {self.email} and password: {self.password}')
    
    def checkObj(self):
        if isinstance(self,User):
            print('Already logged in')
        else:
            print('Go on')
    
    def __setattr__(self,key,value):
        if key == "WORLD":
            raise AttributeError
        else:
            self.__dict__[key] = value
    
    
    @staticmethod
    def getCount():
        return User.__count
    
    def __del__(self):
        User.__count-=1
        
        
        
#user1 = User('Roman','Tymofieiev',15,'rdtymofieiev@gmail.com','terraform')
#user2 = User('Roman','Tymofieiev',15,'rdtymofieiev@yahoo.com','terraform')

user1=User()
user1.credentials = 'Roman','Tymofieiev',15,'rdtymofieiev@gmail.com','terraform'
a = user1.credentials
user1.displayInfo()
user2 = User('Alina','Boldyreva',15,'alinabold@gmail.com','terraform1')
#user1.displayInfo() 
print(User.getCount())
#del user2
#print(User.getCount())
#print(user1.__dict__)
print(isinstance(user1, User))
user2.checkObj()

#print(user1._User__WORLD)
#print(user1.__WORLD)
print(user1.WORLD)

#user1.height = 100




""" class Singleton(object):
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.__instance, cls):
            cls.__instance = super(Singleton,cls).__new__(cls)
        else:
            print("The user data is already created") """
        
