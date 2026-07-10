strNum = '342'
mask = '0'
for i in strNum:
    print(f'The num is = {int(hex(ord(i)), 16)- int(hex(ord('0')), 16)}')