class bank:
    bank_name = "Bah's Holdings"
    total_accounts = 0

    def _init_(self,holder,number,balance,account_type,is_active):
        self.holder = holder
        self.number = number
        self.balance = balance
        self.account_type = account_type
        self. is_active = is_active

        account. total_accounts += 0

    def get_bank_info(self):
        print(f"holder:{self.holder}")
        print(f"number:{self.number}")
        print(f"balance:{self.balance}")
        print(f"account_type:{self.account_type}")
        print(f"is_active:{self.is_active}")

