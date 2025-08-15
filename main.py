from linkedQueue import LinkedQueue
class Main:
    def __init__(self):
         self.__customersList=LinkedQueue()
    def addCustomerToList(self,name):
        self.__customersList.enqueue(name)
        print(f"Arriving: {name}")
    def removeCustomerFromList(self):
        name = self.__customersList.dequeue()
        print(f"Serving: {name}")
    def printMenue(self):
        print(f"1- Add Customer \n2-One Customer Serving \n3-Exit \n")
        if self.__customersList.is_empty():
            print('All customers served.')
    def run(self):
        print('Welcome \n')
        ch=0
        while ch is not 3:
            self.printMenue()
            ch=int(input('enter your chose: '))
            match ch:
                case 1:
                    name=input('Enter cusromer name: ')
                    self.addCustomerToList(name)
                case 2:
                    self.removeCustomerFromList()
                case _:
                    print("plz reenter your chose")
                    
         
if __name__=='__main__':
    main = Main()
    main.run()