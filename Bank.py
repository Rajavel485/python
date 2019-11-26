import random

class Bank:
    def end(self):
        pass

    def name(self):
        na=input("Enter the name:")
        if na=='0':
            return na
        for i in na:
            if ord(i) not in range(65,123):
                print("Name does'nt contains anything other than alphabets\n") 
                return self.name()
        return na

    def pin(self):
        try:
            pword=int(input("Enter the PIN no:"))
            if pword==0:
                return pword
            if len(str(pword))!=4:
                print('A PIN number is a combination of 4 numbers\nSo try again\n')
                return self.pin()
            return pword
        except ValueError:
            print("\nEnter the correct PIN number\n")
            return self.pin()

    def withdrawl(self):
        try:
            w_amount=int(input("\nEnter the withdrawl amount: "))
            if self.d['bal'] - w_amount <= 5000:
                print("Insuffient Account balance")
                return self.menu()
            else:
                self.d['bal']-=w_amount
                self.d['acty'].append('Withdrawn: {} Remaining: {}'.format(w_amount,self.d['bal']))
                return self.details()
        except ValueError:
            print('Type an integer\nTry again\n')
            return self.withdrawl()

    def deposit(self):
        try:
            D_amount=int(input("\nEnter the deposit amount:"))
            if D_amount < 1000:
                print("Amount should be more than 1000")
                return self.deposit()
            else:
                self.d['bal']+=D_amount
                self.d['acty'].append('Deposited: {} Remaining: {}'.format(D_amount,self.d['bal']))
                return self.details()
        except ValueError:
            print('Type an integer')
            return self.deposit()

    def details(self):
        print("\nAccount Details:")
        print("\nName:",self.d['name'],"\nPhone no:",self.d['phno'],"\nAccount no:",self.d['acc_id'],"\nTotal Amount:",self.d['bal'])
        input("\nPress ENTER to continue")
        return self.menu()

    def mstatement(self):
        print('Your name: '+self.d['name'])
        print('Your phone number:',self.d['phno'],'\n')
        print('Your activities'.center(25,'*'))
        for i in range(1,len(self.d['acty'])+1):
            print(str(i)+'.'+self.d['acty'][i-1])
            
        input('Enter to continue')
        return self.menu()

    def menu(self):
        try:
            print("1.Withdrawl \n2.Deposit \n3.Show Details \n4.Ministatement\n"+"0 to enter welcome page".center(25,'*'))
            ch=int(input("\nEnter your choice: "))
            if ch==1:
                return self.withdrawl()
            elif ch==2:
                return self.deposit()
            elif ch==3:
                return self.details()
            elif ch==4:
                return self.mstatement()
            elif ch==0:
                return self.end()
            else:
                print("\nEnter the correct choice:")
            return self.menu()

        except ValueError:
            print('Type an valid integer')
            return self.menu()
    


    def login(self):
        print('You are about to login'.center(50,'*'))
        print('0 to enter welcome screen'.center(25,'*'))
        P_name=self.name()
        pinno=self.pin()
        if P_name=='0' or pinno==0:
            return self.end()

        if ((P_name == self.d['name']) and (pinno == self.d['PIN'])):
            self.d['acty'].append('logged in')
            self.menu()
        else:
            print("\nInvalid account number or PIN\nTry again\n")
            return self.login()

    def create(self,phno):
        self.d={}
        self.d['phno']=phno
        self.d['acty']=[]
        self.d['bal']=10000
        self.d['acc_id']=random.randint(1000000000000000,9999999999999999)
        print('ACCOUNT ID: {}'.format(self.d['acc_id']))

        namerun=True
        while namerun:
            namerun=False
            self.d['name']=input('Enter your name: ')
            if self.d['name'].strip()=='':
                print('Type something\n')
                namerun=True
                continue
            for i in self.d['name'].lower():
                if not 97<=ord(i)<=122:
                    print('Enter a valid name (without numbers or symbols)\n')
                    namerun=True
                    break
    
        
        pinrun=True
        while pinrun:
            pinrun=False
            try:
                self.d['PIN']=int(input('Type your own PIN number: '))
            except ValueError:
                print('Type numbers not characters')
                pinrun=True
                continue
            if self.d['PIN']<0:
                print('Enter a positive interger')
                pinrun=True
                continue
            elif len(str(self.d['PIN']))!=4:
                print('A PIN contains 4 numbers\nTry again')
                pinrun=True
                continue

        print('Created Successfully')



users=[]
usercount=-1
ph=[]
def start():
    beginrun=True
    while beginrun:
        beginrun=False
        try:
            ch=int(input(('WELCOME'.center(50,'*')+'\nEnter your choice with numbers\n1.CREATE NEW ACCOUNT\n2.LOGIN\n\n'+'0 to exit'.center(25,'*'))))
        except ValueError:
            print('Only numbers are allowed')
            beginrun=True
            continue
        if ch==1:
            global usercount
            usercount+=1
            phrun=True
            while phrun:
                phrun=False
                try:
                    phno=int(input('Type your phone number: '))
                except ValueError:
                    print('A phone number contains only numbers, not anything else\n')
                    phrun=True
                    continue
                if str(phno).strip=='':
                    print('Type something\n')
                    phrun=True
                    continue
                if len(str(phno))!=10:
                    print('A phone number is a combination of 10 numbers not more or less than that\n')
                    phrun=True
                    continue
                if phno in ph:
                    print('Existing number\nTry another')
                    phrun=True
                    continue
                ph.append(phno)
            users.append(Bank())
            users[usercount].create(phno)
            print("You're logged in\n")
            users[usercount].menu()
            return start()
        elif ch==2:
            if usercount==-1:
                print('No users created yet')
                return start()
            print('You are about to login'.center(50,'*'))
            logrn=True
            while logrn:
                logrn=False
                try:
                    A_no=int(input('0 to exit\nType your account number: '))
                except ValueError:
                    print('Only numbers')
                    logrn=True
                if A_no==0:
                    return start()
                for i in range(usercount+1):
                    if users[i].d['acc_id']==A_no:
                        users[i].login()
                        return start()
                    else:
                        print('Not in list\n0 to exit')
                        logrn=True
                        continue

        elif ch==0:
            print('Have a nice day'.center(50,'*'))
            return
                        
        else:
            print('Invalid choice')
            beginrun=True
            continue

start()
