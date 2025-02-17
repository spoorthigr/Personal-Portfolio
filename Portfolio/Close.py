s = "b"
t = "abc"

def sub(s, t):
      if len(s) == 0: 
            return True
      
      i=0
      j=0
      while j < len(t) i < len:
            if s[i]  == t[j]:
                 i+=1
                 j+=1
            else:
                  j+=1
      if i == len(s):
            return True
      return False            
                  
sub(s, t)

