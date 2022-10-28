def search(items, amount):
    if amount <= 0:
        return 'no gift found'

    i = 0
    j = len(items) - 1
    diff = {}

    # Sliding window should be O(n)
    while i < j:
        sum = items[j][1] + items[i][1]

        if sum == amount:
            return items[i][0], items[j][0]

        difference = amount - sum
        if difference > 0:
            diff[difference] = (items[i], items[j])

        if sum < amount:
            i += 1

        if sum > amount:
            j -= 1

    # Sorting should be O(n * long n)
    sorted_items = sorted(diff.items())
    item_one, item_two = sorted_items[0][1]

    if len(diff) == 0:
        return 'no gift found'
    return item_one[0], item_two[0]
