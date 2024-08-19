f = open('README.md', 'rb')

f1 = open('test.txt', 'ab')

for data in f:
    f1.write(data)