amount=int(input("Enter the intital amount: "))
percentage=int(input("Enter the percentage tip on intial amount: "))
no=int(input("Enter no of people to split into: "))
final_amount=(amount+((amount*percentage)/100))/no
print(round(final_amount,2))
