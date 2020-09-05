s = input().split()
d = int(s[0])
t = int(s[1])
s = int(s[2])
if d <= t * s:
  print("Yes")
else:
  print("No")