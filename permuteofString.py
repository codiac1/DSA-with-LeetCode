"""
l1 = []
def solve(string , l , r) :
    global l1
    if l == r:
        s = "".join(string)
        l1.append(s)
    else :
        for i in range(l,r+1):
            string[l] , string[i] = string[i] , string[l]
            solve(string , l+1 , r)
            string[l] , string[i] = string[i] , string[l]

def permute(string):
    solve(list(string) , 0 , len(string)-1)

string = "ABC"
permute(string)
print(l1)
"""
l=[]
class Solution:
    def find_permutation(self, S):
      self.solve(list(S),0,len(S)-1)
      print(l)
         
    def solve(self,string,left,right):
        global l
        if left==right:
            l.append("".join(string))
        else:
            for i in range(left,right+1):
                string[left],string[i]=string[i],string[left]
                self.solve(string,left+1,right)
                string[left],string[i]=string[i],string[left]

obj=Solution()
obj.find_permutation("ABC")

            

        
        
    
