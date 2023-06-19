#Interact with system user
print("Hello my client!")
#take input from the user

#pack_sent(float)=the number of packages sent in total 
#weight_sent(float)= the sum of items sent by client in KGs, also refer to total weight of packages sent
#unused_capacity(float)=Total_pack_sent * 20-Total_weight_sent
#Package_least_capacity_used, rank the package which contains the least weight, searched online, using list statement
#Items are added to the package with weights ranging from 1 to 10 kg
#Once weight of 0 kg is given, the program should terminate.
#Each package can carry a maximum of 20 kg
#Handle user inputs that are not as expected
total_items = int(input("Enter the total number of items you wish to send: "))

item_sent = 0
pack_sent = 0
weight_sent = 0
unused_capacity = 0
empty_weight = 0
total_unused_capacity = 0
package_least_capacity_used = 0

current_pack = 0
current_weight = 0

for i in range(total_items):
 
    item_sent = float(input("Please enter the weight of your item: "))
    if item_sent == 0:
        pack_sent += 1
        print("\nLast package will be sent.")
        break
    elif item_sent < 10 or item_sent > 1:
        print("Item weight is counted. Please continue to enter the weight of your item.")   
    if item_sent > 10 or item_sent <0:
        print("\nIt's invalid weight. \n\nThe required weight entered must be between 1 and 10 kgs.")
        continue
    
    if current_weight + item_sent > 20:
        pack_sent += 1
        unused_capacity = 20 - current_weight 
        total_unused_capacity += unused_capacity
        weight_sent += current_weight
        current_weight = item_sent

        print("Package is ready to go." )
    elif current_weight + item_sent == 20:
        pack_sent += 1
        weight_sent += current_weight
        current_weight = item_sent
        print("Package is ready to go." )
    else:
        current_weight += item_sent
        
    if i == total_items - 1:
        pack_sent += 1
        weight_sent += current_weight

    if unused_capacity > empty_weight:
        empty_weight = unused_capacity
        package_least_capacity_used = pack_sent

total_unused_capacity = pack_sent * 20 - weight_sent
print(pack_sent)
print(weight_sent)
print(total_unused_capacity)
print(package_least_capacity_used)
#list statement to sort the package_least_capacity_used 