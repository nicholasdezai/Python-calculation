class Customer:
    def __init__(self, name):
        self.name = name

    def placeOrder(self, employee):
        print(f"{self.name}正在向{employee.name}下单...")
        return employee.takeOrder()


class Employee:
    def __init__(self, name):
        self.name = name

    def takeOrder(self):
        food_name = input(f"{self.name}：请问您要点什么？ ")
        return Food(food_name)


class Food:
    def __init__(self, name):
        self.name = name


class Lunch:
    def __init__(self, customer, employee):
        self.customer = customer
        self.employee = employee

    def order(self):
        food = self.customer.placeOrder(self.employee)
        return food

    def result(self, food):
        print(f"{self.customer.name}收到了{self.employee.name}的食物订单：{food.name}")


def main():
    customer_name = input("请输入顾客姓名： ")
    employee_name = input("请输入商户姓名： ")
    customer = Customer(customer_name)
    employee = Employee(employee_name)
    lunch = Lunch(customer, employee)
    food = lunch.order()
    lunch.result(food)


if __name__ == "__main__":
    main()

