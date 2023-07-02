p1, c1, p2, c2 = map(int, input('').split())

cal1 = p1 * c1
cal2 = p2 * c2


if cal1 == cal2:
    print(0)

elif cal1 > cal2:
    print(-1)

else: 
    print(1)