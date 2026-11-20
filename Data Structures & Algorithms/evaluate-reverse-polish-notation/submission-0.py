class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
            pila=[]
            for i in tokens:
                if i =="+":
                    pila.append(pila.pop()+pila.pop())
                elif i =="*":
                    pila.append(pila.pop()*pila.pop())
                elif i =="/":
                    a=pila.pop()
                    b=pila.pop()
                    pila.append(int(b/a))
                elif i =="-":
                    a=pila.pop()
                    b=pila.pop()
                    pila.append(b-a)
                else:
                    pila.append(int(i))
            return pila[0]

