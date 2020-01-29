
"""

Code Challenge
  Name: 
    Post Codes UK
  Filename: 
    postcodes_uk.py
  Problem Statement:
    We write an expression, which is capable of recognizing the postal codes or postcodes of the UK.

    Postcode units consist of between five and seven characters, 
    which are separated into two parts by a space. 
    
    The two to four characters before the space represent the so-called outward 
    code or out code intended to direct mail from the sorting office to the delivery office. 
    
    The part following the space, which consists of a digit followed by two uppercase characters, 
    comprises the so-called inward code, which is needed to sort mail at the final delivery office. 
    
    The last two uppercase characters do not use the letters CIKMOV, 
    so as not to resemble digits or each other when hand-written.

    The outward code can have the form: One or two uppercase characters, 
    followed by either a digit or the letter R, 
    optionally followed by an uppercase character or a digit. 
    (We do not consider all the detailed rules for postcodes, 
    i.e only certain character sets are valid depending on the position 
    and the context.)    
  Hint: 
    Using Regular Expression 
  Input:
      example_codes = ["SW1A 0AA", # House of Commons
                 "SW1A 1AA", # Buckingham Palace
                 "SW1A 2AA", # Downing Street
                 "BX3 2BB", # Barclays Bank
                 "DH98 1BT", # British Telecom
                 "N1 9GU", # Guardian Newspaper
                 "E98 1TT", # The Times
                 "TIM E22", # a fake postcode
                 "A B1 A22", # not a valid postcode
                 "EC2N 2DB", # Deutsche Bank
                 "SE9 2UG", # University of Greenwhich
                 "N1 0UY", # Islington, London
                 "EC1V 8DS", # Clerkenwell, London
                 "WC1X 9DT", # WC1X 9DT
                 "B42 1LG", # Birmingham
                 "B28 9AD", # Birmingham
                 "W12 7RJ", # London, BBC News Centre
                 "BBC 007" # a fake postcode
                ]

"""
i=0
while(i<18):
    import re
    code=input("Enter the code:")
    i+=1
    rx=re.search("[A-Z0-9]{2,4}\s[0-9][^CIKMOV0-9]{2}",code)
    '[A-Z]{1,2}[0-9|R]{1,2}\s[0-9][^CIKMOV0-9]{2}]'
    if rx:
        print("Valid")
    else:
        print("Invalid")


"""
output=====================================================================

Enter the code:SW1A 0AA
Valid

Enter the code:SW1A 1AA
Valid

Enter the code:SW1A 2AA
Valid

Enter the code:BX3 2BB
Valid

Enter the code:DH98 1BT
Valid

Enter the code:N1 9GU
Valid

Enter the code:E98 1TT
Valid

Enter the code:TIM E22
Invalid

Enter the code:A B1 A22
Invalid

Enter the code:EC2N 2DB
Valid

Enter the code:SE9 2UG
Valid

Enter the code:N1 0UY
Valid

Enter the code:EC1V 8DS
Valid

Enter the code:WC1X 9DT
Valid

Enter the code:B42 1LG
Valid

Enter the code:B28 9AD
Valid

Enter the code:W12 7RJ
Valid

Enter the code:BBC 00
Invalid
"""






