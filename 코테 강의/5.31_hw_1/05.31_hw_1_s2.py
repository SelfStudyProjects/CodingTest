def solution(n, m, x, y, r, c, k):

    def reachable(x,y, count):
        if (abs(r-x)+abs(c-y)) <= (k-count) and ((abs(r-x)+abs(c-y))-(k-count))%2 == 0:
            return True
        return False
    
    if not reachable(x, y, 0):
        return "impossible"
    
    def calculate_neighbors(x,y):
        neighbor = []
        if x+1 <= n:
            neighbor.append((x+1,y, 'd'))
        if y-1 >= 1:
            neighbor.append((x,y-1, 'l'))
        if y+1 <= m:
            neighbor.append((x,y+1, 'r'))
        if x-1 <= n:
            neighbor.append((x-1,y, 'u'))
        return neighbor
    
    answer = ''
    def dfs(x,y, count, answer):
        neighbors = calculate_neighbors(x,y)
        for neighbor in neighbors:
            if reachable(neighbor[0], neighbor[1],count+1):
                answer += neighbor[2]
                answer = dfs(neighbor[0], neighbor[1], count+1, answer)
                break
        return answer
    return dfs(x,y,0,answer) or 'impossible'