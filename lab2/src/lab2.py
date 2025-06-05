def minEatingSpeed(piles, H):
    max_pile = 0
    for pile in piles:
        if pile > max_pile:
            max_pile = pile

    count_piles = 0
    for i in piles:
        count_piles += 1
    if count_piles > H:
        return -1

    left, right = 1, max_pile

    while left < right:
        mid = (left + right) // 2

        hours_needed = 0
        for pile in piles:
            hours_needed += (pile // mid) + (1 if pile % mid != 0 else 0)

        if hours_needed > H:
            left = mid + 1
        else:
            right = mid

    return left


piles = [3, 2, 1, 5]
H = 8

result = minEatingSpeed(piles, H)
if result == -1:
    print("Джекі не встигне з'їсти всі банани")
else:
    print("Мінімальна швидкість поїдання бананів:", result)