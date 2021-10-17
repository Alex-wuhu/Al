import queue
import copy

def solution(q,n):
    outfile_name="./AI/"+str(n)+"_dfs_output.txt"
    outfile=open(outfile_name,"w")
    sol=False
    while not q.empty():
        state=q.get()
        #print_board(state)
        if check_state(state,n):
            sol=True
            break
    if sol:
        for i in range(n):
            for j in range(n):
                if state[j][i]==1:
                    outfile.write(str(j+1)+" ")
                    break
    else:
        outfile.write("no solution!")
    outfile.close()


def check_state(state,n):
    for row in range(n):
        for col in range(n):
            if state[row][col]==1:
                if check_position(state,row,col,n)==False:
                    return False
    return True


def check_position(state,row,col,n):
    for i in range(n):     #check row
        if i==col:
            continue
        elif state[row][i]==1:
            return False
    for i in range(n):    #chcek col
        if i==row:
            continue
        elif state[i][col]==1:
            return False
    
    step=1  #upper 
    for i in range(row-1,-1,-1):
        j=col+step
        if j<n:
            if state[i][j]==1:
                return False
        j=col-step
        if j>=0:
            if state[i][j]==1:
                return False
        step+=1
    
    step=1  #down
    
    for i in range(row+1,n):
        j=col+step
        if j<n:
            if state[i][j]==1:
                return False
        j=col-step
        if j>=0:
            if state[i][j]==1:
                return False
        step+=1
    return True

def bfs(n):    
    table=queue.Queue()
    origin_state=[[ 0 for i in range(n)] for j in range (n)]
    table.put(origin_state)
    col=0

    while not table.empty():
        for i in range(table.qsize()):
            state=table.get()
            for j in range(n):
                new_state=copy.deepcopy(state)
                new_state[j][col]=1
                table.put(new_state)
        col+=1
        if col==n:
            break

    solution(table,n)






