class Bank:
    def __init__(self, balance: List[int]):
        self.ct = len(balance)
        self.b = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if 1 <= account1 <= self.ct and 1 <= account2 <= self.ct:
            if money > self.b[account1-1]:
                return False
            self.b[account1-1] -= money
            self.b[account2-1] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if 1 <= account <= self.ct:
            self.b[account-1] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if 1 <= account <= self.ct and money <= self.b[account-1]:
            self.b[account-1] -= money
            return True
        return False
