def find_pairs(banks, cost):
    """ """
    biggest = max(banks)
    seen    = [False for i in range(biggest+1)]
    pairs   = []
    for bank1 in banks:
        bank2 = cost - bank1
        if not seen[bank2]:
            pairs.append((bank1, bank2))
            seen[bank2] = True

    return pairs
    
if __name__ == "__main__":
    print(find_pairs([1, 2, 3], 4))
    assert find_pairs([1, 2, 3], 4) == [(1,3)]

