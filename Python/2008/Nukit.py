# J5

# functions to determine if you can do a certain move

def canMove(a, b, c, d):
    return canDoAABDD(a, b, c, d) or canDoABCD(a, b, c, d) or canDoCCD(a, b, c, d) or canDoBBB(a, b, c, d) or canDoAD(a, b, c, d)

def canDoAABDD(a, b, c, d):
    return a >= 2 and b >= 1 and d >= 2

def canDoABCD(a, b, c, d):
	return a >= 1 and b >= 1 and c >= 1 and d >= 1

def canDoCCD(a, b, c, d):
	return c >= 2 and d >= 1
    
def canDoBBB(a, b, c, d):
	return b >= 3

def canDoAD(a, b, c, d):
    return a >= 1 and d >= 1

# functions to determine if winning or losing combo

def losingCombo(a, b, c, d):
    if not canMove(a, b, c, d):
        return True
    else:
        temp = True
        if canDoAABDD(a, b, c, d):
            temp = temp and winningCombo(a - 2, b - 1, c, d - 2)
        if canDoABCD(a, b, c, d):
            temp = temp and winningCombo(a - 1, b - 1, c - 1, d - 1)
        if canDoCCD(a, b, c, d):
            temp = temp and winningCombo(a, b, c - 2, d - 1)
        if canDoBBB(a, b, c, d):
            temp = temp and winningCombo(a, b - 3, c, d)
        if canDoAD(a, b, c, d):
            temp = temp and winningCombo(a - 1, b, c, d - 1)
            
        return temp

def winningCombo(a, b, c, d):
    if canDoAABDD(a, b, c, d) and losingCombo(a - 2, b - 1, c, d - 2):
        return True
    elif canDoABCD(a, b, c, d) and losingCombo(a - 1, b - 1, c - 1, d - 1):
        return True
    elif canDoCCD(a, b, c, d) and losingCombo(a, b, c - 2, d - 1):
        return True
    elif canDoBBB(a, b, c, d) and losingCombo(a, b - 3, c, d):
        return True
    elif canDoAD(a, b, c, d) and losingCombo(a - 1, b, c, d - 1):
        return True
    else:
        return False
    
if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        a, b, c, d = list(map(int, input().split()))
        
        if winningCombo(a, b, c, d):
            print("Patrick")
        else:
            print("Roland")
    
    