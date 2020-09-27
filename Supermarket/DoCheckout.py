
from Supermarket.CalculateTotal import calculate_total


def main():
    print("Welcome to self-checkout.\n")
    print("Enter the name of a product followed by the <Enter> key. When you are finished, type \"Done\" then <Enter> "
          "to calculate your total.\n")
    print("Your groceries:")

    item_list = []
    scanned_item = input()
    while scanned_item.lower() != "done":
        item_list.append(scanned_item)
        scanned_item = input()

    grocery_total_message = calculate_total(item_list)
    print(grocery_total_message)

#my comment - NJ

main()
# hi
