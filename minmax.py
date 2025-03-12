
def MAX(data = []):
  Max = data[0]
  for i in range(len(data)):
    element = data[i]
    if element > Max:
      Max = element
  return Max

assert 80 == MAX(data = [46,56,73,21,45, 60,44, 30,80,10,23,45])
assert  5 == MAX(data = [4, 1,2,3,5])


def MIN(data = []):
  Min = data[0]
  for i in range(len(data)):
    element = data[i]
    if element < Min:
      Min = element
  return Min

resultmin = MIN(data = [46,56,73,21,45, 60,44, 30,80,10,23,45])
     
assert 10 == MIN(data = [46,56,73,21,45, 60,44, 30,80,10,23,45])
assert  4 == MIN(data = [4, 6, 5])

def SUM(data = []):
  Sum = 0 
  for i in range(len(data)):
    num = data[i]
    Sum = Sum + num 
  return Sum
    
assert 533 == SUM(data = [46,56,73,21,45, 60,44, 30,80,10,23,45])
assert 17 == SUM(data = [4,7,2,4])
assert 14 == SUM(data = [1,7,2,4])
assert 0 == SUM(data = [])

