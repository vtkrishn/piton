class SnakeAndLadder:
    def __init__(self, size):
        self.size=size
    def constructBoard(self,ladder,snakes):
        self.board =[]
        count = 0
        for i in range(self.size/10):
            l = []
            for i in range(10):
                if ladder.has_key(count):
                    l.append(ladder[count])
                elif snakes.has_key(count):
                    l.append(snakes[count])
                else:
                    l.append(-1)
                count+=1
            self.board.append(l)
            #print count
    def getMinDice(self,ladder,snakes):
        visited = [False]*self.size
        q = []
        
        q.append(0)
        visited[0] = True
        while q:
            s = q.pop(0)
            
            if s == self.size-1:
                return
            
            #While loop
            # if self.board[0][s+1] is -1:
            #     if not visited[s+1]:
            #         if ladder.has_key(s+1):
            #             q.append(ladder[s+1])
            #         elif snakes.has_key(s+1):
            #             q.append(snakes[s+1])    
            #         else:
            #             q.append(s+1)    
            #         visited[s+1] = True
            # if self.board[0][s+3] is -1:
            #     if not visited[s+3]:
            #         if ladder.has_key(s+3):
            #             q.append(ladder[s+3])
            #         elif snakes.has_key(s+3):
            #             q.append(snakes[s+3])    
            #         else:
            #             q.append(s+3)    
            #         visited[s+3] = True
            
        #print visited
            
s = SnakeAndLadder(30)
ladder = {2:21,4:7,10:15,19:28}
snakes = {26:0,20:8,16:3,18:6}
s.constructBoard(ladder,snakes)
s.getMinDice(ladder,snakes)