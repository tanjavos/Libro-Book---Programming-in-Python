while True:
    line = input('> ')
    if line[0] == '#' :
        continue
    if line == 'finish':
        break
    print(line)
print('Finished!')
