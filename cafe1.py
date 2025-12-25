





menu={
  'Pizza':70,
  'Pasta':60,
  'Chicken':120,
  'Tea':20,
  'Burger':90,
  'Salad':50,
  'Coffee':80,
}



print("Welcome to cafe")
print("Here is our Menu:")
print("Pizza: Rs:70\nPasta: RS: 60  \n Chicken: RS: 120 \n Tea: RS: 20\nBurge: Rs:90 \n Salad: Rs:50  \nCoffee:Rs :50")


total=0



choice1=input("Enter your order:")
qty1=int(input("Enter quantity:"))
print("------Thank you for  order-------")
if (choice1=="coffee"):
  print(f"coffee added.")
  total1=80*qty1
elif (choice1=="pizza"):
    print(f"pizza added.")
    total1=70*qty1
elif(choice1=="pasta"):
     print(f"pasta added.")
     total1=60*qty1
elif(choice1=="tea"):
   print(f"tea added.")
   total1=20*qty1
elif(choice1=="salad"):
   print(f"salad added.")
   total1=50*qty1
elif (choice1=="burger"):
   print(f"burgen added.")
   total1=90*qty1
elif (choice1=="chiken"):
   print(f"chiken added.")
   total1=120*qty1
else:
  print(f"Item are not present in menu ,please choice another item! ")
  






more=input("Do you want to add more item!")


if more=="yes":
   choice2=input("Enter the item:")
   qty2=int(input("Enter quantity:"))
print("------Thank you for  order-------")  


if (choice2=="coffee"):
  print(f"coffee added.")
  total2=80*qty2
elif (choice2=="pizza"):
    print(f"pizza added.")
    total2=70*qty2
elif(choice2=="pasta"):
     print(f"pasta added.")
     total2=60*qty2
elif(choice2=="tea"):
   print(f"tea added.")
   total2=20*qty2
elif(choice2=="salad"):
   print(f"salad added.")
   total2=50*qty2
elif (choice2=="burger"):
   print(f"burgen added.")
   total2=90*qty2
elif (choice2=="chiken"):
   print(f"chiken added.")
   total2=120*qty2

else:
   print("No more item.")
   total2=0*qty2

print("Total items : ",{choice1,choice2})
print("Total Amount  ₹:",{total1+total2})








