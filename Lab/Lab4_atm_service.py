class Bank:
    def __init__(self, name: str):
        self.__name = name
        self.__user = []
        self.__ATMMachine = []

    @property
    def name(self):
        return self.__name
    
    @property
    def user(self):
        return self.__user
    
    @property
    def ATMMachine(self):
        return self.__ATMMachine
    
    def addUser(self, new_user):
        self.__user.append(new_user)

    def addATMMachine(self, new_atm):
        self.__ATMMachine.append(new_atm)

    def get_atm(self, atm_id: str):
        for atm in self.__ATMMachine:
            if atm.machine_id == atm_id:
                return atm
        return None

    def get_user(self, citizen_id: str):
        for user in self.__user:
            if user.citizen_id == citizen_id:
                return user
        return None

class User:
    def __init__(self, citizen_id: str, name: str):
        self.__citizen_id = citizen_id
        self.__name = name
        self.__account = []

    @property
    def citizen_id(self):
        return self.__citizen_id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def account(self):
        return self.__account
    
    def addAccount(self, new_account):
        self.__account.append(new_account)

    def get_account(self, account_id: str):
        for account in self.__account:
            if account.account_id == account_id:
                return account
        return None

class Account:
    def __init__(self, owner: User, account_id: str, balance: int):
        self.__account_id = account_id
        self.__max_withdraw_per_day = 40_000
        self.__owner = owner
        self.__balance = balance
        self.__card = None
        self.__history_transaction = []

    @property
    def account_id(self):
        return self.__account_id
    
    @property
    def owner(self):
        return self.__owner
    
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, new_balance):
        self.__balance = new_balance
    
    @property
    def history_transaction(self):
        return self.__history_transaction

    @property
    def card(self):
        return self.__card
    
    @property
    def max_withdraw_per_day(self):
        return self.__max_withdraw_per_day
    @max_withdraw_per_day.setter
    def max_withdraw_per_day(self, new_max_withdraw):
        self.__max_withdraw_per_day = new_max_withdraw

    def createCard(self, new_card):
        self.__card = new_card

    def get_balance(self):
        return self.__balance

    def get_transaction(self):
        return self.__history_transaction

class ATMCard:
    def __init__(self, card_id: str, card_account: Account, pin: str):
        self.__card_id = card_id
        self.__card_account = card_account
        self.__pin = pin #'1234' fix

    @property
    def card_id(self):
        return self.__card_id
    
    @property
    def card_account(self):
        return self.__card_account
    
    @property
    def pin(self):
        return self.__pin

    def check_id_pin(self, validate_id, validate_pin):
        if validate_id == self.card_id and validate_pin == self.pin:
            return account
        else:
            return None

class ATMMachine:
    def __init__(self, machine_id: str, machine_balance: float):
        self.__machine_id = machine_id
        self.__machine_balance = machine_balance

    @property
    def machine_id(self):
        return self.__machine_id
    
    @property
    def machine_balance(self):
        return self.__machine_balance
    @machine_balance.setter
    def machine_balance(self, new_balance):
        self.__machine_balance = new_balance

    # TODO 2
    def insert_card(self, card_id: ATMCard.card_id, pin: str):
        for user in bank.user:
            for account in user.account:
                #method should in class card
                if account.card.check_id_pin(card_id, pin):
                    return account
        return None
    
    # TODO 3
    def deposit(self, account: Account, amount: int):
        if amount <= 0:
            return "Error"
        account.balance += amount

        transaction = Transaction('D', account.account_id, self.__machine_id, amount)
        #method should in Transaction class
        account.history_transaction.append(transaction)

        self.machine_balance += amount

        return "Success"
    
    # TODO 4
    def withdraw(self, account: Account, amount: int):
        if amount > self.__machine_balance:
            return "ATM has insufficient funds"
        elif amount > account.max_withdraw_per_day:
            return "Exceeds daily withdrawal limit of 40,000 baht"
        elif amount <= 0 or amount > account.balance:
            return "Error"

        account.balance -= amount
        account.max_withdraw_per_day -= amount

        transaction = Transaction('W', account.account_id, self.__machine_id, amount)
        account.history_transaction.append(transaction)

        self.machine_balance -= amount

        return "Success"
    
    def transfer(self, giver: Account, receiver: Account, amount: int):
        if amount <= 0 or amount > giver.balance:
            return "Error"

        giver.balance -= amount
        receiver.balance += amount

        transaction = Transaction('TD', giver.account_id, self.__machine_id, amount)
        giver.history_transaction.append(transaction)

        transaction_reciever = Transaction('TD', receiver.account_id, self.__machine_id, amount)
        receiver.history_transaction.append(transaction_reciever)

        return "Success"

    def get_balance(self):
        return self.__machine_balance
    
class Transaction:
    def __init__(self, transaction_type: str, account_id: str, machine_id: str, amount: int):
        self.__type = transaction_type
        self.__machine_id = machine_id
        self.__account_id = account_id
        self.__amount = amount

    @property
    def type(self):
        return self.__type
    
    @property
    def machine_id(self):
        return self.__machine_id

    @property
    def account_id(self):
        return self.__account_id
    
    @property
    def amount(self):
        return self.__amount

##################################################################################
# กำหนดรูปแบบของ user ดังนี้ {รหัสประชาชน : [ชื่อ, หมายเลขบัญชี, จำนวนเงิน, หมายเลข ATM ]}

# TODO 1
#create Bank - Success
bank = Bank('bank')

##################################################################################
#create User - Success
user_data ={'1-1101-12345-97-0':['Harry Potter','1234567890',20000,'12345'],
       '1-1101-12345-98-0':['Hermione Jean Granger','0987654321',1000,'12346']}
for key, value in user_data.items():
    citizen_id = key
    name, account_id, balance, card_id = value
    user = User(citizen_id, name)
    account = Account(user, account_id, balance)
    card = ATMCard(card_id, account, '1234')
    user.addAccount(account)
    account.createCard(card)
    bank.addUser(user)

##################################################################################
#create ATMMachine - Success
atm_data ={'1001':5000,'1002':5000} 
for key, value in atm_data.items():
    new_atm = ATMMachine(key, value)
    bank.addATMMachine(new_atm)

###################################################################################
##TEST
#
#print(bank.ATMMachine[0].machine_id, bank.ATMMachine[0].machine_balance)
#print(bank.ATMMachine[1].machine_id, bank.ATMMachine[1].machine_balance)
#print(bank.user[0].name, bank.user[0].account[0].account_id, bank.user[0].account[0].card.card_id)
#print(bank.user[1].name, bank.user[1].account[0].account_id, bank.user[1].account[0].card.card_id)
#
###################################SUCCESS#########################################
# TODO 1 : จากข้อมูลใน user ให้สร้าง instance โดยมีข้อมูล
# TODO :   key:value โดย key เป็นรหัสบัตรประชาชน และ value เป็นข้อมูลของคนนั้น ประกอบด้วย
# TODO :   [ชื่อ, หมายเลขบัญชี, หมายเลขบัตร ATM, จำนวนเงินในบัญชี]
# TODO :   return เป็น instance ของธนาคาร
# TODO :   และสร้าง instance ของเครื่อง ATM จำนวน 2 เครื่อง
##################################SUCCESS#########################################

##################################SUCCESS#########################################
# TODO 2 : เขียน method ที่ทำหน้าที่สอดบัตรเข้าเครื่อง ATM มี parameter 2 ตัว ได้แก่ 1) instance ของธนาคาร
# TODO     2) atm_card เป็นหมายเลขของ atm_card
# TODO     return ถ้าบัตรถูกต้องจะได้ instance ของ account คืนมา ถ้าไม่ถูกต้องได้เป็น None
# TODO     ควรเป็น method ของเครื่อง ATM
#TEST
#print(bank.ATMMachine[0].insert_card(bank, '12345').account_id)
#print(bank.ATMMachine[0].insert_card(bank, '12346').account_id)
##################################SUCCESS#########################################

##################################SUCCESS#########################################
# TODO 3 : เขียน method ที่ทำหน้าที่ฝากเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account 3) จำนวนเงิน
# TODO     การทำงาน ให้เพิ่มจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0
##################################SUCCESS#########################################

##################################SUCCESS#########################################
#TODO 4 : เขียน method ที่ทำหน้าที่ถอนเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account 3) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี
##################################SUCCESS#########################################

##################################SUCCESS#########################################
#TODO 5 : เขียน method ที่ทำหน้าที่โอนเงิน โดยรับ parameter 4 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account ตนเอง 3) instance ของ account ที่โอนไป 4) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชีตนเอง และ เพิ่มเงินในบัญชีคนที่โอนไป และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี
##################################SUCCESS#########################################

# ##################################################################################
##TEST ALL POOP!!!!!!!!!!!!!
#print(Harry.citizen_id, Harry.name)
#print(Hermione.citizen_id, Hermione.name)
#print(Harry_Account.owner.name, Harry_Account.account_id, Harry_Account.balance)
#print(Harry_Account.owner.name, Hermione_Account.account_id, Hermione_Account.balance)
#print(Harry_Card.pin)
#print(Harry_Card.card_account.account_id)
#print(ATM_1.machine_id, ATM_1.machine_balance)
#print(ATM_2.machine_id, ATM_2.machine_balance)
###################################################################################

##################################SUCCESS#########################################
# Test case #1 : ทดสอบ การ insert บัตร โดยค้นหาเครื่อง atm เครื่องที่ 1 และบัตร atm ของ harry
# และเรียกใช้ function หรือ method จากเครื่อง ATM
# ผลที่คาดหวัง : พิมพ์ หมายเลข account ของ harry อย่างถูกต้อง และ พิมพ์หมายเลขบัตร ATM อย่างถูกต้อง
# Ans : 12345, 1234567890, Success
print("Test case #1 : Test insert card")
atm = bank.get_atm('1001')
account = atm.insert_card("12345", '1234')
if account:
    print(f"{account.account_id}, {account.card.card_id}, Success")
else:
    print("Failed")
print("-------------------------")
##################################SUCCESS#########################################


# Test case #2 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 1000 บาท
# ให้เรียกใช้ method ที่ทำการฝากเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนฝาก หลังฝาก และ แสดง transaction
# Hermione account before test : 1000
# Hermione account after test : 2000
print("Test case #2 : Test deposit")
atm = bank.get_atm('1002')
account = atm.insert_card("12346", '1234')
print(f"Hermione account before test : {account.balance}")
result = atm.deposit(account, 1000)
print(result)
print(f"Hermione account after test : {account.balance}")
print(f"transaction : {account.history_transaction[0].type}-ATM:{account.history_transaction[0].machine_id}-{account.history_transaction[0].amount}-{account.balance}")
print("-------------------------")

# Test case #3 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน -1 บาท
# ผลที่คาดหวัง : แสดง Error
print("Test case #3 : Test deposit Error")
atm = bank.get_atm('1002')
account = atm.insert_card("12346", '1234')
result = atm.deposit(account, -1)
print(result)
print("-------------------------")


# Test case #4 : ทดสอบการถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 500 บาท
# ให้เรียกใช้ method ที่ทำการถอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน และ แสดง transaction
# Hermione account before test : 2000
# Hermione account after test : 1500
print("Test case #4 : Test withdraw")
atm = bank.get_atm('1002')
account = atm.insert_card("12346", '1234')
print(f"Hermione account before test : {account.balance}")
result = atm.withdraw(account, 500)
print(result)
print(f"Hermione account after test : {account.balance}")
print(f"transaction : {account.history_transaction[1].type}-ATM:{account.history_transaction[1].machine_id}-{account.history_transaction[1].amount}-{account.balance}")
print("-------------------------")


# Test case #5 : ทดสอบถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 2000 บาท
# ผลที่คาดหวัง : แสดง Error
print("Test case #5 : Test withdraw Error")
atm = bank.get_atm('1002')
account = atm.insert_card("12346", '1234')
result = atm.withdraw(account, 2000)
print(result)
print("-------------------------")
# Test case #6 : ทดสอบการโอนเงินจากบัญชีของ Harry ไปยัง Hermione จำนวน 10000 บาท ในเครื่อง atm เครื่องที่ 2
# ให้เรียกใช้ method ที่ทำการโอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Harry ก่อนถอน หลังถอน และ แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน แสดง transaction
# Harry account before test : 20000
# Harry account after test : 10000
# Hermione account before test : 1500
# Hermione account after test : 11500
print("Test case #6 : Test transfer")
atm = bank.get_atm('1002')
harry_account = atm.insert_card("12345", '1234')
hermione_account = bank.get_user('1-1101-12345-98-0').get_account('0987654321')
print(f"Harry account before test : {harry_account.balance}")
print(f"Hermione account before test : {hermione_account.balance}")
result = atm.transfer(harry_account, hermione_account, 10000)
print(result)
print(f"Harry account after test : {harry_account.balance}")
print(f"Hermione account after test : {hermione_account.balance}")
print(f"transaction_harry : {harry_account.history_transaction[0].type}-ATM:{harry_account.history_transaction[0].machine_id}-{harry_account.history_transaction[0].amount}-{harry_account.balance}")
print(f"transaction_hermione : {hermione_account.history_transaction[2].type}-ATM:{hermione_account.history_transaction[2].machine_id}-{hermione_account.history_transaction[2].amount}-{hermione_account.balance}")
print("-------------------------")


# Test case #7 : แสดง transaction ของ Hermione ทั้งหมด 
# ผลที่คาดหวัง
# Hermione transaction : D-ATM:1002-1000-2000
# Hermione transaction : W-ATM:1002-500-1500
# Hermione transaction : TD-ATM:1002-10000-11500
print("Test case #7 : Test transaction")
hermione_account = bank.user[1].account[0]
Transactions = hermione_account.get_transaction()
for transaction in Transactions:
    print(f"{transaction.type}-ATM:{transaction.machine_id}-{transaction.amount}-{hermione_account.balance}")
print("-------------------------")

# Test case #8 : ทดสอบการใส่ PIN ไม่ถูกต้อง 
# ให้เรียกใช้ method ที่ทำการ insert card และตรวจสอบ PIN
# atm_machine = bank.get_atm('1001')
# test_result = atm_machine.insert_card('12345', '9999')  # ใส่ PIN ผิด
# ผลที่คาดหวัง
# Invalid PIN
print("Test case #8 : Test invalid PIN")
atm_machine = bank.get_atm('1001')
test_result = atm_machine.insert_card('12345', '9999')
if test_result:
    print("Success")
else:
    print("Invalid PIN")
print("-------------------------")

# Test case #9 : ทดสอบการถอนเงินเกินวงเงินต่อวัน (40,000 บาท)
print("Test case #9 : Test withdraw exceeds daily limit")
atm_machine = bank.get_atm('1001')
account = atm_machine.insert_card('12345', '1234')  # PIN ถูกต้อง
harry_balance_before = account.get_balance()
print(f"Harry account before test: {harry_balance_before}")
print("Attempting to withdraw 45,000 baht...")
atm_machine.machine_balance = 200_000
result = atm_machine.withdraw(account, 45000)
print(f"Expected result: Exceeds daily withdrawal limit of 40,000 baht")
print(f"Actual result: {result}")
print(f"Harry account after test: {account.get_balance()}")
print("-------------------------")

# Test case #10 : ทดสอบการถอนเงินเมื่อเงินในตู้ ATM ไม่พอ
atm_machine = bank.get_atm('1002')  # สมมติว่าตู้ที่ 2 มีเงินเหลือ 200,000 บาท
atm_machine.machine_balance = 200_000
account = atm_machine.insert_card('12345', '1234')
print("Test case #10 : Test withdrawal when ATM has insufficient funds")
print(f"ATM machine balance before: {atm_machine.get_balance()}")
print("Attempting to withdraw 250,000 baht...")
result = atm_machine.withdraw(account, 250000)
print(f"Expected result: ATM has insufficient funds")
print(f"Actual result: {result}")
print(f"ATM machine balance after: {atm_machine.get_balance()}")
print("-------------------------")

