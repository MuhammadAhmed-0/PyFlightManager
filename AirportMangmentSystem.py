class Node:
 def __init__(self,fname,lname,age,gend,contact,email,pnr,deptime,arrtime,flight,date,cargo,cargodes,cargocharges):   #Node to initialize data for seat reservation
  print("Node created")
  self.fname=fname
  self.lname=lname
  self.age=age
  self.gend=gend
  self.contact=contact
  self.email=email
  self.pnr=pnr
  self.deptime=deptime
  self.arrtime=arrtime
  self.flight=flight
  self.date=date

  self.cargo=cargo
  self.cargodes=cargodes
  self.cargocharges=cargocharges

  self.next=None

class Node2:                      # node to initialize data for airport hotels
    def __init__(self, name, phone_no=None, check_in_date=None, check_out_date=None, type_of_room=None, cost=None,room_no=None):
        self.name = name
        self.phone_no = phone_no
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.type_of_room = type_of_room
        self.cost = cost
        self.room_no = room_no
        self.next = None

class Seatreservation:                 #Class for seat reservation
 def __init__(self):       #constructor to initialize the head & data
  self.head=None
  self.fname=None
  self.lname=None
  self.age=0
  self.gend=None
  self.contact=0
  self.email=None
  self.pnr=0
  self.deptime=None
  self.arrtime=None
  self.flight=None
  self.cargo=None
  self.cargodes=None
  self.cargocharges=0
  self.date=0
  self.ctr=0
  self.cargo=None
  self.cargodes=None
  self.cargocharges=0

 def seatreser(self):           #function for reservation of seat/ticket
  print("1.Domestic")
  print("2.International")
  n=int(input("Enter the type of flight:"))

  if n==1:
    self.date=None
    while (self.date!="180122"):
      self.date=input("Enter Date of Journey<DDMMYY>(Please enter a valid date)")
      if (self.date!="180122" and len(self.date)==6):
       print("**No flights available for this date.Try again**")
       print("try: 18012022")
      elif(len(self.date)!=6):
       print("**Invalid Date.Try again**")
    print(" 1.Karachi 2.Lahore 3.Islamabad 4.KPK ")
    
    src=0
    des=0

    while (src>4 or src<=0)or(des>4 or des<=0):             
      src=int(input("Enter source:"))
      des=int(input("Enter destination:"))
      if (src>4 or src<=0)or(des>4 or des<=0):
       print("--Invalid source or destination.Try again--")
    
    if ((src == 1 and des == 2) or (src == 2 and des == 1)): 
     print("                          Flights Found                           ") 
     print("Airline:       Departure:    Arrival:     Price:     Category:    ") 
     print("(1)IIA         08:00         12:05        Rs.5800    Refundable   ")
     print("(2)KJIA        14:00         16:05         Rs.6500    Refundable   ") 
     print("(3)MIA         19:00         22:05        Rs.6000    Refundable   ")
    elif ((src == 1 and des == 3) or (src == 3 and des == 1)): 
     print("                          Flights Found                           ") 
     print("Airline:       Departure:    Arrival:     Price:     Category:    ") 
     print("(1)IIA         08:00         13:05        Rs.5000    Refundable   ")
     print("(2)KJIA        14:00         15:05        Rs.5500    Refundable   ") 
     print("(3)MIA         19:00         21:05        Rs.6000    Refundable   ")
    elif ((src == 1 and des == 4) or (src == 4 and des == 1)): 
     print("                          Flights Found                           ") 
     print("Airline:       Departure:    Arrival:     Price:     Category:    ") 
     print("(1)IIA         08:00         11:05        Rs.4000    Refundable   ")
     print("(2)KJIA        14:00         17:05        Rs.4250    Refundable   ") 
     print("(3)MIA         19:00         20:05        Rs.6100    Refundable   ")
    elif ((src == 2 and des == 3) or (src == 3 and des == 2)): 
     print("                          Flights Found                           ") 
     print("Airline:       Departure:    Arrival:     Price:     Category:    ") 
     print("(1)IIA         08:00         13:05        Rs.5400    Refundable   ")
     print("(2)KJIA        14:00         20:05        Rs.2500    Refundable   ") 
     print("(3)MIA         19:00         19:05        Rs.2890    Refundable   ")
    elif ((src ==2 and des == 4) or (src == 4 and des == 2)): 
     print("                          Flights Found                           ") 
     print("Airline:       Departure:    Arrival:     Price:     Category:    ") 
     print("(1)IIA         08:00         11:05        Rs.5000    Refundable   ")
     print("(2)KJIA        04:00         19:05        Rs.4500    Refundable   ") 
     print("(3)MIA         19:00         18:05        Rs.6000    Refundable   ")
    elif ((src == 3 and des== 4) or (src == 4 and des == 3)): 
     print("                          Flights Found                           ") 
     print("Airline:       Departure:    Arrival:     Price:     Category:    ") 
     print("(1)IIA         08:00         14:05        Rs.5800    Refundable   ")
     print("(2)KJIA        14:00         18:05        Rs.5500    Refundable   ") 
     print("(3)MIA         19:00         17:05        Rs.6050    Refundable   ")

    elif(src==des):
     print("Source and Destination can't be same.Try again")
    else:
      print("Wrong input entered.Try again")
    c=0
    while (c>3 or c<=0)or(c>3 or c<=0):
     c=int(input("Enter your choice:"))
     if (c>3 or c<=0)or(c>3 or c<=0):
       print("--Invalid entry.Try again--")
    
    if ((src==1 and des==2) or (src==2 and des==1)):
     if c==1:
      self.flight="IIA"
      self.deptime="08:00"
      self.arrtime="12:05"
     
     elif c==2:
      self.flight="KJIA"
      self.deptime="14:00"
      self.arrtime="04:05"
     elif c==3:
      self.flight="MIA"
      self.deptime="19:00"
      self.arrtime="21:05"
     else:
      print("Enter a valid choice")
     
    elif ((src==1 and des==3) or (src==3 and des==1)):
     if c==1:
      self.flight="IIA"
      self.deptime="08:00"
      self.arrtime="13:05"
     
     elif c==2:
      self.flight="KJIA"
      self.deptime="14:00"
      self.arrtime="15:05"
     elif c==3:
      self.flight="MIA"
      self.deptime="19:00"
      self.arrtime="21:05"
     else:
      print("Enter a valid choice")
     
    elif ((src==1 and des==4) or (src==4 and des==1)):
     if c==1:
      self.flight="IIA"
      self.deptime="08:00"
      self.arrtime="11:05"
     
     elif c==2:
      self.flight="KJIA"
      self.deptime="14:00"
      self.arrtime="17:05"
     elif c==3:
      self.flight="MIA"
      self.deptime="19:00"
      self.arrtime="20:05"
     else:
      print("Enter a valid choice")
      
    elif ((src==2 and des==3) or (src==3 and des==2)):
     if c==1:
      self.flight="IIA"
      self.deptime="08:00"
      self.arrtime="13:05"
     
     elif c==2:
      self.flight="KJIA"
      self.deptime="14:00"
      self.arrtime="20:05"
     elif c==3:
      self.flight="MIA"
      self.deptime="19:00"
      self.arrtime="23:05"
     else:
      print("Enter a valid choice")
     
    elif ((src==2 and des==4) or (src==4 and des==2)):
     if c==1:
      self.flight="IIA"
      self.deptime="08:00"
      self.arrtime="11:05"
     
     elif c==2:
      self.flight="KJIA"
      self.deptime="14:00"
      self.arrtime="19:05"
     elif c==3:
      self.flight="MIA"
      self.deptime="19:00"
      self.arrtime="21:05"
     else:
      print("Enter a valid choice") 
     
    elif ((src==3 and des==4) or (src==4 and des==3)):
     if c==1:
      self.flight="IIA"
      self.deptime="08:00"
      self.arrtime="14:05"
     
     elif c==2:
      self.flight="KJIA"
      self.deptime="14:00"
      self.arrtime="18:05"
     elif c==3:
      self.flight="MIA"
      self.deptime="19:00"
      self.arrtime="22:05"
     else:
      print("Enter a valid choice") 

    print("---Enter Passenger Details---")
    self.fname=input("Enter first name:")
    self.lname=input("Enter last name:")
    print("Gender:")
    print("For Male press:1")
    print("For Female press:2")
    a=int(input())
    if a==1:
      self.gend="Male"
    else:
      self.gend="Female"
    self.age=int(input("Enter your age:"))
    self.email=input("Enter your email id:")
    self.contact=int(input("Enter your contact no."))
    
    print("---Details Entered---")
    print("Name:",self.fname,self.lname)
    print("Gender:",self.gend)
    print("Age:",self.age)
    print("Email id:",self.email)
    print("Contact no.",self.contact)

    def details(): 
     print("Flight:",self.flight)  
     print("Name:",self.fname,self.lname)
     print("Departure time:",self.deptime)
     print("Arrival time:",self.arrtime)
     print("Date of flight is:",self.date)
  
    print("How would you like to pay:")
    print("1.Debit card")
    print("2.Credit card")
    print("3.Net Banking")
    ch=0
    while (ch>3 or ch<=0)or(ch>3 or ch<=0):
     ch=int(input("Enter your choice:"))
     if (ch>3 or ch<=0)or(ch>3 or ch<=0):
       print("--Invalid choice.Try again--")
      
    if(ch==1):
       cvv=input("Enter CVV number:")
       cno=input("Enter card no.")
       expdate=input("Enter expiry data:")
       print("---Transaction Successfull---")
       self.pnr=self.pnr+1
       print("PNR:",self.pnr)
       details()
      
    elif ch==2:
       cno=input("Enter card no.")
       expdate=input("Enter expiry data:")
       password=input("Enter Password:")
       print("---Transaction Successfull---")
       self.pnr=self.pnr+1
       print("PNR:",self.pnr)
       details()
    elif ch==3:
       print("Banks available:")
       print("1.Habib Bnak Limited")
       print("2.Allied Bank")
       print("3.National Bank")
       print("4.Others")
       bank=input("Select your bank:")
       print("You have selected:",bank)

       id=input("Enter user id:")
       password=input("Enter password:")
       print("---Transaction Successfull---")
       self.pnr=self.pnr+1
       print("PNR:",self.pnr)
       details()
    else:
      print("--Enter a valid choice--")
      

  elif(n==2):
    self.date=None
    while (self.date!="18012022"):
      self.date=input("Enter Date of Journey<DDMMYY>(Please enter a valid date)")
      if (self.date!="18012022" and len(self.date)==8):
       print("**No flights available for this date.Try again**")
       print("try: 18012022")
      elif(len(self.date)!=8):
       print("**Invalid Date.Try again**")
    print(" 1.Dubai 2.Singapore 3.London 4.New York ")
    src=0
    des=0
    while (src>4 or src<=0)or(des>4 or des<=0):
      src=int(input("Enter source:"))
      des=int(input("Enter destination:"))
      if (src>4 or src<=0)or(des>4 or des<=0):
       print("Invalid source or destination.Try again")
    if ((src == 1 and des == 2) or (src == 2 and des == 1)): 
     print("                          Flights Found                           ") 
     print("Airline:       Departure:    Arrival:     Price:     Category:    ") 
     print("(1)Airblue       12:00        14:05      Rs.25000    Refundable   ")
     print("(2)Shaheen       14:00        18:05      Rs.21500    Refundable   ") 
     print("(3)PIA           18:00        22:05      Rs.24000    Refundable   ")
    elif ((src == 1 and des == 3) or (src == 3 and des == 1)): 
     print("                          Flights Found                           ") 
     print("Airline:       Departure:    Arrival:     Price:     Category:    ") 
     print("(1)Airblue       12:00        15:05      Rs.25500    Refundable   ")
     print("(2)Shaheen       14:00        20:05      Rs.21300    Refundable   ") 
     print("(3)PIA           18:00        22:05      Rs.24650    Refundable   ")
    elif ((src == 1 and des == 4) or (src == 4 and des == 1)): 
     print("                          Flights Found                           ") 
     print("Airline:       Departure:    Arrival:     Price:     Category:    ") 
     print("(1)Airblue       12:00        17:05      Rs.52500    Refundable   ")
     print("(2)Shaheen       14:00        18:05      Rs.59420    Refundable   ") 
     print("(3)PIA           18:00        21:05      Rs.64892    Refundable   ")
    elif ((src ==2 and des == 3) or (src == 3 and des == 2)): 
     print("                          Flights Found                           ") 
     print("Airline:       Departure:    Arrival:     Price:     Category:    ") 
     print("(1)Airblue       12:00        14:05      Rs.20000    Refundable   ")
     print("(2)Shaheen       14:00        17:05      Rs.18000    Refundable   ") 
     print("(3)PIA           18:00        22:05      Rs.17500    Refundable   ")
    elif ((src == 2 and des== 4) or (src == 4 and des == 2)): 
     print("                          Flights Found                           ") 
     print("Airline:       Departure:    Arrival:     Price:     Category:    ") 
     print("(1)Airblue       12:00        16:05      Rs.30000    Refundable   ")
     print("(2)Shaheen       14:00        16:05      Rs.34000    Refundable   ") 
     print("(3)PIA           18:00        23:05      Rs.28000    Refundable   ")
    elif ((src == 3 and des== 4) or (src == 4 and des == 3)): 
     print("                          Flights Found                           ") 
     print("Airline:       Departure:    Arrival:     Price:     Category:    ") 
     print("(1)Airblue       12:00        15:05      Rs.60000    Refundable   ")
     print("(2)Shaheen       14:00        18:05      Rs.58000    Refundable   ") 
     print("(3)PIA           18:00        23:05      Rs.54500    Refundable   ")
    
    elif(src==des):
     print("Source and Destination can't be same.Try again")
    else:
      print("Wrong input entered.Try again")
    c=0
    while (c>3 or c<=0)or(c>3 or c<=0):
     c=int(input("Enter your choice:"))
     if (c>3 or c<=0)or(c>3 or c<=0):
       print("Invalid entry.Try again")
    if ((src==1 and des==2) or (src==2 and des==1)):
     if c==1:
      self.flight="Airblue"
      self.deptime="12:00"
      self.arrtime="14:05"
     
     elif c==2:
      self.flight="Shaheen"
      self.deptime="14:00"
      self.arrtime="18:05"
     elif c==3:
      self.flight="PIA"
      self.deptime="18:00"
      self.arrtime="22:05"
     else:
      print("Enter a valid choice")
   
    elif ((src==1 and des==3) or (src==3 and des==1)):
     if c==1:
      self.flight="Airblue"
      self.deptime="12:00"
      self.arrtime="17:05"
      
     elif c==2:
      self.flight="Shaheen"
      self.deptime="14:00"
      self.arrtime="18:05"
     elif c==3:
      self.flight="PIA"
      self.deptime="18:00"
      self.arrtime="21:05"
     else:
      print("Enter a valid choice")
   

    elif ((src==1 and des==3) or (src==3 and des==1)):
     if c==1:
      self.flight="Airblue"
      self.deptime="12:00"
      self.arrtime="14:05"
      self.inflgihts()
     elif c==2:
      self.flight="Shaheen"
      self.deptime="14:00"
      self.arrtime="18:05"
     elif c==3:
      self.flight="PIA"
      self.deptime="18:00"
      self.arrtime="22:05"
     else:
      print("Enter a valid choice")
     
    elif ((src==2 and des==3) or (src==3 and des==2)):
     if c==1:
      self.flight="Airblue"
      self.deptime="12:00"
      self.arrtime="14:05"
     
     elif c==2:
      self.flight="Shaheen"
      self.deptime="14:00"
      self.arrtime="17:05"
     elif c==3:
      self.flight="PIA"
      self.deptime="18:00"
      self.arrtime="22:05"
     else:
      print("Enter a valid choice")
     
    elif ((src==2 and des==4) or (src==4 and des==2)):
     if c==1:
      self.flight="Airblue"
      self.deptime="12:00"
      self.arrtime="16:05"
     
     elif c==2:
      self.flight="Shaheen"
      self.deptime="14:00"
      self.arrtime="16:05"
     elif c==3:
      self.flight="PIA"
      self.deptime="18:00"
      self.arrtime="23:05"
     else:
      print("Enter a valid choice")
     
    elif ((src==3 and des==4) or (src==4 and des==3)):
     if c==1:
      self.flight="Airblue"
      self.deptime="12:00"
      self.arrtime="15:05"
     
     elif c==2:
      self.flight="Shaheen"
      self.deptime="14:00"
      self.arrtime="18:05"
     elif c==3:
      self.flight="PIA"
      self.deptime="18:00"
      self.arrtime="23:05"
     else:
      print("Enter a valid choice")
 
    print("---Enter Passenger Details---")
    self.fname=input("Enter first name:")
    self.lname=input("Enter last name:")
    print("Gender:")
    print("For Male press:1")
    print("For Female press:2")
    a=int(input())
    if a==1:
      self.gend="Male"
    else:
      self.gend="Female"
    self.age=int(input("Enter your age:"))
    self.email=input("Enter your email id:")
    self.contact=int(input("Enter your contact no."))
    
    print("---Details Entered---")
    print("Name:",self.fname,self.lname)
    print("Gender:",self.gend)
    print("Age:",self.age)
    print("Email id:",self.email)
    print("Contact no.",self.contact)
    
    def details():
     print("Flight:",self.flight)  
     print("Name:",self.fname,self.lname)
     print("Departure time:",self.deptime)
     print("Arrival time:",self.arrtime)


    print("How would you like to pay:")
    print("1.Debit card")
    print("2.Credit card")
    print("3.Net Banking")
    ch=0
    while (ch>3 or ch<=0)or(ch>3 or ch<=0):
     ch=int(input("Enter your choice:"))
     if (ch>3 or ch<=0)or(ch>3 or ch<=0):
       print("--Invalid choice.Try again--")
      
    if(ch==1):
       cvv=input("Enter CVV number:")
       cno=input("Enter card no.")
       expdate=input("Enter expiry data:")
       print("---Transaction Successfull---")
       self.pnr+=1
       print("PNR:",self.pnr)
       details()
      
    elif ch==2:
       cno=input("Enter card no.")
       expdate=input("Enter expiry data:")
       password=input("Enter Password:")
       print("---Transaction Successfull---")
       self.pnr+=1
       print("PNR:",self.pnr)
       details()
    elif ch==3:
       print("Banks available:")
       print("1.Habib Bnak Limited")
       print("2.Allied Bank")
       print("3.National Bank")
       print("4.Others")
       bank=input("Select your bank:")
       print("You have selected:",bank)

       id=input("Enter user id:")
       password=input("Enter password:")
       print("---Transaction Successfull---")
       self.pnr+=1
       print("PNR:",self.pnr)
       details()
    else:
      print("--Enter a valid choice--")
 
  node=Node(self.fname,self.lname,self.age,self.gend,self.contact,self.email,self.pnr,self.deptime,self.arrtime,self.flight,self.date,self.cargo,self.cargodes,self.cargocharges)
  return node
 def insert(self):
      node1=self.seatreser()
      if self.head==None:
        self.head=node1
      else:
        temp=self.head
        while (temp.next is not None):
          temp=temp.next
        temp.next=node1
 def checkticket(self,pos):      
             #function to check the ticket of given PNR number
    if self.head==None:
       print("**No record exists**")
    else:
     temp=self.head
     while True:
        if pos==temp.pnr:
         print("Name:",temp.fname,temp.lname)
         print("Gender:",temp.gend)
         print("Email id:",temp.email)
         print("Date of flight:",temp.date)
         print("Flight:",temp.flight)  
         print("Departure time:",temp.deptime)
         print("Arrival time:",temp.arrtime)
         n=1
         break;
        if temp.next is None:
          print("***No record found with given PNR number***")
          break;
        else:
         temp=temp.next

 def cancelticket(self,pos):                  #function to cancel the ticket/to delete the node
  i=1                                        #take variable i to find the number of node to be deleted and intitialize it with zero
  do='no'                                    #take variable do to check whether the node is found or not and intitialize it with no
  if self.head==None:                       #first check that head is none
    print("***No record exists***")
  else:                                  #if head is not none then start traversing
   temp=self.head                         #take temporary node temp and assign it with head
   while True:                             #run an while loop
    if pos==temp.pnr:                   
      do='yes'                                  #if the given pnr number is found then declare do with yes and break the loop
      break;                                             
    if temp.next is None:
        print("**No record exists with given pnr number**")       
        break;                                        #if list is ended and no record found then break the loop
    else:
      i+=1                                              #increment i with 1       
      temp=temp.next                                  #if list is ended and no record found then break the loop
      
  if i==1 and do=='yes':                          #this loop will check if i is 1 and whether record was founded
    if temp.next is None:                             #if there is only head in linked list then make the head none
      self.head=None
      print("***Ticket with PNR:",pos," is cancelled***")
    else:                                         #if more than one node exists then make the second node head
      self.head=self.head.next 
      print("***Ticket with PNR:",pos," is cancelled***")
  if i>1 and do=='yes':                         #if i greater than 1 and recorded was founded then this loop will run
     if temp.next is None:                         #if temp is none then it means we have to delete the last node
       temp1=self.head                                   #we will traverse through list and after reaching on second last node we will make its next none
       for j in range(i-2):
         temp1=temp1.next
       temp1.next=None                                               #the last node will be deleted
       print("***Ticket with PNR:",pos," is cancelled***")
     else:                                      #else the node to be deleted was node in middle
      temp1=self.head                             #traverse through list and take your prev on node behind the node to be deleted
      prev=None
      for j in range(i-1):                 #traverse through list
        prev=temp1                        #at end prev will be on node behind the node to be deleted
        temp1=temp1.next                  #at end of loop temp will be on node to be deleted
      prev.next=temp1.next                #make next of prev equals to next of next of temp
      temp1.next=None                         #make next of temp equals to none
      print("***Ticket with PNR:",pos," is cancelled***")                      #node will be deleted 

 def travellersinfo(self):                  #this function will display all the tickets data(usable for administration)
    if self.head==None:
     print("***No record exist***")
    else:
     temp=self.head
     while True:
         print("****************************")
         print("Name:",temp.fname,temp.lname)
         print("Gender:",temp.gend)
         print("Email id:",temp.email)
         print("Date of flight:",temp.date)
         print("Flight:",temp.flight)  
         print("Departure time:",temp.deptime)
         print("Arrival time:",temp.arrtime)      
         if temp.next is None:
           break;
         else:
          temp=temp.next
 def cargoservices(self):
  n=0
  while(n!=1):
   firstname=input("Enter your first name:")
   lastname=input("Enter your last name:")
   pnr=int(input("Enter your PNR number:"))
   if self.head==None:
     print("***No record exist***")
   else:
     temp=self.head
     while True:
        if(firstname==temp.fname and lastname==temp.lname and pnr==temp.pnr):
          n=1
          print("**Record found**")
          break;
        if temp.next is None:
           break;
        else:
          temp=temp.next
     if(n!=1):
          print("**No record found with given data.Kindly renter**")
        
       
  self.cargodes=input("Enter your country from:-  .Dubai .Singapore .London .New York")
  print("What kind of package do you want to send:")
  print("1.Luggage 2.Car 3.Mail")
  c=0
  while (c>3 or c<1):
     c=int(input("Enter your choice:"))
     if (c>3 or c<1):
       print("Invalid entry.Try again")
  if c==1:
    self.cargo="Luggage"
    size=int(input("Enter the size of Luggage:"))
    print("***weight per kg=75$***")
    quant=int(input("Enter quantity:"))
    self.cargocharges=quant*75
    print("Your cargo charges are:",self.cargocharges,"$")
  elif c==2:
    self.cargo="Car"
    print("1.Light weight 2.Heavy weight 3.Motorcycles")
    v=int(input("***Select type of vehicle***"))
    if v==1:
      print("**Charges for light vehicle are:2500$**","$")
      quant=int(input("Enter quantity:"))
      self.cargocharges=quant*2500
      print("Your cargo charges are:",self.cargocharges)
    elif v==2:
      print("**Charges for heavy vehicle are:3500$**")
      quant=int(input("Enter quantity:"))
      self.cargocharges=quant*3500
      print("Your cargo charges are:",self.cargocharges,"$")
    elif v==3:
      print("**Charges for motorcycle are:1000$**")
      quant=int(input("Enter quantity:"))
      self.cargocharges=1000
      print("Your cargo charges are:",self.cargocharges,"$") 
  elif c==3:
     address=input("Enter your address:")
     self.cargo="Mail"
     self.cargocharges=100
     print("Your cargo charges are:",self.cargocharges,"$") 
  if self.head==None:
     print("***No record exist***")
  else:
     temp=self.head
     while True:
        if(self.fname==temp.fname and self.lname==temp.lname and self.pnr==temp.pnr):
          temp.cargo=self.cargo
          temp.cargodes=self.cargodes
          temp.cargocharges=self.cargocharges
          print("***Details Entered***")
          print("Name:",temp.fname," ",temp.lname)
          print("PNR number:",temp.pnr)
          print("Type of cargo:",temp.cargo)
          print("Cargo destination:",temp.cargodes)
          print("Cargo charges:",temp.cargocharges,"$")
          break;
        else:
          temp=temp.next
#initializing data for airport hotels
firstclass_rooms = [6, 7, 8, 9]
executive_rooms = [1, 2, 3, 4, 5]
economy_rooms = [10, 11, 12, 13, 14]

fir_occ = []
ex_occ = []
eco_occ = []

class hotel:

    def __init__(self):
        self.head = None

    def insertion(self, name=None, phone_no=None, check_in_date=None, check_out_date=None, type_of_room=None,
                  cost=None):
        node = Node2(name, phone_no, check_in_date, check_out_date, type_of_room, cost)
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = node

    def airporthotels(self):
        firstclass_rooms = [6, 7, 8, 9]
        executive_rooms = [1, 2, 3, 4, 5]
        economy_rooms = [10, 11, 12, 13, 14]

        fir_occ = []
        ex_occ = []
        eco_occ = []

        def checkedin():
            cost = ("")
            room_no = (" ")
            print("Checking IN ")
            name = input("Name  ")
            phone_no = input("phone no. ")
            check_in_date = input("Check in date  ")
            check_out_date = input("Check out date ")
            print("1. First class    ")
            print("2. executive class")
            print("3. economy class  ")
            print("4. Exit")
            type_of_room = int(input(" select "))
            # instance.insertion(name, phone_no, check_in_date, check_out_date, type_of_room, cost, room_no)
            if type_of_room == 1:
                cost = '300$'

            elif type_of_room == 2:
                cost = '100$'

            elif type_of_room == 3:
                cost = '50$'
            elif type_of_room == 4:
                print("exit")
            print("*****Details entered*****")
            print("Name:",name)
            print("Phone no.",phone_no)
            print("Check in date:",check_in_date)
            print("Check our date:",check_out_date)
            print("Type of room:",type_of_room)
            print("Cost:",cost)

            self.insertion(name, phone_no, check_in_date, check_out_date, type_of_room, cost)



        print("_______HOTEL RESERVATION_______")
        print("1. Check IN ")
        print("2. Check out ")
        print("3. Exit")
        end = 'n'
        select = int(input("Select  "))

        if select == 1:
            checkedin()
        elif select == 2:
            end = 'y'
            print("Exit")
        else:
            print("Invalid selection")


def menu():
  print("                                  Welcome To IST Flight Reservation System                    ")
  print("                               **********************************************                 ")
  print("                               Book Your Flight Tickets at affordable prices!                 ")
  print("                               **********************************************                 ")
  print("                                             ******MENU******                                 ")
  print("                                            1.Seat Reservation                                ")
  print("                                            2.Checking Tickets                                ")
  print("                                            3.Ticket Cancellaton                              ")
  print("                                            4.Cargo Services                                  ")
  print("                                            5.Airport hotels                                  ")
  print("                                            6.Traveller's Information                         ")
  print("                                            7.Exit                                            ")
  c=int(input("Enter choice:"))
  return c


l=Seatreservation()
k=hotel()
m=Seatreservation()
while True:
 ch=menu()
 if ch==1:
  l.insert()
 elif ch==2:
  pos=int(input("Enter your PNR number:"))
  l.checkticket(pos)
 elif ch==3:
  n=int(input("Enter PNR number of ticket that you want to cancel:"))
  l.cancelticket(n)
 elif ch==6:
  l.travellersinfo()
 elif ch==4:
  l.cargoservices()
 elif ch==5:
  k.airporthotels()
 elif ch==7:
  print("Exit")
  break;
 else:
   print("--Please enter a valid choice--")