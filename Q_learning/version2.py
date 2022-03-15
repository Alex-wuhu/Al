#define the shape of the environment (i.e., its states)
import random
start_x=0
start_y=0
board=[[0 for i in range(5)] for j in range (5)]
def environment_setting(environment_rows,environment_columns,board):
    global start_x
    global start_y    
    input_file=open("./AI/Q_learning/input.txt","r")
    for i in range(environment_rows):
      s=input_file.readline()
      for j in range(environment_columns):
          if s[j]=='S':
              start_x=i
              start_y=j
          elif s[j]=='T':
              board[i][j]=1
          elif s[j]=='B':
              board[i][j]=-100
          elif s[j]=='G':
              board[i][j]=100
    input_file.close()


def is_terminal_state(row, column):
  if board[row][column] ==0 or board[row][column]==1 :
    return False
  else:
    return True

def get_starting_location():
      #get a random row and column index
  current_row = random.randint(0,environment_rows-1)
  current_column = random.randint(0,environment_columns-1)
  #continue choosing random row and column indexes until a non-terminal state is identified
  while is_terminal_state(current_row, current_column):
    current_row = random.randint(0,environment_rows-1)
    current_column = random.randint(0,environment_columns-1)
  return current_row, current_column



def transform(row,column):
  return column+row*environment_rows    
def get_next_action(row,column):
  state=transform(row,column)
  val=max(q_values[state])
  learning=random.random()
  if learning<0.999: 
    for i in range(0,4):
      if q_values[state][i]==val:
        return i
  else:
    return random.randint(0,3)    
def get_next_location(current_row_index, current_column_index, action_index):
  new_row_index = current_row_index
  new_column_index = current_column_index
  if actions[action_index] == 'up' and current_row_index > 0:
    new_row_index -= 1
  elif actions[action_index] == 'right' and current_column_index < environment_columns - 1:
    new_column_index += 1
  elif actions[action_index] == 'down' and current_row_index < environment_rows - 1:
    new_row_index += 1
  elif actions[action_index] == 'left' and current_column_index > 0:
    new_column_index -= 1
  return new_row_index, new_column_index
def get_shortest_path(start_row_index, start_column_index):
      #return immediately if this is an invalid starting location
  if is_terminal_state(start_row_index, start_column_index):
    return []
  else: #if this is a 'legal' starting location
    current_row_index, current_column_index = start_row_index, start_column_index
    shortest_path = []
    shortest_path.append(transform(current_row_index, current_column_index))
    #continue moving along the path until we reach the goal (i.e., the item packaging location)
    while not is_terminal_state(current_row_index, current_column_index):
      #get the best action to take
      action_index = get_next_action(current_row_index, current_column_index)
      current_row_index, current_column_index = get_next_location(current_row_index, current_column_index, action_index)
      shortest_path.append(transform(current_row_index, current_column_index))
    return shortest_path
# environment setting 
environment_rows = 5
environment_columns = 5
board=[[0 for i in range(environment_rows)] for j in range (environment_columns)]
environment_setting(environment_rows,environment_columns,board)

#The value of each (state, action) pair is initialized to 0.
q_values = [ [0 for i in range(4)] for j in range(environment_columns*environment_rows)]
actions = ['up', 'right', 'down', 'left']


print(board)


#run through 1000 training episodes
for episode in range(100000):
  #get the starting location for this episode
  row_index, column_index = get_starting_location()
  while not is_terminal_state(row_index, column_index):
    #choose which action to take (i.e., where to move next)
    action_index = get_next_action(row_index, column_index)
    #perform the chosen action, and transition to the next state (i.e., move to the next location)
    old_row_index, old_column_index = row_index, column_index #store the old row and column indexes
    row_index, column_index = get_next_location(row_index, column_index, action_index)
    reward = board[row_index][column_index]
    new_state=transform(row_index,column_index)
    new_action=get_next_action(row_index,column_index)
    max_val=q_values[new_state][new_action]
    #update the Q-value for the previous state and action pair
    new_q_value = reward+0.9*max_val
    old_state=transform(old_row_index,old_column_index)
    q_values[old_state][action_index] = new_q_value
print('Training complete!')

start_state=transform(start_x,start_y)
output_file=open("output.txt","w")
shortest_path=get_shortest_path(start_x,start_y)
for i in shortest_path:    
  output_file.write(str(i)+" ")
output_file.write("\n"+str(max(q_values[start_state])))
print(q_values)
print(get_shortest_path(start_x,start_y))
print(max(q_values[start_state]))
output_file.close()

