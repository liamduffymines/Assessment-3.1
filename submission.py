#Liam Duffy 
#Assessment 3
#CSCI 128
#Time: 2.5 Hours 


#Inputs
Primarybloodbank = input().split(" ")
Secondarybloodbank = input().split(" ")
Bloodtypes = input()
Amount = int(input())

#Specific Blood Type Amounts
Primaryblood = Primarybloodbank.index(Bloodtypes)
Primebloodtotal = int(Primarybloodbank[Primaryblood+1])
Secondaryblood = Secondarybloodbank.index(Bloodtypes)
Secondarybloodtotal = int(Secondarybloodbank[Secondaryblood+1])

#Total Blood/Amount Left
totalamount = int(Secondarybloodtotal + Primebloodtotal)
Amountleft = int(Secondarybloodtotal + Primebloodtotal - Amount)

#Outputs
if totalamount < Amount:
    print("OUTPUT", "Error: Amount requested exceeds reserves")

elif Primebloodtotal > Amount:
    print("OUTPUT", "Main Level:", Primebloodtotal - Amount)
    print("OUTPUT", "Backup Level:", Secondaryblood)

elif Primebloodtotal < Amount:
    print("OUTPUT", "Warning: Main reserve depleted")
    print("OUTPUT", "Main Level: 0")
    print("OUTPUT", "Backup Level:", Amountleft)

else:
    print("OUTPUT", "Warning: Main reserve depleted")
    print("OUTPUT", "Main Level: 0")
    print("OUTPUT", "Warning: Backup reserve depleted")
    print("OUTPUT", "Backup Level: 0")



