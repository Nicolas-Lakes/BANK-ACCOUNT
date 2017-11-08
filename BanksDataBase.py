
#                           THE BANKS DATABASE SYSTEM

# Order by line Index [Name, Id, Location, Withdraw Charge, Minimum Balance Allowable]

#               POST BANK
with open("BANKS\PostBankFiles\BankInfo.txt") as PBankInfoFile:
    PostBankInfo = list(line[:-1] for line in PBankInfoFile)
    PostBankName = str(PostBankInfo[0])
    PostBankId = int(PostBankInfo[1])
    PostBankLocation = str(PostBankInfo[2])
    PostWithDrawCharge = int(PostBankInfo[3])
    PostMinBalance = int(PostBankInfo[4])
    #print('WELCOME TO ', PostBankName, PostBankLocation, 'BRANCH\n YOUR BANK!')

#               CENTENARY BANK
with open("BANKS\CentenaryBankFiles\BankInfo.txt") as CBankInfoFile:
    CentenaryBankInfo = list(line[:-1] for line in CBankInfoFile)
    CentenaryBankName = str(CentenaryBankInfo[0])
    CentenaryBankId = int(CentenaryBankInfo[1])
    CentenaryBankLocation = str(CentenaryBankInfo[2])
    CentenaryWithDrawCharge = int(CentenaryBankInfo[3])
    CentenaryMinBalance = int(CentenaryBankInfo[4])

# "Making program list out of a file for easy use within Program"
#               CUSTOMER FILES
#              Centenary Customer DataBase
with open("BANKS\CentenaryBankFiles\CustomerAccountNos.txt") as CentenaryCustomerAccountNosFile:
    CentenaryCustomerAccountNos = list(line[:-1] for line in CentenaryCustomerAccountNosFile)
with open("BANKS\CentenaryBankFiles\CustomerNames.txt") as CentenaryCustomerNamesFile:
    CentenaryCustomerNames = list(line[:-1] for line in CentenaryCustomerNamesFile)
with open("BANKS\CentenaryBankFiles\CustomerIds.txt") as CentenaryCustomerIdsFile:
    CentenaryCustomerIds = list(line[:-1] for line in CentenaryCustomerIdsFile)
with open("BANKS\CentenaryBankFiles\CustomerAddresses.txt") as CentenaryCustomerAddressesFile:
    CentenaryCustomerAddresses = list(line[:-1] for line in CentenaryCustomerAddressesFile)
with open("BANKS\CentenaryBankFiles\CustomerPhoneNos.txt") as CentenaryCustomerPhoneNosFile:
    CentenaryCustomerPhoneNos = list(line[:-1] for line in CentenaryCustomerPhoneNosFile)
with open("BANKS\CentenaryBankFiles\CustomerBalance.txt") as CentenaryCustomerBalanceFile:
    CentenaryCustomerBalance = list(line[:-1] for line in CentenaryCustomerBalanceFile)

#             Post Customer DataBase
#print('\n'+' '*10+'Post Customer DataBase')
with open("BANKS\PostBankFiles\CustomerAccountNos.txt") as PostCustomerAccountNosFile:
    PostCustomerAccountNos = list(line[:-1] for line in PostCustomerAccountNosFile)
with open("BANKS\PostBankFiles\CustomerNames.txt") as PostCustomerNamesFile:
    PostCustomerNames = list(line[:-1] for line in PostCustomerNamesFile)
with open("BANKS\PostBankFiles\CustomerIds.txt") as PostCustomerIdsFile:
    PostCustomerIds = list(line[:-1] for line in PostCustomerIdsFile)
with open("BANKS\PostBankFiles\CustomerAddresses.txt") as PostCustomerAddressesFile:
    PostCustomerAddresses = list(line[:-1] for line in PostCustomerAddressesFile)
with open("BANKS\PostBankFiles\CustomerPhoneNos.txt") as PostCustomerPhoneNosFile:
    PostCustomerPhoneNos = list(line[:-1] for line in PostCustomerPhoneNosFile)
with open("BANKS\PostBankFiles\CustomerBalance.txt") as PostCustomerBalanceFile:
    PostCustomerBalance = list(line[:-1] for line in PostCustomerBalanceFile)

#                   TELLER
#     CentenaryBank
with open("BANKS\CentenaryBankFiles\TellerNames.txt") as CentenaryTellerNamesFile:
    CentenaryTellerNames = list(line[:-1] for line in CentenaryTellerNamesFile)
with open("BANKS\CentenaryBankFiles\TellerIds.txt") as CentenaryTellerIdsFile:
    CentenaryTellerIds = list(line[:-1] for line in CentenaryTellerIdsFile)
#       PostBank
with open("BANKS\PostBankFiles\TellerNames.txt") as PostTellerNamesFile:
    PostTellerNames = list(line[:-1] for line in PostTellerNamesFile)
with open("BANKS\PostBankFiles\TellerIds.txt") as PostTellerIdsFile:
    PostTellerIds = list(line[:-1] for line in PostTellerIdsFile)
#                   LOAN INFO
#   CentenaryBank
with open("BANKS\CentenaryBankFiles\LoanIds.txt") as CentenaryLoanIdsFile:
    CentenaryLoanIds = list(line[:-1] for line in CentenaryLoanIdsFile)
with open("BANKS\CentenaryBankFiles\LoanTypes.txt") as CentenaryLoanTypesFile:
    CentenaryLoanTypes = list(line[:-1] for line in CentenaryLoanTypesFile)
with open("BANKS\CentenaryBankFiles\LoansRecords.txt") as CentenaryLoansRecordsFile:
    CentenaryLoansRecords = list(line[:-1] for line in CentenaryLoansRecordsFile)
# PostBank
with open("BANKS\PostBankFiles\LoanIds.txt") as PostLoanIdsFile:
    PostLoanIds = list(line[:-1] for line in PostLoanIdsFile)
with open("BANKS\PostBankFiles\LoanTypes.txt") as PostLoanTypesFile:
    PostLoanTypes = list(line[:-1] for line in PostLoanTypesFile)
with open("BANKS\PostBankFiles\LoansRecords.txt") as PostLoansRecordsFile:
    PostLoansRecords = list(line[:-1] for line in PostLoansRecordsFile)

#               METHODS
def CheckDataBase(self):
    # CHECKING AND VALIDATING CUSTOMER INFO STORED IN BANK DATABASE
    try:
        self.CustomerAccountNo = int(input('Enter Your CustomerAccountNo: '))
    except ValueError:
        print('Integers Please!')
    # CHECKING AND VALIDATING CUSTOMER INFO STORED IN BANK DATABASE
    while 1:
        if str(self.CustomerAccountNo) in self.CustomerAccountNos:
            CustomerAccountNoIndex = int(self.CustomerAccountNos.index(str(self.CustomerAccountNo)))
            break
        else:
            try:
                self.CustomerAccountNo = int(input('You entered Wrong CustomerAccountNo, please re-enter:\n'))
            except ValueError:
                print('Integers Please!')
    CustomerName = str(input('Enter CustomerName: '))
    while 2:
        if CustomerName == self.CustomerNames[CustomerAccountNoIndex]:
            break
        else:
            CustomerName = input('You entered Wrong CustomerName, please re-enter:\n')
    try:
        self.CustomerId = int(input('Enter Your CustomerId: '))
    except ValueError:
        print('Integers Please!')
    while 3:
        if str(self.CustomerId) == self.CustomerIds[CustomerAccountNoIndex]:
            break
        else:
            try:
                self.CustomerId = int(input('You entered Wrong CustomerId, please re-enter:\n'))
            except ValueError:
                print('Integers Please!')
    self.Id = CustomerAccountNoIndex
    self.CustomerAddress = self.CustomerAddresses[self.Id]
    self.CustomerName = self.CustomerNames[self.Id]
    self.Balance = int(self.Balances[self.Id])
    self.CustomerPhoneNo = self.CustomerPhoneNos[self.Id]
    self.CustomerName = self.CustomerNames[self.Id]
    self.CustomerId = self.CustomerIds[self.Id]
    self.MinBalance = int(self.BankInfo[4])  # minimum Balance is BankInfo file index 4
    self.WithdrawCharge = int(self.BankInfo[3])  # withdraw charge is BankInfo file index




def AccUpdate(self):    # updates the Program list then opens files and "write" them in form of over-write

    f = open("BANKS\CentenaryBankFiles\CustomerAccountNos.txt", 'w')
    for i in self.CustomerAccountNos:
        f.write(str(i) + "\n")
    f.close()
    f = open("BANKS\CentenaryBankFiles\CustomerNames.txt", 'w')
    for i in self.CustomerNames:
        f.write(str(i) + "\n")
    f.close()
    f = open("BANKS\CentenaryBankFiles\CustomerIds.txt", 'w')
    for i in self.CustomerIds:
        f.write(str(i) + "\n")
    f.close()
    f = open("BANKS\CentenaryBankFiles\CustomerAddresses.txt", 'w')
    for i in self.CustomerAddresses:
        f.write(str(i) + "\n")
    f.close()
    f = open("BANKS\CentenaryBankFiles\CustomerPhoneNos.txt", 'w')
    for i in self.CustomerPhoneNos:
        f.write(str(i) + "\n")
    f.close()
    f = open("BANKS\CentenaryBankFiles\CustomerBalance.txt", 'w')
    for i in self.Balances:
        f.write(str(i) + "\n")
    f.close()
# Over write Balance file with new updates list
def BalUpdate(self):
    self.Balances[self.Id] = self.Balance
    f = open("BANKS\CentenaryBankFiles\CustomerBalance.txt", 'w')
    for i in self.Balances:
        f.write(str(i) + "\n")
    f.close()

def PostAccUpdate(self):  # updates the Program list then opens files and "write" them in form of over-write
    f = open("BANKS\PostBankFiles\CustomerAccountNos.txt", 'w')
    for i in self.CustomerAccountNos:
        f.write(str(i) + "\n")
    f.close()
    f = open("BANKS\PostBankFiles\CustomerNames.txt", 'w')
    for i in self.CustomerNames:
        f.write(str(i) + "\n")
    f.close()
    f = open("BANKS\PostBankFiles\CustomerIds.txt", 'w')
    for i in self.CustomerIds:
        f.write(str(i) + "\n")
    f.close()
    f = open("BANKS\PostBankFiles\CustomerAddresses.txt", 'w')
    for i in self.CustomerAddresses:
        f.write(str(i) + "\n")
    f.close()
    f = open("BANKS\PostBankFiles\CustomerPhoneNos.txt", 'w')
    for i in self.CustomerPhoneNos:
        f.write(str(i) + "\n")
    f.close()
    f = open("BANKS\PostBankFiles\CustomerBalance.txt", 'w')
    for i in self.Balances:
        f.write(str(i) + "\n")
    f.close()
# Over write Balance file with new updates list
def PostBalUpdate(self):
    self.Balances[self.Id] = self.Balance
    f = open("BANKS\PostBankFiles\CustomerBalance.txt", 'w')
    for i in self.Balances:
        f.write(str(i) + "\n")
    f.close()

def QUIT(self):
    self.answer = input("To Quit <PRESS> 'Q'\n: ")
    self.answer = self.answer.upper()
    if self.answer == "Q":
        exit()
