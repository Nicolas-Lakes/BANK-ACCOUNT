class Interface(object):
    def LogIn(self):
        self.BankChoice = input("For CENTENARY BANK:  <PRESS> 'C'\nFor POST BANK:  <PRESS> 'P'")
        self.answer = input("For CUSTOMER:  <PRESS> 'C'\nFor TELLER:  <PRESS> 'T'")
        self.BankChoice = self.BankChoice.lower()
        self.answer = self.answer.lower()
        if self.BankChoice == 'c' and self.answer == 'c':
            from CentenaryBankCustomer import CUSTOMER
            CentCustomerObj = CUSTOMER()
            CentCustomerObj.CustomerInterface()
        elif self.BankChoice == 'c' and self.answer == 't':
            from CentenaryTeller import TELLER
            CentTellerObj = TELLER()
            CentTellerObj.TellerInterface()
        elif self.BankChoice == 'p' and self.answer == 't':
            from PostBankTeller import TELLER
            PostTellerObj = TELLER()
            PostTellerObj.TellerInterface()
        elif self.BankChoice == 'p' and self.answer == 'c':
            from PostBankCustomer import CUSTOMER
            PostCustomerObj = CUSTOMER()
            PostCustomerObj.CustomerInterface()
interfaceObj = Interface()
interfaceObj.LogIn()
