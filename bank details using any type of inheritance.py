class bank:
    def __init__(self,bank_name,branch,code):
        self.bank_name=bank_name
        self.branch=branch
        self.code=code
    def abc(self):
        print('bank name:',self.bank_name)
        print('bank branch:',self.branch)
        print('bank code:',  self.code)
class bankaccount (bank):
    def __init__(self,bank_name,branch,code,account_holder,account_number,balance):
        super().__init__(bank_name,branch,code)
        self.account_holder=account_holder
        self.account_number=account_number
        self.balance=balance
    def var(self):
        print('self.account_holder:',account_holder)
        print('self.account_number:',account_number)
        print('self.balance:',balance)
bank_name=input('bank name:')
branch=input('branch:')
code=input('code:')
account_holder=input('account holder name:')
account_number=input('account name:')
balance=float(input('enter balance:'))
a=bankaccount(bank_name,branch,code,account_holder,account_number,balance)
a.abc()
a.var()
        
