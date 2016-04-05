sum = 0
old = 0
current = 2

while current < 4000000:
  sum += current
  temp = old
  old = current
  current = temp + 4 * old


print(sum)