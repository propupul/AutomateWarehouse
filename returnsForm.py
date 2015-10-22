import csv #imports csv module
import time #import time module for the sub_Time
from PythonsublimeCS import cs_inventory # Dictionary containing CS location(Do not open!) will be used in the future.

packageReturns = {} # appends the amount of packackes returned 
stuff = []
# The below code is sitting in a while loop. (while True)
while True:
    with open('Returns.csv', 'a') as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)

        datime = time.strftime("%I:%M:%S")
        date = time.strftime("%d/%m/%Y")


        print("Submission Time:",date,datime)
        sub_Time = (date,datime) # puts sub_Time in a tuple
        cust_Name = input("Customer Name: ")
        order_Num = input("Order Number: ")
        email = input("Email: ")
        zip_Code = input("Zip: ")
        damage = input("Damage Defective: ")

        while True:
            
            items_returned = input(str("Items to be Returned: "))
            
            if items_returned == '':
                break

            
            stuff = stuff + [items_returned]
            stuff.sort()

            

            
            
            
            

        # DEBUGGER print(len(stuff))
        print("This is what you entered: ",stuff)
        
        quantity = print("Quantity: ",len(stuff)) # Had to make this a print statement inside var quantity
        notes_Defective = input("Notes - if defective: ")
        status = input("Status: ")
        resaleable = input("Resaleable: ")
        inventory_Updated = input("Inventory Updated: ")
        return_Date = input("Return Date: ")

      
            
        refund_Amount = input("Refund Amount: ")
    
        return_Shipping = input("return shipping: ")
        
        replacement_Cost = input("replacement cost: ")
        
        replacement_shipping = input("replacement shipping: ")

        try:
   
                
            total = int(refund_Amount) + int(return_Shipping) + int(replacement_Cost) + int(replacement_shipping)
            total = print("Total:"'$',total)
        
        except ValueError:
            total = 0
            print("Continue")
       
            
 
        notes = input("notes: ")
        received_by = input("Received by: ")

        
    
        w.writerow([sub_Time, cust_Name, order_Num, email, zip_Code, damage, stuff,
                    quantity, notes_Defective, status, resaleable, inventory_Updated, return_Date,
                    refund_Amount, return_Shipping, replacement_Cost, replacement_shipping, total, notes,
                    received_by])





    """
    Keeps count of any returns that have been done with this script, and puts them in a dictionary file -dailyReturns.csv
    {Order# : date}
    """

    with open('dailyRetuns.csv', 'a') as f:
        w2 = csv.writer(f, quoting=csv.QUOTE_NONE)

        packageReturns[order_Num] = date
        w2.writerow([packageReturns])





        

        #value 'stuff' replaced the items_returned after 'damage'

        question = input("Do you need to do another return?(yes/no)'")

        if question == 'yes':
            continue
        else:
            print("No problem, Ill see you later")
            break


