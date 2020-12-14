#goal_test function
def goal_test(state):  
    if state['A']==[2,2] and state['B']==[3,2] and state['C']==[4,2]:
        return True
    return False  
    

#action function
def move_right(state,size):
    import copy
    new_state=copy.deepcopy(state)
    if state['Agent'][1]+1>=1 and state['Agent'][1]+1<=size:  #check if move will be out of box
        agent_position1=state['Agent'] #store the position of agent before moving
        new_state['Agent'][1]=new_state['Agent'][1]+1 #move the agent
        agent_position2=new_state['Agent']#store the position of agent after moving
        for block in {key:value for key,value in new_state.items() if key != 'Agent'}:#iterate every block 
            if new_state[block]==agent_position2:#check if the position of block overlap the agent after moving
                new_state[block]=agent_position1#assign the position of agent before moving to the overlap block
    return new_state  
def move_left(state,size):
    import copy
    new_state=copy.deepcopy(state)
    if state['Agent'][1]-1>=1 and state['Agent'][1]-1<=size:  #check if move will be out of box
        agent_position1=state['Agent'] #store the position of agent before moving
        new_state['Agent'][1]=new_state['Agent'][1]-1 #move the agent
        agent_position2=new_state['Agent']#store the position of agent after moving
        for block in {key:value for key,value in new_state.items() if key != 'Agent'}:#iterate every block 
            if new_state[block]==agent_position2:#check if the position of block overlap the agent after moving
                new_state[block]=agent_position1#assign the position of agent before moving to the overlap block
    return new_state  
def move_up(state,size):
    import copy
    new_state=copy.deepcopy(state)
    if state['Agent'][0]-1>=1 and state['Agent'][0]-1<=size:  #check if move will be out of box
        agent_position1=state['Agent'] #store the position of agent before moving
        new_state['Agent'][0]=new_state['Agent'][0]-1 #move the agent
        agent_position2=new_state['Agent']#store the position of agent after moving
        for block in {key:value for key,value in new_state.items() if key != 'Agent'}:#iterate every block 
            if new_state[block]==agent_position2:#check if the position of block overlap the agent after moving
                new_state[block]=agent_position1#assign the position of agent before moving to the overlap block
    return new_state  
def move_down(state,size):
    import copy
    new_state=copy.deepcopy(state)
    if state['Agent'][0]+1>=1 and state['Agent'][0]+1<=size:  #check if move will be out of box
        agent_position1=state['Agent'] #store the position of agent before moving
        new_state['Agent'][0]=new_state['Agent'][0]+1 #move the agent
        agent_position2=new_state['Agent']#store the position of agent after moving
        for block in {key:value for key,value in new_state.items() if key != 'Agent'}:#iterate every block 
            if new_state[block]==agent_position2:#check if the position of block overlap the agent after moving
                new_state[block]=agent_position1#assign the position of agent before moving to the overlap block
    return new_state  
def action(state,size):
    right_state=move_right(state,size) if  state!=move_right(state,size) else None
    left_state=move_left(state,size) if  state!=move_left(state,size) else None
    up_state=move_up(state,size) if  state!=move_up(state,size) else None
    down_state=move_down(state,size) if  state!=move_down(state,size) else None
    results=[right_state,left_state,up_state,down_state]
    return [result for result in results if result is not None]#return only legal move results
    
    
#1， BFS(tree version)
def BFS(node,size):
    #check if the initial node is the goal node
    if goal_test(node['state']):
        print(node)
    # a FIFO queue with node as the only element
    frontier=[node]
    explored=[]
    goal_found=False
    # while not goal_test(node['state']):
    while goal_found==False:
    #update node and explored state

        #check if the frontier is empty
        if len(frontier)==0:
            print('failure')
        #pop the shallowest node from frontier for expansion
        node=frontier[0]
        for n in frontier:
            if n['depth']<node['depth']:
                node=n
        frontier.pop(frontier.index(node))
        #add the pop node state to the explored list
        explored.append(node)
    #update frontier node list
        for result in action(node['state'],size):
            child={"state":result,"path_cost":node['path_cost']+1,"depth":node['depth']+1,"parent_node":node}            
            if goal_test(child['state']):
                goal_found=True
                print('goal found: '+str(child['state'])+'/'+
                      ' path_cost:'+str(child['path_cost'])+'/'+
                      ' depth:'+str(child['depth'])+'/'+
                      ' parent:'+str(child['parent_node']['state'])+'/'+
                      ' exploredlen:'+str(len(explored))+
                      ' fronlen:'+str(len(frontier))

                     )   
            frontier.append(child)
            
#initial_state={"A":[4,1],"B":[4,2],"C":[4,3],"Agent":[4,4]}
initial_state={"A":[2,1],"B":[3,2],"C":[4,3],"Agent":[1,1]}
node={"state":initial_state,"path_cost":0,"depth":0,"parent_node":None}
BFS(node,4)   
BFS(node,5)  
BFS(node,6)  

#BFS(graph version)
def BFS(node,size):
    #check if the initial node is the goal node
    if goal_test(node['state']):
        print(node)
    # a FIFO queue with node as the only element
    frontier=[node]
    explored=[]
    goal_found=False
    while goal_found==False:
    #update node and explored state

        #check if the frontier is empty
        if len(frontier)==0:
            print('failure')
        #pop the shallowest node from frontier for expansion
        node=frontier[0]
        for n in frontier:
            if n['depth']<node['depth']:
                node=n
        frontier.pop(frontier.index(node))
        #add the pop node state to the explored list
        explored.append(node)
    #update frontier node list
        for result in action(node['state'],size):
            child={"state":result,"path_cost":node['path_cost']+1,"depth":node['depth']+1,"parent_node":node}
            if child['state'] not in [i['state'] for i in explored ] and child not in [i['state'] for i in frontier ]:
                #this need to be check the duplicate of the 'state' rather than the 'node',because the state can be duplicate in different node
                if goal_test(child['state']):
                    goal_found=True
                    print('goal found: '+str(child['state'])+'/'+
                          ' path_cost:'+str(child['path_cost'])+'/'+
                          ' depth:'+str(child['depth'])+'/'+
                          ' parent:'+str(child['parent_node']['state'])+'/'+
                          ' exploredlen:'+str(len(explored))+
                          ' fronlen:'+str(len(frontier))

                         )
                    

                frontier.append(child)


initial_state={"A":[4,1],"B":[4,2],"C":[4,3],"Agent":[4,4]}
#initial_state={"A":[2,1],"B":[3,2],"C":[4,3],"Agent":[1,1]}
node={"state":initial_state,"path_cost":0,"depth":0,"parent_node":None}
BFS(node,4)


# 2, DFS(tree version)
def DFS(node,size):
    #check if the initial node is the goal node
    if goal_test(node['state']):
        print(node)
    # a LIFO queue with node as the only element
    frontier=[node]
    explored=[]
    goal_found=False
    while goal_found==False:
    #update node and explored state

        #check if the frontier is empty
        if len(frontier)==0:
            print('failure')
        #pop the deepest node from frontier for expansion
        node=frontier[0]
        for n in frontier:
            if n['depth']>node['depth']:
                node=n
        frontier.pop(frontier.index(node))
        #add the pop node state to the explored list
        explored.append(node)
    #update frontier node list
        for result in action(node['state'],size):
            child={"state":result,"path_cost":node['path_cost']+1,"depth":node['depth']+1,"parent_node":node}
            if goal_test(child['state']):
                    goal_found=True
                    print('goal found: '+str(child['state'])+'/'+
                          ' path_cost:'+str(child['path_cost'])+'/'+
                          ' depth:'+str(child['depth'])+'/'+
                          ' parent:'+str(child['parent_node']['state'])+'/'+
                          ' exploredlen:'+str(len(explored))+
                          ' fronlen:'+str(len(frontier))

                         )
                    return child


            frontier.append(child)

# initial_state={"A":[2,1],"B":[3,2],"C":[4,3],"Agent":[1,1]}
# node={"state":initial_state,"path_cost":0,"depth":0,"parent_node":None}
# result=DFS(node,4)  

#DFS(graph version)
def DFS(node,size):
    #check if the initial node is the goal node
    if goal_test(node['state']):
        print(node)
    # a LIFO queue with node as the only element
    frontier=[node]
    explored=[]
    goal_found=False
    #for i in range(4):
    while goal_found==False:
    #update node and explored state
        #check if the frontier is empty
        if len(frontier)==0:
            print('failure')
        #pop the deepest node from frontier for expansion
        node=frontier[0]
        for n in frontier:
            if n['depth']>node['depth']:
                node=n
        frontier.pop(frontier.index(node))
        #add the pop node state to the explored list
        explored.append(node)
    #update frontier node list
        for result in action(node['state'],size):
            child={"state":result,"path_cost":node['path_cost']+1,"depth":node['depth']+1,"parent_node":node}
            if child['state'] not in [i['state'] for i in explored ] and child not in [i['state'] for i in frontier ]:
            #this need to be check the duplicate of the 'state' rather than the 'node',because the state can be duplicate in different node
                if goal_test(child['state']):
                    goal_found=True
                    print('goal found: '+str(child['state'])+'/'+
                          ' path_cost:'+str(child['path_cost'])+'/'+
                          ' depth:'+str(child['depth'])+'/'+
                          ' parent:'+str(child['parent_node']['state'])+'/'+
                          ' exploredlen:'+str(len(explored))+
                          ' fronlen:'+str(len(frontier))

                         )
                    return child
                frontier.append(child)
                

                

#initial_state={"A":[2,1],"B":[3,2],"C":[4,3],"Agent":[1,1]}
initial_state={"A":[4,1],"B":[4,2],"C":[4,3],"Agent":[4,4]}
node={"state":initial_state,"path_cost":0,"depth":0,"parent_node":None}
result=DFS(node,4)

#3, IDS
def recursive_dls(node,limit,size):    
    #check if the initial node is the goal node
    if goal_test(node['state']):
        return node['state'],node['path_cost'],node['depth'],len(explored)      
    elif limit==0:
        return 'cut off'        
    else:
        explored.append(node)
        cutoff=False

        for i in action(node['state'],size):
            child={"state":i,"path_cost":node['path_cost']+1,"depth":node['depth']+1,"parent_node":node}
            result=recursive_dls(child,limit-1,size) 
            if result=='cut off':
                cutoff=True
            elif result!='failure':
                return result                
        if cutoff==True:
            return 'cut off'            
        else:
            return 'failure'
        
#Iterative deepening search with recursive_dls
def ids(node,size):
    limit=0
    stop=False
    while stop==False:
        result=recursive_dls(node,limit,size)        
        if result!='cut off':
            return result
            stop=True
        limit=limit+1  

initial_state={"A":[2,1],"B":[3,2],"C":[4,3],"Agent":[1,1]}
node={"state":initial_state,"path_cost":0,"depth":0,"parent_node":None}
explored=[]
print(ids(node,4)) 
explored=[]
print(ids(node,5))    
explored=[]
print(ids(node,6))  


#4, A*
#hueristic function:
def h(state,htype):    
    #manhattan distance from current state to goal state of each block
    if htype=='md2goal':
        a=abs(state['A'][0]-2)+abs(state['A'][1]-2)
        b=abs(state['B'][0]-3)+abs(state['B'][1]-2)
        c=abs(state['C'][0]-4)+abs(state['C'][1]-2)
        return a+b+c

    #euclidean distance from current state to goal state of each block
    if htype=='ed2goal':
        a=(abs(state['A'][0]-2)**2+abs(state['A'][1]-2)**2)**0.5
        b=(abs(state['B'][0]-3)**2+abs(state['B'][1]-2)**2)**0.5
        c=(abs(state['C'][0]-4)**2+abs(state['C'][1]-2)**2)**0.5
        return a+b+c

    #misplaced blocks
    if htype=='misplaced':
        l1=[state['A'],state['B'],state['C']]
        l2=[[2,2],[3,2],[4,2]]
        m=0
        for i in range(3):
            if l1[i]!=l2[i]:
                m=m+1
        return m        

    #inversions of permutation of the blocks' row coordinate 
    if htype=='inver_p':   
        l=[[state['A'][0],state['B'][0]],[state['A'][0],state['C'][0]],[state['B'][0],state['C'][0]]]
        inv=0
        for i in l:
            if i[0]>=i[1]:
                inv=inv+1
        return inv  

# A*(tree version)   
def A_star(node,htype,size):
    #check if the initial node is the goal node
    if goal_test(node['state']):
        print(node)
    # a queue with node as the only element
    frontier=[node]
    explored=[]
    goal_found=False
    while goal_found==False:
    #update node and explored state

        #check if the frontier is empty
        if len(frontier)==0:
            print('failure')
        #pop the node with the lowest evaluation function from frontier for expansion
        node=frontier[0]
        for n in frontier:
            if n['path_cost']+n['heuristic']<node['path_cost']+node['heuristic']:
                node=n
        frontier.pop(frontier.index(node))
        #add the pop node state to the explored list
        explored.append(node)
        for result in action(node['state'],size):
            child={"state":result,"path_cost":node['path_cost']+1,"depth":node['depth']+1,"parent_node":node,"heuristic":h(result,htype)}
            if goal_test(child['state']):
                goal_found=True
                print('goal found: '+str(child['state'])+'/'+
                      ' path_cost:'+str(child['path_cost'])+'/'+
                      ' depth:'+str(child['depth'])+'/'+
                      ' parent:'+str(child['parent_node']['state'])+'/'+
                      ' exploredlen:'+str(len(explored))+
                      ' fronlen:'+str(len(frontier))

                     )



            frontier.append(child)

initial_state={"A":[2,1],"B":[3,2],"C":[4,3],"Agent":[1,1]}
htype='md2goal'
node={"state":initial_state,"path_cost":0,"depth":0,"parent_node":None,"heuristic":h(initial_state,htype)} 
A_star(node,htype,4)
A_star(node,htype,5)
A_star(node,htype,6)

#A*(graph version)
def A_star(node,htype,size):
    #check if the initial node is the goal node
    if goal_test(node['state']):
        print(node)
    # a queue with node as the only element
    frontier=[node]
    explored=[]
    goal_found=False
    while goal_found==False:
    #update node and explored state
        #check if the frontier is empty
        if len(frontier)==0:
            print('failure')
        #pop the node with the lowest evaluation function from frontier for expansion
        node=frontier[0]
        for n in frontier:
            if n['path_cost']+n['heuristic']<node['path_cost']+node['heuristic']:
                node=n
        frontier.pop(frontier.index(node))
        #add the pop node state to the explored list
        explored.append(node)
        for result in action(node['state'],size):
            child={"state":result,"path_cost":node['path_cost']+1,"depth":node['depth']+1,"parent_node":node,"heuristic":h(result,htype)}
            if child['state'] not in [i['state'] for i in explored ] and child not in [i['state'] for i in frontier ]:
                #this need to be check the duplicate of the 'state' rather than the 'node',because the state can be duplicate in different node
                if goal_test(child['state']):
                    goal_found=True
                    print('goal found: '+str(child['state'])+'/'+
                          ' path_cost:'+str(child['path_cost'])+'/'+
                          ' depth:'+str(child['depth'])+'/'+
                          ' parent:'+str(child['parent_node']['state'])+'/'+
                          ' exploredlen:'+str(len(explored))+
                          ' fronlen:'+str(len(frontier))

                         )                  


                frontier.append(child)
                
                
#htype='md2goal'
initial_state={"A":[4,1],"B":[4,2],"C":[4,3],"Agent":[4,4]}
htype='md2goal'
node={"state":initial_state,"path_cost":0,"depth":0,"parent_node":None,"heuristic":h(initial_state,htype)} 
A_star(node,htype,4)
A_star(node,htype,5)
A_star(node,htype,6)

#htype='ed2goal'
initial_state={"A":[4,1],"B":[4,2],"C":[4,3],"Agent":[4,4]}
htype='ed2goal'
node={"state":initial_state,"path_cost":0,"depth":0,"parent_node":None,"heuristic":h(initial_state,htype)} 
A_star(node,htype,4)
A_star(node,htype,5)
A_star(node,htype,6)

#htype='misplaced'
initial_state={"A":[4,1],"B":[4,2],"C":[4,3],"Agent":[4,4]}
htype='misplaced'
node={"state":initial_state,"path_cost":0,"depth":0,"parent_node":None,"heuristic":h(initial_state,htype)} 
A_star(node,htype,4)
A_star(node,htype,5)
A_star(node,htype,6)

#htype='inver_p'
initial_state={"A":[4,1],"B":[4,2],"C":[4,3],"Agent":[4,4]}
htype='inver_p'
node={"state":initial_state,"path_cost":0,"depth":0,"parent_node":None,"heuristic":h(initial_state,htype)} 
A_star(node,htype,4)
A_star(node,htype,5)
A_star(node,htype,6)

    
