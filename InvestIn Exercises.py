def solution1():
  return "Hello World"

def solution2(n):
  if type(n) != int: return
  
  if n%2 == 1: return "Weird"
  elif n in range(2,6): return "Not Weird"
  elif n in range(6,21): return "Weird"
  else: return "Not Weird"

def solution3(a,b):
  if type(a) != int or type(b) != int: return
  
  def add(a,b):
    return a+b
  def sub(a,b):
    return abs(a-b)
  def mult(a,b):
    return a*b
    
  return f"{add(a,b)}\n{sub(a,b)}\n{mult(a,b)}"

def solution4(a, b):
  if type(a) != int or type(b) != int: return
  
  return f"{a//b}\n{a/b}"

def solution5(n):
  if type(n) != int or n < 0: return
  
  out = []
  for i in range(n-1, 0, -1): out.append(str(i**2))
  print(out)
  return "\n".join(out)
  
def solution6(n):
  if type(n) != int or n < 0: return
  
  if n%4 == 0 and (n%100 != 0 or n%400 ==0): return True
  return False
  
def solution7(n):
  if type(n) != int: return
  
  for i in range(1, n+1):
    print(i, end=" ", flush=True)

def solution8(A):
  A.sort(reverse=True)
  if A[0] != A[1] and A[1]!= A[2]: return A[1]
  else: return "Not enough participants with different scores"

def solution9(records):
  def sortfunc(inp):
    return inp[1]
  records.sort(key=sortfunc)

  records2, out = records.copy(), []
  
  for i in records:
    if i[1] == records[0][1]: records2.remove(i)

  for i in records2:
    if i[1] == records2[0][1]: out.append(i[0])


  return "\n".join(out)

# print(solution1())
# print(solution2(3))
# print(solution3(5,6))
# print(solution4(5,2))
# print(solution5(5))
# print(solution6(2025))
# solution7(7)
print(solution8([1, 4, 56, 2, 24, 67, 56]))
# print(solution9([["Sameer", 97], ["Seb", 95], ["Rishi", 32], ["Anuj", 13], ["Sid", 32]]))