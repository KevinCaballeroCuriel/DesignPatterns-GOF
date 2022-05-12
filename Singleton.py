class DatabaseConfiguration():
    _sharedData = {}
    def __init__(self, **kwargs):
        self._sharedData.update(kwargs)            
    def __str__(self):
        return str(self._sharedData)                
 
configDetailsOne = DatabaseConfiguration(database = "10.10.10.10")
print(configDetailsOne)                             
 
configDetailsTwo = DatabaseConfiguration(user = "userOne")
configDetailsThree = DatabaseConfiguration(password="userOne")
configDetailsFour = DatabaseConfiguration(serviceName="serviceOne")
 
print(configDetailsFour)

