class Solution:
    def isValid(self, s: str) -> bool:
        pila=[]
        list_elem={")" : "(",
                   "]" : "[",
                   "}" : "{"}
        for st in s:
            if st in list_elem:
                if pila and list_elem[st]==pila[-1]:
                    pila.pop()
                else:
                    return False
            else:
                pila.append(st)
        
        return True if not pila else False