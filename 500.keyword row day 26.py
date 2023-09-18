class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        s=[]
        
        a=['Q','q','W','w','E','e','R','r','T','t','Y','y','U','u','I','i','O','o','P','p']
        b=['A','a','S','s','D','d','F','f','G','g','H','h','J','j','K','k','L','l']
        c=['Z','z','X','x','C','c','V','v','B','b','N','n','M','m']
        for i in range(len(words)):
            n=0
            x=len(words[i])
            for j in range(x):
                if words[i][j] in a:
                    n +=1
            if n ==x:
                s.append(words[i])
            n=0
            for j in range(x):
                if words[i][j] in b:
                    n+=1
            if n==x:
                s.append(words[i])
            n=0
            for j in range(x):
                if words[i][j] in c:
                    n+=1
            if n==x:
                s.append(words[i])
        return s
        
