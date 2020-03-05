import random,sys,copy

class board:
  def __init__(self):
      self.board = [[0 for i in range(0,8)] for j in range(0,8)]
      for i in range(0,8):
        while 1:
          rand_row = random.randint(0,7)
          rand_col = random.randint(0,7)
          if self.board[rand_row][rand_col] == 0:
            self.board[rand_row][rand_col] = "Q"
            break

  def __repr__(self):
    mstr = ""	
    for i in range(0,8):
      for j in range(0,8):
        mstr = mstr + str(self.board[i][j]) + " "
      mstr = mstr + "\n"
    return (mstr)
 
class queens:
  def __init__(self,v):
    self.v=v
    self.mboard = board()
    self.cost = self.calc_cost(self.mboard)
    self.hill_solution()
 
  def hill_solution(self):
    while 1:
      currViolations = self.cost
      self.getlowercostboard()
      if currViolations == self.cost:
        break
      if self.cost == 0:
         if self.v==True:
            print ("SOLUTION FOUND")
            print(self.mboard)
    return self.cost
 
  def calc_cost(self, tboard):
    hcost = 0
    dcost = 0
    for i in range(0,8):
      for j in range(0,8):
        if tboard.board[i][j] == "Q":
           hcost -= 2
           for k in range(0,8):
              if tboard.board[i][k] == "Q":
                hcost += 1
              if tboard.board[k][j] == "Q":
                hcost += 1
           k, l = i+1, j+1
           while k < 8 and l < 8:
            if tboard.board[k][l] == "Q":
              dcost += 1
            k +=1
            l +=1
           k, l = i+1, j-1
           while k < 8 and l >= 0:
            if tboard.board[k][l] == "Q":
              dcost += 1
            k +=1
            l -=1
           k, l = i-1, j+1
           while k >= 0 and l < 8:
            if tboard.board[k][l] == "Q":
              dcost += 1
            k -=1
            l +=1
           k, l = i-1, j-1
           while k >= 0 and l >= 0:
            if tboard.board[k][l] == "Q":
              dcost += 1
            k -=1
            l -=1
    return ((dcost + hcost))
 

  def getlowercostboard(self):
    lowcost = self.calc_cost(self.mboard)
    lowestavailable = self.mboard
    for q_row in range(0,8):
      for q_col in range(0,8):
        if self.mboard.board[q_row][q_col] == "Q":
          for m_row in range(0,8):
            for m_col in range(0,8):
              if self.mboard.board[m_row][m_col] != "Q":
                tryboard = copy.deepcopy(self.mboard)
                tryboard.board[q_row][q_col] = 0
                tryboard.board[m_row][m_col] = "Q"
                thiscost = self.calc_cost(tryboard)
                if thiscost < lowcost:
                  lowcost = thiscost
                  lowestavailable = tryboard
    self.mboard = lowestavailable
 #   print(self.mboard)
    self.cost = lowcost
 #   print(self.cost)
    

mboard = queens(True)
   
