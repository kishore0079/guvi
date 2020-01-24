denominations = [1, 2, 5, 10, 20, 50, 100, 200, 500]
denominations.reverse()
amount = int(input())
for denom in denominations:
    if amount >= denom:
        print(denom, ' x ', amount//denom,' = ' ,denom*(amount//denom))
        amount = amount%denom
    if amount==0:
        break
