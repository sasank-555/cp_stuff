def generate_subseq(s):
  n = len(s)
  res = []
  for i in range(2**n):
    temp = ""
    for j in range(32):
      if (1<<j)&i :
        temp+=s[j]
    res.append(temp)
  return res
print(generate_subseq("abc"))