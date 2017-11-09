#       importing modules and BankDatabase file
import time, random, BanksDataBase

TransactionDay = time.strftime('%A %d/%m/%y\n%H:%M:%S %p', time.localtime())
IssueDay = time.strftime('%A', time.localtime())


class BANK(object):
    BankInfo = BanksDataBase.PostBankInfo
    print('WELCOME TO ', BankInfo[0], BankInfo[2], '\nHERE TO SERVE YOU!')


class CUSTOMER(BANK):
    def __init__(self):
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

    def OpenAccount(self):
        self.CustomerName = (input('Enter Your Full Name (Upper Case): '))
        while 1:
            if (len(self.CustomerName) >= 6) and (self.CustomerName == self.CustomerName.upper()):
                break
            else:
                print('Name should have atleast Six Letters! And Please Use Right Letter Case')
                self.CustomerName = input('Re-enter Full Name (Upper Case): ')

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
        # check Account Existence
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

            self.MinBalance = int(self.BankInfo[4])  # minimum Balance is BankInfo file index 4
            self.WithdrawCharge = int(self.BankInfo[3])  # withdraw charge is BankInfo file index 3
            try:
                self.Amount = int(input('Enter Amount As Your First Deposit: '))
            except ValueError:
                print('Integers Please!')
            while 5:
                if self.Amount > (self.MinBalance + self.WithdrawCharge):
                    break
                else:
                    try:
                        self.Amount = int(input('Your Amount must exceed UGX ' + str(
                            self.MinBalance + self.WithdrawCharge) + '\nRe-enter Amount: '))
                    except ValueError:
                        print('Integers Please!')
            self.Balance = self.Amount
            self.CustomerPhoneNo = ('0' + str(self.CustomerPhoneNo))
            #   Not to generate Duplicate AccountNo, we while the random module
            while 6:
                self.CustomerAccountNo = (self.BankInfo[1] + str(random.randint(10000, 99999)))
                if self.CustomerAccountNo not in self.CustomerAccountNos:
                    break
                else:
                    pass
            print('Your Account Has Been Successfully Created!'
                  '\nTHANKS FOR JOINING', self.BankInfo[0], 'WE CARE!')
            print('\n' + ' ' * 10 + 'YOUR ACCOUNT DETAILS:\nYOUR ACCOUNT NUMBER:', self.CustomerAccountNo,
                  '\nNAME: ', self.CustomerName, '\nRESIDENCE:', self.CustomerAddress,
                  '\nBALANCE:', self.Balance, '\nPHONE NUMBER:', self.CustomerPhoneNo,
                  '\nOPENED AT:', self.BankInfo[2], 'BRANCH \nOn', TransactionDay)

            self.CustomerAccountNos.append(self.CustomerAccountNo)
            self.CustomerNames.append(self.CustomerName)
            self.CustomerIds.append(self.CustomerId)
            self.CustomerAddresses.append(self.CustomerAddress)
            self.CustomerPhoneNos.append(self.CustomerPhoneNo)
            self.Balances.append(self.Balance)

            BanksDataBase.PostAccUpdate(self)

    def DepositMoney(self):
        BanksDataBase.CheckDataBase(self)
        while 1:
            try:
                self.Amount = int(input('Enter Amount to Deposit: '))
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
        print('Thanks,', self.CustomerName, 'fot your deposit of UGX', self.Amount,
              '\nYou Now Have UGX', self.Balance)

    def WithdrawMonney(self):
        BanksDataBase.CheckDataBase(self)
        try:
            self.Amount = int(input('Enter Amount to WithDraw: '))
        except ValueError:
            print('Integers Please!')
        self.CustomerAccountNoIndex = self.Id
        self.Balance = int(self.Balances[self.Id])
        self.CustomerName = self.CustomerNames[self.Id]
        if self.Amount < (self.Balance - (int(self.MinBalance) + int(self.WithdrawCharge))):
            self.Balance -= (self.Amount + int(self.WithdrawCharge))
            BanksDataBase.PostBalUpdate(self)
            print('Thanks For Your Transaction.\nYou Now Have', self.Balance, 'UGX Left')
        elif self.Amount == (self.Balance - (int(self.MinBalance) + int(self.WithdrawCharge))):
            self.Balance -= (self.Amount + int(self.WithdrawCharge))
            BanksDataBase.PostBalUpdate(self)
            print('Thanks For Your Transaction.'
                  '\nNew Amount  On Account: UGX', self.Balance, '(NOT WITHDRAWABLE)')
        elif self.Amount > (self.Balance - int(self.MinBalance + self.WithdrawCharge)):
            print('Hey,', self.CustomerName, 'you are not able to Withdraw UGX', self.Amount,
                  '\nYou Need to have a Balance of UGX', self.Amount + int(self.WithdrawCharge) + int(self.MinBalance))
            print('But instead you have UGX', self.Balance, '\nThank You!')

    def GeneralInquiry(self):
        BanksDataBase.CheckDataBase(self)
        print(' ' * 10 + 'YOUR ACCOUNT DETAILS:\nACCOUNT NUMBER: ', self.CustomerAccountNo, '\nNAME: ',
              self.CustomerName,
              '\nCUSTOMER ID: ', self.CustomerId, '\nBALANCE: ', self.Balance,
              '\nPHONE NUMBER: ', str(self.CustomerPhoneNo))

    def ApplyForLoan(self):
        BanksDataBase.CheckDataBase(self)
        print(' ' * 10 + 'YOUR ACCOUNT DETAILS:\nACCOUNT NUMBER: ', self.CustomerAccountNo,
              '\nNAME: ', self.CustomerName, '\nBALANCE: ', self.Balance,
              '\nPHONE NUMBER: ', str(self.CustomerPhoneNo))
        try:
            self.Amount = int(input('\nEnter Amount To Borrow: '))
        except ValueError:
            print('Integers Please!')
        if self.Amount >= 20 * int(self.Balance) or self.Amount <= 1.5 * int(self.Balance):
            print('Amount loanable must be between', (1.5 * int(self.Balance)), 'and', (20 * self.Balance))
            print('Loan Request Of', self.Amount, 'Denied!')

        else:
            print('Loan Request Of', self.Amount, 'Granted!\nApplied on: ', TransactionDay)
            self.CustomerLoansRecords.append('On ' + TransactionDay + ' ACCOUNT NUMBER: ' + str(
                self.CustomerAccountNo) + ' NAME: ' + self.CustomerName + ' LOAN AMOUNT: ' + str(
                self.Amount) + ' PHONE NUMBER: ' + str(self.CustomerPhoneNo) + '\n')
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
        print("Your Account Has Been Successfully Closed.\nThanks For All Your Services!")

    def RequestCard(self, answer):
        self.answer = answer
        self.answer = self.answer.lower()
        if self.answer == 'f':
            BanksDataBase.CheckDataBase(self)
            print(' ' * 10 + 'YOUR ACCOUNT DETAILS:\nACCOUNT NUMBER: ', self.CustomerAccountNo,
                  '\nNAME: ', self.CustomerName, '\nBALANCE: ', self.Balance,
                  '\nPHONE NUMBER: ', str(self.CustomerPhoneNo))
            print('Your Card Will Be Issued In A Weeks Time.\nPlease Check Back Next', IssueDay, 'Thanks!')
        elif self.answer == 'l':
            BanksDataBase.CheckDataBase(self)
            self.Balance -= self.WithdrawCharge
            print(' ' * 10 + 'YOUR ACCOUNT DETAILS:\nACCOUNT NUMBER: ', self.CustomerAccountNo,
                  '\nNAME: ', self.CustomerName, '\nBALANCE: ', self.Balance,
                  '\nPHONE NUMBER: ', str(self.CustomerPhoneNo))
            print('Your Card Will Be Issued In A Weeks Time On A Charge of UGX: ', self.WithdrawCharge,
                  '\nPlease Check Back Next', IssueDay, 'Thanks!')
            BanksDataBase.PostBalUpdate(self)

    def CustomerInterface(self):
        print(
            "\nUSER INTERFACE\n<PRESS> 'O': To Open New Account\n<PRESS> 'D': To Deposit Cash\n<PRESS> 'W': To Withdraw Cash"
            "\n<PRESS> 'I': To Inquire Your Current Account Status\n<PRESS> 'A': To Apply For Loan"
            "\n<PRESS> 'C': To Close Your Account\n<PRESS> 'R': To Request For Card"
            "\n<PRESS> 'Q': To QUIT\n")
        self.answer = input('Enter Desired Option: ')
        self.answer = self.answer.lower()
        if self.answer == 'o':
            PostCustomerObj.OpenAccount()
            PostCustomerObj.MoreTransactions()
        elif self.answer == 'd':
            PostCustomerObj.DepositMoney()
            PostCustomerObj.MoreTransactions()
        elif self.answer == 'w':
            PostCustomerObj.WithdrawMonney()
            PostCustomerObj.MoreTransactions()
        elif self.answer == 'i':
            PostCustomerObj.GeneralInquiry()
            PostCustomerObj.MoreTransactions()
        elif self.answer == 'a':
            PostCustomerObj.ApplyForLoan()
            PostCustomerObj.MoreTransactions()
        elif self.answer == 'c':
            PostCustomerObj.CloseAccount()
            PostCustomerObj.MoreTransactions()
        elif self.answer == 'r':
            PostCustomerObj.RequestCard(input('If Requesting Card for first time <PRESS> f'
                                          '\nLost Card? <PRESS> l\n: '))
            PostCustomerObj.MoreTransactions()
        elif self.answer == 'q':
            exit()

    def MoreTransactions(self):
        self.answer = input("For more Transactions <PRESS> 'M'\nTo Quit <PRESS> 'Q'\n: ")
        self.answer = self.answer.upper()
        if self.answer == "M":
            PostCustomerObj.CustomerInterface()
        elif self.answer == "Q":
            exit()

            # Instanciating Customer


PostCustomerObj = CUSTOMER()
