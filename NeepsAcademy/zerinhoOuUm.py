alice, clara, beto = map(int, input().split())

if alice != clara and alice != beto:
    print('A')

elif clara != alice and clara != beto:
    print('B')


elif beto != alice and beto != clara:
    print('C')

else:
    print('*')
