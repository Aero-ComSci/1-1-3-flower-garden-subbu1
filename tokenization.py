def main():
    flowerList = ["lily", "rose", "tulip", "lotus", "sunflower"]
    prompt(flowerList)

def prompt(itemList):
    sourceInput = input("Hi, what would you like to generate: ").lower().strip()

    # Extract numerical options and item options
    numericalOptions = [int(x) for x in sourceInput.split() if x.isdigit()]
    itemOptions = [x for x in sourceInput.split() if x.isalpha()]

    finalItem = itemMatching(itemOptions, itemList)

    if len(numericalOptions) > 1:
        finalNum = numberSelector(sourceInput, numericalOptions, finalItem)
    elif len(numericalOptions) == 0:
        finalNum = 1
    else:
        finalNum = numericalOptions[0]

    print([finalNum, finalItem])
    return [finalNum, finalItem]

def itemMatching(itemList, allowedItems):
    for item in itemList:
        # Normalize item for comparison
        normalized_item = ''.join(filter(str.isalpha, item))
        if normalized_item in allowedItems:
            return normalized_item
    return None

def numberSelector(input, numberList, item):
    finalNumSelector = (None, float('inf'))

    if item is None:
        return None

    for n in numberList:
        try:
            item_index = input.index(item)
            number_index = input.index(str(n))
            proximity = abs(item_index - number_index)

            if proximity < finalNumSelector[1]:
                finalNumSelector = (n, proximity)
        except ValueError:
            continue

    return finalNumSelector[0]

def verifyNum(inputMessage):
    while True:
        num = input(inputMessage)
        if num.isdigit():
            return int(num)
        else:
            print("Please make it a number")

def guidelines():
    print("Sorry, nothing you have given us follows community guidelines")
    prompt([])  # Pass an empty list to avoid recursion with an undefined itemList

if __name__ == "__main__":
    main()
