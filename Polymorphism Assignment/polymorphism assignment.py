#creating a parent class
class Company_Manager:
    name = 'GiuseppeSAS'
    email = 'giuseppeSAS@gmail.com'
    password = '123456giu'

    def Companymsg(self):
        msg = "Welcome Manager"
        print(msg)
        

#child class1
class Company_Supervisor(Company_Manager):
    name = 'Victor Slone'
    email = 'victorslone@gmail.com'
    securePin = '546866'
#child class method  
    def Companymsg(self):
        msg = "Welcome supervisor"
        print(msg)


#child class2
class Company_HR(Company_Manager):
    name = 'Alexandra Dry'
    email = 'alexandradry@gmail.com'
    secretWord = 'youcrazy'
#child class2 method
    def Companymsg(self):
        msg = "Welcome HR"
        print(msg)


if __name__ == "__main__":
    manager = Company_Manager()
    supervisor = Company_Supervisor()
    HR = Company_HR()
    
#displaying the msg
    manager.Companymsg()
    supervisor.Companymsg()
    HR.Companymsg()


    






































