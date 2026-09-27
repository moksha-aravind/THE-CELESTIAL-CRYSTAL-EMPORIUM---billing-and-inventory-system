import pandas as pd
import csv
csv_file = "inventory.csv"
df = pd.DataFrame({"ID": ["10A1", "10A2", "10B1", "10C1", "10D4"],"Item": ["Moonstone Crystal", "Rose Quartz", "Raw Lapis Lazuli", "Selenite", "Pyrite"],"Price": [5650, 3500, 8999, 7685, 2560],"Stock": [100, 150, 55, 75, 90],})
df.to_csv("inventory.csv", index=False)
while True:
        print ("WELCOME TO THE CELESTIAL CRYSTAL EMPORIUM 🌙💎")
        print ("Please see the options below :")
        print ("{1} --- View Inventory 🪐")
        print ("{2} --- Add items to the cart")
        print ("{3} --- Exit")
        c=input ("Please enter your choice 🪄:")
        if c =='1':
                print ("_____CURRENT INVENTORY_____")
                df = pd.read_csv("inventory.csv")
                print(df.to_string(index=False))
                input("\nPress Enter to return to the main menu 🔮")
        elif c == '2':
                cart = []
                while True:
                        i = input("Please enter item ID :")
                        if i not in df["ID"].values:
                                print ("Invalid ID , please try again !")
                                continue
                        item = df[df["ID"] == i].iloc[0]
                        print("Item:", item["Item"])
                        print("Price:", item["Price"])
                        q = int(input("Enter the quantity you want to purchase :"))
                        stock = df[df["ID"] == i]["Stock"].values[0]
                        m=input ("Do you want to add more items to the cart (y/n)")
                        if m != 'y':
                                break
                if q > stock:
                        print("The item is out of stock !")
                else:
                        print("The item is in stock !")
                        
                price = df.loc[df["ID"] == i, "Price"].values[0]
                item_name = df.loc[df["ID"] == i, "Item"].values[0]
                item_total = q * price
                cart.append({'ID': i,'Item': item_name,'Qty': q,'Total': item_total})
                df.loc[df["ID"] == i, "Stock"] -= q
                df.to_csv(csv_file, index=False)
                
                
                if cart:
                        print ("++++++YOUR CURRENT BILL=======")
                        grand_total = 0
                        for item in cart :
                                print(f"{item['Qty']} x {item['Item']} - ₹{item['Total']}")
                                grand_total +=item ['Total']
                        print("-" * 30)
                        print(f"GRAND TOTAL: ₹{grand_total}")
                        
                input("\n Press Enter to return to the main menu 🔮")
                
        elif c=='3':
                print ("Thank you for visting THE CELESTIAL CRYSTAL EMPORIUM 🌙💎 !")
                break
        else:
                print ("Invalid choice , please choose again ( 1 , 2 or 3) !")


           
