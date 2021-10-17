import random

def random_state(n):
    origin_state=[[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        origin_state[random.randint(0,n-1)][i]=1
    return origin_state
#heuristic fuction
def h(state,n):
    attack=0
    #starting from left side and only care right side
    for i in range(n):
        for j in range(n):
            if state[j][i]==1:
                attack+=local_h(state,j,i,n)
    return attack
def local_h(state,row,col,n):
    local_attack=0
    for i in range(col+1,n):
        if state[row][i]==1:   #check row
            local_attack+=1
    step=1

    for i in range (col+1,n):
        if row+step<n and state[row+step][i]==1:         #upper 
            local_attack+=1
        if row-step>=0 and state[row-step][i]==1:        #down
            local_attack+=1
        step+=1
    return local_attack
#successor functioin
def successor(state,n):
    for j in range(n):
        for i in range(n):
            if state[i][j]==1:        #find queen
                min_h=h(state,n)
                min_h_row=i            #set min_h and min_row
                state[i][j]=0         #set 0, only 1 queen exits
                for row in range(n):
                    state[row][j]=1
                    if h(state,n)<min_h:
                        min_h=h(state,n)
                        min_h_row=row
                    state[row][j]=0
                state[min_h_row][j]=1  #found min location and move it                  
def hc(n):
    solution=False
    outfile_name="./AI/"+str(n)+"_hc_output.txt"
    outfile=open(outfile_name,"w")
    for i in range(100):
        current_state=random_state(n)
        successor(current_state,n)
        if h(current_state,n)==0:
            solution=True
            break
    if not solution:
        outfile.write("No solution")
    else:
        for i in range(n):
            for j in range(n):
                if current_state[j][i]==1:
                    outfile.write(str(j+1)+" ")
                    break
