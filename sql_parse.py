f = open("info.csv", "r")
for x in f:
  a = x.split(',')
  print(",('"+a[1]+"' ,'"+a[2]+"' ,"+a[3].replace('\n','')+")")