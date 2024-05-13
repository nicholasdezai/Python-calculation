import os,sys
class Food:
    def __init__(self,food_name:str) -> None:
        self._food_name=food_name

class Employee:
    def takeOrder(self,food_name:str)->Food:
        return Food(food_name)
    
class Customer:
    def __init__(self) -> None:
        self._food_list=[]

    def placeOrder(self,employee:Employee,food_name:str):
        self._food_list.append(employee.takeOrder(food_name))

class Lunch:
    def __init__(self)->None:
        self._customer=Customer()
        self._employee=Employee()

    def order(self,food_name:str):
        self._customer.placeOrder(self._employee,food_name)

    def result(self):
        i=1
        for item in self._customer._food_list:
            print(f"{i}. {item._food_name}")
            i+=1

if __name__=="__main__":
    launch=Lunch()
    while True:
        os.system("clear")
        print("Please choose the function you need:\n1. take an order\n2. print the food list\n0. exit")
        try:
            num=input()
            os.system("clear")
            match num:
                case '1':
                    launch.order(input("Please order some food: "))
                case '2':
                    launch.result()
                    input("Press <ENTER> to continue...")
                case '0':
                    print("Thank you for using. Good bye.")
                    sys.exit()
                case _:
                    raise Exception
        except Exception:
            print("Invalid input! Please try again.")
            input("Press <ENTER> to continue...")
