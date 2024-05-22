def reverse_string(s):
   
    if len(s) <= 1:
        return s
    else:
      
        return reverse_string(s[1:]) + s[0]


print(reverse_string("hello"))  
print(reverse_string("ngawang")) 
print(reverse_string(""))       
print(reverse_string("a"))  
