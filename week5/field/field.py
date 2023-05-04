def nine():
    f = open('구구단.txt', 'w', encoding='UTF-8')
    for i in range(1, 10):
        line = "======{0}======\n".format(i)
        f.write(line)
        for j in range(1, 10):
            line = "{0} * {1} = {2}\n".format(i, j, i*j)
            f.write(line)
    f.close

nine()