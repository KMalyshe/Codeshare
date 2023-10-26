# K M
# a
n = 7
for i in range (0,n):
  current_line = "K"
  for j in range (0, abs(3-i)):
    current_line += " "
  finished = current_line + "K"
  if len(finished) < 6:
    for k in range (0, 6-len(finished)):
      finished += " "
  finished += " "
  if i == 0:
    finished += "M   M"
  elif (i == 1) or (i == 2):
    finished += "MM MM"
  elif i == 3:
    finished += "M M M"
  else:
    finished += "M   M"
  print(finished)