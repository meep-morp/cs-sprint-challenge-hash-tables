def get_indices_of_item_weights(weights, length, limit):
    if length < 2:
        return None

    item_weights = {}
    for i in range(length):
        value = limit - weights[i]

        if value in item_weights:
            val_i = item_weights[value]
            rtn = [i, val_i]
            return rtn

        else:
            item_weights[weights[i]] = i

    print("None found")
    return None


print(get_indices_of_item_weights([12, 6, 7, 14, 19, 3, 0, 25, 40], 9, 7))
