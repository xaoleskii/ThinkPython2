def ack(m, n):
    if m == 0:
        print('ack({}, {})'.format(m, n))
        return n + 1
    elif n == 0:
        print('ack({}, {})'.format(m, n))
        return  ack(m - 1 , 1)
    return ack(m - 1, ack(m, n - 1))

print('Result is ', ack(3, 4))
