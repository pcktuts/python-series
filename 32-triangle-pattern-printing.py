#Python pattern printing
'''
* 
* * 
* * * 
* * * * 
* * * * * 
'''
def right_triangle(n):    
    for i in range(0, n): 
        for k in range(0, i+1):
            print("* ", end="")                    
        print("\r")

'''
         *
       * *
     * * *
   * * * *
 * * * * *
'''
def left_triangle(n):   
    for i in range(0, n): 
        # print space      
        for j in range(0, n-1-i):            
                print("  ", end="")             
        for k in range(0, i+1):
            print(" *", end="")                    
        print("\r")
'''
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
'''
def triangle(n):     
    for i in range(0, n): 
        # print space      
        for j in range(0, n-1-i):            
                print(" ", end="")             
        for k in range(0, i+1):
            print("* ", end="")                    
        print("\r")
        
right_triangle(10)
left_triangle(10)
triangle(10)
