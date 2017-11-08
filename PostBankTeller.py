import time,random,BanksDataBase
TransactionDay = time.strftime('%A %d/%m/%y\n%H:%M:%S %p', time.localtime())
IssueDay = time.strftime('%A', time.localtime())


class BANK(object):
    BankInfo = BanksDataBase.PostBankInfo
    print(BankInfo)

class TELLER(BANK):
    def __init__(self):
        self.TellerId = 'Any TellerId'
        self.TellerName = 'Any TellerName'
        self.CustomerName = "Any CustomerName"
        self.CustomerId = 'Any CustomerId.'
        self.CustomerAccountNo = 'Any CustomerAccountNo.'
        self.Amount = 'Any Amount'
        self.CustomerAddress = 'Any CustomerAddress'
        self.CustomerPhoneNo = 'Any CustomerPhoneNo'
        self.Balance = 'Any Balance'
        self.answer = 'Any answer'
        self.WithdrawCharge = 'Bank Charge'
        self.MinBalance = 'Least Amount to stay on account'
        self.Id = 'Identifier'
        self.CustomerAccountNos = BanksDataBase.PostCustomerAccountNos
        self.CustomerNames = BanksDataBase.PostCustomerNames
        self.CustomerIds = BanksDataBase.PostCustomerIds
        self.CustomerAddresses = BanksDataBase.PostCustomerAddresses
        self.Balances = BanksDataBase.PostCustomerBalance
        self.CustomerPhoneNos = BanksDataBase.PostCustomerPhoneNos
        self.CustomerLoansRecords = BanksDataBase.PostLoansRecords
        self.TellerIds = BanksDataBase.PostTellerIds
        self.TellerNames = BanksDataBase.PostTellerNames

    def OpenAccount(self):
        self.CustomerName = (input('Enter Your Full Name (Upper Case): '))
        while 1:
            if (len(self.CustomerName) >= 6) and (self.CustomerName == self.CustomerName.upper()):
                break
            else:
                print('Name should have atleast Six Letters! And Please Use Right Letter Case')
                self.CustomerName = input('Re-enter Full Name (Upper Case): ')
                TellerObj.QUIT()

        try:
            self.CustomerId = int(input('Enter Your ID Number: '))
        except ValueError:
            print('Integers Please!')
        while 2:
            if len(str(self.CustomerId)) >= 4:
                break
            else:
                try:
                    self.CustomerId = int(input('Your ID Must Have Atleast 4 Numbers'
                                                '\nRe-enter Your ID Number: '))
                except ValueError:
                    print('Integers Please!')
                TellerObj.QUIT()
        #   check Account Existence
        if self.CustomerName in self.CustomerNames:
            if str(self.CustomerId) == self.CustomerIds[self.CustomerNames.index(self.CustomerName)]:
                print('YOUR ARE ALREADY A CUSTOMER!')
        else:

            self.CustomerAddress = (input('Enter Place Of Residence (Upper Case): '))
            while 3:
                if (len(self.CustomerAddress) >= 3) and (self.CustomerAddress == self.CustomerAddress.upper()):
                    break
                else:
                    print('Address should have atleast Three Letters! And Please Use Right Letter Case')
                    self.CustomerAddress = input('Re-enter Address (Upper Case): ')
                    TellerObj.QUIT()
            try:
                self.CustomerPhoneNo = int(input('Enter Your Phone Number: '))
            except ValueError:
                print('Integers Please!')
            while 4:
                if len(str(self.CustomerPhoneNo)) == 9:
                    break
                else:
                    try:
                        self.CustomerPhoneNo = int(input('Your Phone Number Must Have 10 Numbers e.g 07...'
                                                         '\nRe-enter Your Phone Number: '))
                    except ValueError:
                        print('Integers Please!')
                    TellerObj.QUIT()
            self.MinBalance = int(self.BankInfo[4])  # minimum Balance is BankInfo file index 4
            self.WithdrawCharge = int(self.BankInfo[3])  # withdraw charge is BankInfo file index 3
            try:
                self.Amount = int(input("Enter Amount As Customer's First Deposit: "))
            except ValueError:
                print('Integers Please!')
            while 5:
                if self.Amount > (self.MinBalance + self.WithdrawCharge):
                    break
                else:
                    try:
                        self.Amount = int(input('Your Amount must exceed UGX '+str(self.MinBalance + self.WithdrawCharge)+'\nRe-enter Amount: '))
                    except ValueError:
                        print('Integers Please!')
            self.Balance = self.Amount
            self.CustomerPhoneNo = ('0'+str(self.CustomerPhoneNo))
            #   Not to generate Duplicate AccountNo, we while the random module
            while 6:
                self.CustomerAccountNo = (self.BankInfo[1]+str(random.randint(10000, 99999)))
                if self.CustomerAccountNo not in self.CustomerAccountNos:
                    break
                else:
                    pass
            print("Customer's Account Successfully Created!")
            print("\nCUSTOMER'S ACCOUNT NUMBER:", self.CustomerAccountNo,
                  '\nOn', TransactionDay)

            self.CustomerAccountNos.append(self.CustomerAccountNo)
            self.CustomerNames.append(self.CustomerName)
            self.CustomerIds.append(self.CustomerId)
            self.CustomerAddresses.append(self.CustomerAddress)
            self.CustomerPhoneNos.append(self.CustomerPhoneNo)
            self.Balances.append(self.Balance)

            BanksDataBase.PostAccUpdate(self)

    def CollectMoney(self):
        BanksDataBase.CheckDataBase(self)
        while 1:
            try:
                self.Amount = int(input('Enter Amount to Collect: '))
            except ValueError:
                print('Integers Please!')
            if self.Amount is type(str):
                pass
            else:
                break
        self.CustomerAccountNoIndex = self.Id
        self.Balance = int(self.Balances[self.Id])
        self.CustomerName = self.CustomerNames[self.Id]
        self.Balance += self.Amount
        BanksDataBase.PostBalUpdate(self)
        print('You have Collected of UGX', self.Amount,'To Account of', self.CustomerName)

    def ProvideInfo(self):
        BanksDataBase.CheckDataBase(self)
        print(' '*10+'CUSTOMER ACCOUNT DETAILS:\nACCOUNT NUMBER: ', self.CustomerAccountNo, '\nNAME: ', self.CustomerName,
              '\nCUSTOMER ID: ', self.CustomerId, '\nBALANCE: ', self.Balance,
              '\nPHONE NUMBER: ', str(self.CustomerPhoneNo))

    def LoanRequest(self):
        BanksDataBase.CheckDataBase(self)
        print(' '*10+'CUSTOMER ACCOUNT DETAILS:\nACCOUNT NUMBER: ', self.CustomerAccountNo,
              '\nNAME: ', self.CustomerName, '\nBALANCE: ', self.Balance,
              '\nPHONE NUMBER: ',str(self.CustomerPhoneNo))
        try:
            self.Amount =int(input('\nEnter Amount Being Borrowed: '))
        except ValueError:
            print('Integers Please!')
        if self.Amount >= 20*int(self.Balance) or self.Amount <= 1.5*int(self.Balance):
            print('Amount loanable must be between', (1.5*int(self.Balance)), 'and', (20*self.Balance))
            print('Loan Request Of', self.Amount, 'Denied!')

        else:
            print('Loan Request Of', self.Amount, 'Granted!\nApplied on: ',TransactionDay)
            self.CustomerLoansRecords.append('On '+TransactionDay+' ACCOUNT NUMBER: '+str(self.CustomerAccountNo)+' NAME: '+self.CustomerName+' LOAN AMOUNT: '+str(self.Amount)+' PHONE NUMBER: '+str(self.CustomerPhoneNo)+'\n')
            f = open("BANKS\PostBankFiles\LoansRecords.txt", 'w')
            for i in self.CustomerLoansRecords:
                f.write(str(i) + "\n")
            f.close()

    def CloseAccount(self):
        BanksDataBase.CheckDataBase(self)
        self.CustomerAccountNos.__delitem__(self.Id)
        self.CustomerNames.__delitem__(self.Id)
        self.CustomerIds.__delitem__(self.Id)
        self.CustomerAddresses.__delitem__(self.Id)
        self.Balances.__delitem__(self.Id)
        self.CustomerPhoneNos.__delitem__(self.Id)
        BanksDataBase.PostAccUpdate(self)
        print("Customer's Account Successfully Closed.")
    def IssueCard(self,answer):
        self.answer =answer
        self.answer = self.answer.lower()
        if self.answer == 'f':
            BanksDataBase.CheckDataBase(self)
            print(' ' * 10 + 'ACCOUNT DETAILS FOR REQUESTED CARD:\n'+'#'*(25+len(self.CustomerName))+'\n#   ACCOUNT NUMBER: ', self.CustomerAccountNo,
                  '\n#   NAME:           ', self.CustomerName,'\n#   CUSTOMER ID:    ',str(self.CustomerId),
                  '\n#   PHONE NUMBER:   ', str(self.CustomerPhoneNo),'\n'+'#'*(25+len(self.CustomerName)))
            print('Your Card Will Be Issued In A Weeks Time.\nPlease Check Back Next',IssueDay,'Thanks!')
        elif self.answer == 'l':
            BanksDataBase.CheckDataBase(self)
            self.Balance -= self.WithdrawCharge
            print(' ' * 10 + ' ACCOUNT DETAILS FOR REQUESTED CARD:\nACCOUNT NUMBER: ', self.CustomerAccountNo,
                  '\nNAME: ', self.CustomerName,
                  '\nPHONE NUMBER: ', str(self.CustomerPhoneNo))
            print('Your Card Will Be Issued in a weeks time On A Charge of UGX: ',self.WithdrawCharge,
                  '\nPlease Check Back Next', IssueDay, 'Thanks!')
            BanksDataBase.PostBalUpdate(self)

    def TellerInterface(self):
        print("\nYOU CAN NOW ACCESS TELLER INTERFACE\n<PRESS> 'O': To Open New Customer Account"
              "\n<PRESS> 'D': To Collect Cash'"
              "\n<PRESS> 'I': To Provide Info"
              "\n<PRESS> 'A': To Request For Loan"
              "\n<PRESS> 'C': To Close Customer's Account\n<PRESS> 'R': To Issue Card"
              "\n<PRESS> 'Q': To QUIT\n")
        self.answer = input('Enter Desired Option: ')
        self.answer = self.answer.lower()
        if self.answer == 'o':
            TellerObj.OpenAccount()
            TellerObj.MoreTransactions()
        elif self.answer == 'd':
            TellerObj.CollectMoney()
            TellerObj.MoreTransactions()
            TellerObj.MoreTransactions()
        elif self.answer == 'i':
            TellerObj.ProvideInfo()
            TellerObj.MoreTransactions()
        elif self.answer == 'a':
            TellerObj.LoanRequest()
            TellerObj.MoreTransactions()
        elif self.answer == 'c':
            TellerObj.CloseAccount()
            TellerObj.MoreTransactions()
        elif self.answer == 'r':
            TellerObj.IssueCard(input("Customer Requesting Card for first time?? <PRESS> 'F'"
                                      "'\nCustomer Lost Card?? <PRESS> 'L'\n: "))
            TellerObj.MoreTransactions()
        elif self.answer == 'q':
            exit()

    def MoreTransactions(self):
        self.answer = input("For more Transactions <PRESS> 'M'\nTo Quit <PRESS> 'Q'\n: ")
        self.answer = self.answer.upper()
        if self.answer == "M":
            TellerObj.TellerInterface()
        elif self.answer == "Q":
            exit()
PostTellerObj = TELLER()
