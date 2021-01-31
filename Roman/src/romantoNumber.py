class first_assignment_rn(object):
   def r2nmethod(self, roman):
  
      romannumber = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
      i = 0
      result = 0
      while i < len(roman):
         if i+1<len(roman) and roman[i:i+2] in romannumber:
            result+=romannumber[roman[i:i+2]]
            i+=2
         else:         
            result+=romannumber[roman[i]]
            i+=1
      return result

print(first_assignment_rn().r2nmethod("IV"))
print(first_assignment_rn().r2nmethod("MMXVIII"))
