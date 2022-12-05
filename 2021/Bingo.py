import numpy as np

class Bingo:
    def __init__(self,size):
        self.size = size
        self.mask = np.ones([self.size,self.size])*-1
        self.board = []
        self.win = 0
    def loadBingo(self, bingoList):
         self.board = bingoList
    
    def checkBingo(self, num):
        for i in range(self.size):
            for j in range(self.size):
                if(self.board[j+i*self.size] == num):
                    self.mask[i][j] = 1
        self.win = 0
        line = np.ones(self.size)
        diag = np.zeros((self.size,self.size))
        np.fill_diagonal(diag, 1)
        for i in range(self.size):
            if(np.matmul(self.mask[i],line) == self.size):
                self.win += 1
            if(np.matmul(line,self.mask[:,i]) == self.size):
                self.win += 1
    
    def didWin(self):
        return self.win
    
    def __str__(self) -> str:
        result = ''
        for i in range(self.size):
            for j in range(self.size):
                if(self.mask[i][j] != -1):
                    result += '\"'+ str(self.board[j+i*self.size]) + '\",'
                else:
                    result += ' '+ str(self.board[j+i*self.size]) + ' ,'
            result = result[:-1]
            result += '\n'
        result = result[:-1]
        return result
    
    def __repr__(self) -> str:
        return "this is bingo class with %d size"%(self.size)