import os.path
file = input('Input file name with extension -> ')
ls = [1, 2, 2]
if not os.path.exists(file):
  with open(file, 'w') as fp:
    pass
else:
  print('FILE ALREADY EXISTS!')
string = ' '
op = '0'
while op != '6':
  print('\n')
  print('1. Add')
  print('2. Delete')
  print('3. Display')
  print('4. Calculate')
  print('5. Update')
  print('6. Exit')
  op = input('Choose one of the following operations -> ')

  if op == '1':
    ls = []
    print('Input the data elements : ')
    for i in range(4):
      x = input()
      ls.append(x)
    string = ' '
    with open(file, 'a') as fp:
      fp.write(string.join(ls) + '\n')

  if op == '2':
    with open(file, 'r+') as fp:
      lines = fp.readlines()
      idx = int(input('Enter the index of record you want to delete -> '))
      del lines[idx]
      fp.seek(0)
      fp.truncate(0)
      for line in lines:
        fp.write(line)

  if op == '3':
    with open(file, 'r') as fp:
      lines = fp.readlines()
      print('\nData : \n')
      for line in lines:
        print(line)
  
  if op == '4':
    with open(file, 'r') as fp:
      r = fp.readlines()
      ls = []
      idx = int(input('Enter the index of record for which you want to calculate the sum -> '))
      ls = r[idx].split(' ')
      ls[-1] = ls[-1].split('\n')[0]  
      ls.pop(0)
      sum = 0
      for n in ls:
        sum = sum + int(n)
      print('\nTotal marks of student at index {} is {}'.format(idx, sum))

  if op == '5':
    with open(file, 'r+') as fp:
      lines = fp.readlines()
      idx = int(input('Enter the index of record you want to update -> '))
      ls = []
      print('Input the data elements : ')
      for i in range(4):
        x = input()
        ls.append(x)
      ls.append('\n')
      upd = ' '.join(ls)
      for line in lines:
        ls = line.split(' ')
      lines[idx] = upd
      fp.seek(0)
      fp.truncate(0)
      for line in lines:
        fp.write(line)
    
  if op == '6':
    break