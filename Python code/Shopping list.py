shopping_list = []
print("---Shopping List---")
while True:
    choice = int(input("Enter an option (1-5): "))
    match choice:
        case 1:
            new_item = input("Enter an item to be added: ")
            shopping_list.append(new_item)
            print(f"{new_item.title()} added. ")
        case 2:
            item_remove = input("Enter an item to be removed: ")
            if item_remove in shopping_list:
                shopping_list.remove(item_remove)
                print(f"{item_remove.title()} has been removed. ")
            else:
                print(f"{item_remove.title()} is not in the list. ")
        case 3:
            for i in range(len(shopping_list)):
                print(f"{i+1}. {shopping_list[i]}")
        case 4:
