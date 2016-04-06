sum = 0
old = 1
current = 1

while current < 4000000:
  temp = old
  old = current
  current = temp + old
  if current % 2 == 0:
    sum += current