# A cashier has currency notes of denominations 10, 50 and 100. If the amount to be withdrawn is input 
# through the keyboard in hundreds, find the total number of
# currency notes of each denomination the cashier will have to give to the withdrawer.

how_much_cash = int(input("How much do you want to change"))
num_100s = how_much_cash // 100    # also equivalent to = int(how_much_cash / 100)
print(f"Number of 100s notes: {num_100s}") # DO WE NEED TO USE F IF ONLY ONE VARIABLE ?

remaining_cash = how_much_cash % 100
num_50s = remaining_cash // 50

#simplier way ?

amount = int(input("Enter the amount to be withdrawn in hundreds: ")) # prompt user to enter amount

hundred_notes = amount // 100 # calculate number of 100 notes
fifty_notes = (amount % 100) // 50 # calculate number of 50 notes
ten_notes = (amount % 50) // 10 # calculate number of 10 notes
print("Number of 100 notes:", hundred_notes)
print("Number of 50 notes:", fifty_notes)
print("Number of 10 notes:", ten_notes)