núm = int(input('Digíte um número: '))
total = 0
for c in range(1, núm + 1):
    if núm % c == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} ' .format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(núm, total))
if total == 2:
    print('E por isso ele é Primo!')
else:
    print('E por isso ele não é Primo!')