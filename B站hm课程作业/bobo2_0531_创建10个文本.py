def text():
    path = './'
    for name in range(1,5):
        with open(path + str(name) + '.txt','w') as t:
            t.write(str(name))
            t.close()
            print('Done')
text()