class Account:
    def __init__(self, name):
        print("[init start]")
        self.name = name
        self.money = 10000
        print("[init end]")
        print("객체가 생성되었습니다.")
    def deposit(self, money):
        self.money += money
        print("%d원을 저축하여 총 잔액은 %d원 입니다." %(money, self.money))
    def withdraw(self, money):
        self.money -= money
        print("인출 잔액: %d" %self.money)
    def printBalance(self):
        print("잔고 금액입니다.")
        return self.money
    def printOwner(self):
        print("소유자: ", self.name)
        #return self.name

