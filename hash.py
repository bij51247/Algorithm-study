import sys

def hash_store(arrayD,hash_key):
  arrayH = [0 for x in range(0,11)]
  
  for x in arrayD:
    k = x % hash_key
    while(arrayH[k] != 0):
      k = (k + 1) % hash_key
    arrayH[k] = x
  
  return(arrayH)

def hash_search(ls,x,hash_key):
  k = x % hash_key
  while(ls[k] != 0):
    if(ls[k] == x):
      return(k)
    else:
      k += (k+1)%hash_key
  return(None)

def main():
  target = int(sys.argv[1])
  hash_key = int(sys.argv[2])
  
  arrayD = [12,25,36,20,8,42]
  
  hash_array = hash_store(arrayD,hash_key)
  print("hash_array",hash_array)
  
  print(hash_search(hash_array,target,hash_key))
  
if __name__ == '__main__':
  main()