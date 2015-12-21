import csv #imports csv module
from time import gmtime, strftime #import time module for the sub_Time
from PythonsublimeCS import cs_inventory # Dictionary containing CS location(Do not open!) will be used in the future.
import time


packageReturns = {} # appends the amount of packages returned 
stuff = []
# The below code is sitting in a while loop. (while True)
while True:
    with open('Returns.csv', 'a') as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)

        date = strftime('%a, %b %d %Y at %H:%M:%S', gmtime()) # Imported from the time module.
        date2 = strftime('%a, %b %d %Y', gmtime()) # Imported from the time module for the "return_Date" variable


        print("Submission Time:",date)
        sub_Time = (date) 
        cust_Name = input("Customer Name: ")
        order_Num = input("Order Number: ")
        email = input("Email: ")
        zip_Code = input("Zip: ")
        damage = input("Damage Defective: ")

        while True:
            
            items_returned = input("Items to be Returned: ")
            
            if not items_returned:
                break

            
            stuff.append(items_returned)
        stuff.sort()
            

            

            
            
            
            

        # DEBUGGER print(len(stuff))
        print("This is what you entered: ",stuff)
        print("Quantity: ",len(stuff))   # PLEASE NOTE: DO NOT PUT PRINT STATEMENS INSIDE A VARIABLE NOT A GOOD IDEA. IT WILL CONFUSE YOU.
        quantity = len(stuff)       # Make sure you use the len() for the list to give you the lenght of it.
        notes_Defective = input("Notes - if defective: ")
        status = input("Status: ")
        resaleable = input("Resaleable: ")
        inventory_Updated = input("Inventory Updated: ")

        
        print("Is the return date today? y/n")
        return_Date = input()
        if return_Date.lower() =='y':
            return_Date = date2
        else:
            return_Date = input("Enter Return Date: ")
      
            
        refund_Amount = input("Refund Amount: ")
    
        return_Shipping = input("return shipping: ")
        
        replacement_Cost = input("replacement cost: ")
        
        replacement_shipping = input("replacement shipping: ")

        try:
   
                
            total = int(refund_Amount) + int(return_Shipping) + int(replacement_Cost) + int(replacement_shipping)
            print("the total is",'$' + str(total))  # PLEASE NOTE: DO NOT PUT PRINT STATEMENS INSIDE A VARIABLE NOT A GOOD IDEA. IT WILL CONFUSE YOU.
 
        except ValueError:
            total = 0
            print("Continue")
       
            
 
        notes = input("notes: ")
        received_by = input("Received by: ")

        
    
        w.writerow([sub_Time, cust_Name, order_Num, email, zip_Code, damage, stuff,
                    quantity, notes_Defective, status, resaleable, inventory_Updated, return_Date,
                    refund_Amount, return_Shipping, replacement_Cost, replacement_shipping, total, notes,
                    received_by])
        # value 'stuff' replaced the 'items_returned' after 'damage'





    """
    Keeps count of any returns that have been done with this script, and puts them in a dictionary file -dailyReturns.csv
    {Order# : date}
    """
    #Currently not working - below
    with open('dailyReturns.csv', 'a') as f:
        w2 = csv.writer(f, delimiter='"',quoting=csv.QUOTE_NONE, quotechar='') # When quoting=csv.QUOTE_NONE csv error:need to escape popped.

        packageReturns[order_Num] = date
        w2.writerow([packageReturns])





        

        

    question = input("Do you need to do another return?(yes/no)")

    if question == 'yes':
        continue
    else:
        print("No problem, Ill see you later")
        break


