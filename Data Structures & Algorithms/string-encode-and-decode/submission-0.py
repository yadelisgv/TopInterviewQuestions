class Solution:

    def encode(self, strs: List[str]) -> str:
        cadena=[]
        for i in strs:
            cadena.append(str(len(i)))
            cadena.append('#')
            cadena.append(i)
        return "".join(cadena)


    def decode(self, s: str) -> List[str]:
        #    5#Hello 5#World  len=14
        
        resul=[]
        i=0
        while i< len(s):
            result=[]
            j=i
            while s[j] != "#":
                j+=1
            long=int(s[i:j])
            i=j+1
            j=i+long
            resul.append(s[i:j])
            i=j
        return resul