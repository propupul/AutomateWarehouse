#! /usr/bin/env python3

# Small programs that compares string values
# If they are equal message will pop. Same for difference

import time


print("Welcome, this program will run forever. If you need to exit please hit enter twice.")
time.sleep(1)
print('......')



while True:

    
    
    print('Please Scan the location SKU')
    input1 = str(input(''))
    print('Please scan the item SKU')

    input2 = str(input(''))

    if input1 == input2:
        print('Values are the same! Please put the product away.')

    else:
        print('THE SKUs DO NOT MATCH, CHECK THE ITEM!')


