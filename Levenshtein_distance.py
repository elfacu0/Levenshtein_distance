import numpy as np
class Dictionary:
    def __init__(self,words):
        self.words=words
    def levenshtein_distance(self,s,t):
        rows = len(s)+1
        cols = len(t)+1
        distance = np.zeros((rows,cols),dtype = int)
        
        for i in range(1,rows):
            for j in range(1,cols):
                distance[i][0] = i
                distance[0][j] = j
                
        for col in range(1,cols):
            for row in range(1,rows):
                if s[row-1] == t[col-1]:
                    cost = 0
                else:
                    cost = 1
                distance[row][col] = min(distance[row-1][col]+1,distance[row][col-1]+1,distance[row-1][col-1] + cost)
            
        return(distance[row][col])
        
    def find_most_similar(self,term):
        l = []
        for key in self.words:
            l.append(self.levenshtein_distance(key,term))
        return self.words[l.index(min(l))]
