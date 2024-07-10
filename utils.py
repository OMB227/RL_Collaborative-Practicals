import difflib
import numpy as np

def compareAndDiff(param,output=True):
    testname,inp,out,errdesc,mark = param
    printout("_"*30 + "\n",output)
    printout(f"Test: {testname}",output)
    printout("_"*30,output)
    if inp != out:
        #[line for line in differ if line.startswith('- ') or line.startswith(' ')]
        printout(f"Error: {errdesc}. Here's the differences:",output)
        printout("\n".join([line for line in difflib.unified_diff(inp.splitlines(), out.splitlines())]),output)
        printout(f"Result: Failed! Mark: 0",output)
        printout("_"*30,output)
        printout("",output)
        return False
    printout(f"Result: Passed! Mark: {mark}",output)
    printout("_"*30,output)
    printout("",output)
    return True

def getMDPAllTransitionandRewards(mdp):
    out = []
    for st in mdp.states:
        out.append(f"State {st} options:")
        for act in mdp.getActions(st):
            out.append(f"Action '{act}': {mdp.getTransitionAndReward(st,act)}")
        out.append("")
    return "\n".join(out)

def printout(s,output=True):
    if not output:
        return
    print(s)

def testCell(params,output=True):

    try:
        results = []
        for param in params:
            results.append(compareAndDiff(param,output))

        marks = sum([int(result)*param[4] for param,result in zip(params,results)])

        if False in results:
            printout(f"Errors were encountered! Current Marks: {marks}",output)
        else:
            printout(f"Looks good from the few tests done! Marks: {marks}",output)
        return marks

    except Exception as e:
        printout("Error: Something went wrong when executing the tests... Re-visit your MDP",output)
        printout("Here's the error:",output)
        printout(e,output)
        return 0.0

def listQValues(mdp,V,getQ):
    return f"Starting with V = {str(V)}\n" + "\n".join([f"({state},{action}):{getQ(mdp,state,action,V)}" for state in mdp.states for action in mdp.getActions(state)])


def formatValueFunction(V,rounding=True,roundnum=3):
    return "\n".join([f"{state}: {val}" if not rounding else f"{state}: {round(val,roundnum)}" for state,val in V.items()])

def formatMazeValueFunctionForMarking(mazemdp,v,rounding=True,roundnum=3):
            
    newmazev = np.empty_like(mazemdp.maze)

    for state in mazemdp.states:
        if state in mazemdp.getTerminalStates():
            continue
        newmazev[state]=v[state] if not rounding else round(v[state],roundnum) 

    return np.array2string(newmazev, separator=',')


def params6(mdp1, mdp2, getValueIteration, getPolicyIteration):
       
    return [("Check Value Iteration on Transport MDP",str(getValueIteration(mdp1)),"{1: -5.489312499949874, 2: -4.988124999979949, 3: -4.43124999999198, 4: -3.8124999999967923, 5: -3.1249999999987166, 6: -3.439, 7: -2.71, 8: -1.9, 9: -1.0, 10: 0.0}","Your value(s) are incorrect",2.5),
            ("Check Policy Iteration on Transport MDP",str(getPolicyIteration(mdp1)[0]),"{1: 'walk', 2: 'walk', 3: 'walk', 4: 'walk', 5: 'subway', 6: 'walk', 7: 'walk', 8: 'walk', 9: 'walk', 10: 'None'}","Your policy entry/entries are incorrect",2.5),
            ("Check Value Iteration on Bungee MDP",str(getValueIteration(mdp2)),"{1: 0.0, 2: 0.0, 3: 0.0, 4: 1.0236686389993523, 5: 2.2485207100397666, 6: 2.0, 7: 0.0, 8: 0.0, 9: 0.0, 10: 0.0, 11: 0.0, 12: 0.0, 13: 0.0, 14: 0.0}","Your value(s) are incorrect",2.5),
            ("Check Policy Iteration on Bungee MDP",str(getPolicyIteration(mdp2)[0]),"{1: -1, 2: -1, 3: -1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: -1, 10: -1, 11: -1, 12: -1, 13: -1, 14: -1}","Your policy entry/entries are incorrect",2.5),
           ]

def params5(mdp1, mdp2, getPolicyEvaluation):
    Vopt1 = getPolicyEvaluation(mdp1,{0: 'draw', 2: 'draw', 3: 'draw', 4: 'stop', 5: 'draw', 'END': 0.0})
    
    Vopt2 = getPolicyEvaluation(mdp2,{(0, 0): (0, 1), (0, 1): (1, 0), (0, 2): (0, -1), (0, 3): 'EXIT', (1, 0): (1, 0), (1, 2): (-1, 0), (1, 3): 'EXIT', (2, 0): (0, 1), (2, 1): (-1, 0), (2, 2): (0, 1), (2, 3): (0, 1), 'TERMINAL_STATE': 0.0})
    
    return [("Check Card Game Values",formatValueFunction(Vopt1),"0: 1.778\n2: 1.333\n3: 0.0\n4: 4.0\n5: 0.0\nEND: 0.0","Your value(s) are incorrect",5),
            ("Check Maze World Values",formatMazeValueFunctionForMarking(mdp2,Vopt2),"[[-0.026,-0.016,-0.024,1.0],\n [-0.131,None,-0.118,-1.0],\n [-0.149,-0.172,-0.386,-0.474]]","Your value(s) are incorrect",5),
           ]


def params4(mdp1, mdp2, getValueIteration):
    Vopt1 = getValueIteration(mdp1)
    
    Vopt2 = getValueIteration(mdp2)
    
    return [("Check Card Game Values",formatValueFunction(Vopt1),"0: 2.507\n2: 2.4\n3: 3.0\n4: 4.0\n5: 5.0\nEND: 0.0","Your value(s) are incorrect",7.5),
            ("Check Maze World Values",formatMazeValueFunctionForMarking(mdp2,Vopt2),"[[-0.101,0.029,0.314,1.0],\n [-0.156,None,-0.025,-1.0],\n [-0.18,-0.168,-0.128,-0.193]]","Your value(s) are incorrect",7.5),
           ]
           
            
            
            
            
def params3(mdp1,mdp2,getQ):
    Vopt1 = {0: 2.91, 2: 2.7, 3: 3.0, 4: 4.0, 5: 5.0, 'END': 0.0}
    Vopt2 = {(0, 0): 0.08196637885701688, (0, 1): 0.19011646207113636, (0, 2): 0.4277620396600567, (0, 3): 1.0, (1, 0): 0.03642950171422971, (1, 2): 0.12747875354107652, (1, 3): -1.0, (2, 0): 0.01656432741497401, (2, 1): 0.023286207179158164, (2, 2): 0.05239396616172714, (2, 3): 0.004763087788198657, 'TERMINAL_STATE': 0.0}
        
    return [("Check Card Game Q Values",listQValues(mdp1,Vopt1,getQ),"Starting with V = {0: 2.91, 2: 2.7, 3: 3.0, 4: 4.0, 5: 5.0, 'END': 0.0}\n(0,draw):2.91\n(2,stop):2.0\n(2,draw):2.7\n(3,stop):3.0\n(3,draw):1.5\n(4,stop):4.0\n(4,draw):0.0\n(5,stop):5.0\n(5,draw):0.0","One or more Q values are incorrect",2.5),
              ("Check Maze World Q Values",listQValues(mdp2,Vopt2,getQ),"Starting with V = {(0, 0): 0.08196637885701688, (0, 1): 0.19011646207113636, (0, 2): 0.4277620396600567, (0, 3): 1.0, (1, 0): 0.03642950171422971, (1, 2): 0.12747875354107652, (1, 3): -1.0, (2, 0): 0.01656432741497401, (2, 1): 0.023286207179158164, (2, 2): 0.05239396616172714, (2, 3): 0.004763087788198657, 'TERMINAL_STATE': 0.0}\n((0, 0),(-1, 0)):0.04639069358921442\n((0, 0),(0, 1)):0.08196637885701688\n((0, 0),(1, 0)):0.02817594273209955\n((0, 0),(0, -1)):0.03870634557136908\n((0, 1),(-1, 0)):0.10153300575430824\n((0, 1),(0, 1)):0.19011646207113636\n((0, 1),(1, 0)):0.10153300575430824\n((0, 1),(0, -1)):0.051798197749920394\n((0, 2),(-1, 0)):0.23061063896757955\n((0, 2),(0, 1)):0.4277620396600567\n((0, 2),(1, 0)):0.11049732451998742\n((0, 2),(0, -1)):0.10380862448851122\n((0, 3),EXIT):1.0\n((1, 0),(-1, 0)):0.03642950171422972\n((1, 0),(0, 1)):0.019498335999291433\n((1, 0),(1, 0)):0.010268681137412576\n((1, 0),(0, -1)):0.019498335999291433\n((1, 2),(-1, 0)):0.12747875354107652\n((1, 2),(0, 1)):-0.37599219970891085\n((1, 2),(1, 0)):-0.02266847585825532\n((1, 2),(0, -1)):0.0749993017075198\n((1, 3),EXIT):-1.0\n((2, 0),(-1, 0)):0.016564327415398494\n((2, 0),(0, 1)):0.011964174328123453\n((2, 0),(1, 0)):0.008618257695696213\n((2, 0),(0, -1)):0.00927542242244979\n((2, 1),(-1, 0)):0.012762397550498324\n((2, 1),(0, 1)):0.02328620718260667\n((2, 1),(1, 0)):0.012762397550498324\n((2, 1),(0, -1)):0.008954351683905421\n((2, 2),(-1, 0)):0.052393966164798446\n((2, 2),(0, 1)):0.010898871100419646\n((2, 2),(1, 0)):0.022360051213058695\n((2, 2),(0, -1)):0.018308118856803453\n((2, 3),(-1, 0)):-0.39714214730250375\n((2, 3),(0, 1)):-0.047856610495310606\n((2, 3),(1, 0)):0.004763087812775752\n((2, 3),(0, -1)):-0.028804259145899215","One or more Q values are incorrect",2.5),
             ] 

def params2(mdp):
    return [("Check Start State",str(mdp.getStartState()),"1","Your start state isn't correct",0.5),
              ("Check Terminal State(s)",str(mdp.getTerminalStates()),"[]","Your terminal state(s) isn't/aren't correct",0.5),
        ("Compare Transitions and Rewards",getMDPAllTransitionandRewards(mdp),"State 1 options:\nAction '-1': [(14, 1.0, 0)]\nAction '1': [(2, 1.0, 0)]\n\nState 2 options:\nAction '-1': [(1, 1.0, 0)]\nAction '1': [(3, 1.0, 0)]\n\nState 3 options:\nAction '-1': [(2, 1.0, 0)]\nAction '1': [(4, 1.0, -1)]\n\nState 4 options:\nAction '-1': [(3, 1.0, 0)]\nAction '1': [(5, 1.0, -1)]\n\nState 5 options:\nAction '-1': [(4, 1.0, 0)]\nAction '1': [(6, 0.6, 2), (4, 0.4, -1)]\n\nState 6 options:\nAction '1': [(7, 1.0, 2)]\n\nState 7 options:\nAction '1': [(8, 1.0, 0)]\n\nState 8 options:\nAction '1': [(9, 1.0, 0)]\n\nState 9 options:\nAction '-1': [(8, 1.0, 0)]\nAction '1': [(10, 1.0, 0)]\n\nState 10 options:\nAction '-1': [(9, 1.0, 0)]\nAction '1': [(11, 1.0, 0)]\n\nState 11 options:\nAction '-1': [(10, 1.0, 0)]\nAction '1': [(12, 1.0, 0)]\n\nState 12 options:\nAction '-1': [(11, 1.0, 0)]\nAction '1': [(13, 1.0, 0)]\n\nState 13 options:\nAction '-1': [(12, 1.0, 0)]\nAction '1': [(14, 1.0, 0)]\n\nState 14 options:\nAction '-1': [(13, 1.0, 0)]\nAction '1': [(1, 1.0, 0)]\n", "Your MDP Transitions and Rewards don't seem to be correct",5),
             ("Get Action for State 5", str(mdp.getActions(5)),"[-1, 1]","Actions aren't correct",1),
             ("Get Action for State 6", str(mdp.getActions(6)),"[1]","Actions aren't correct",1),
              ("Get Action for State 7", str(mdp.getActions(7)),"[1]","Actions aren't correct",1),
            ("Get Actions for State 8", str(mdp.getActions(8)),"[1]","Actions aren't correct",1),
             ] 
        
def params1(mdp):
    return [("Check Start State",str(mdp.getStartState()),"1","Your start state isn't correct",0.5),
              ("Check Terminal State(s)",str(mdp.getTerminalStates()),"[10]","Your terminal state(s) isn't/aren't correct",0.5),
        ("Compare Transitions and Rewards",getMDPAllTransitionandRewards(mdp),"State 1 options:\nAction 'walk': [(2, 1.0, -1.0)]\nAction 'subway': [(2, 0.6, -2.0), (1, 0.4, -2.0)]\n\nState 2 options:\nAction 'walk': [(3, 1.0, -1.0)]\nAction 'subway': [(4, 0.6, -2.0), (2, 0.4, -2.0)]\n\nState 3 options:\nAction 'walk': [(4, 1.0, -1.0)]\nAction 'subway': [(6, 0.6, -2.0), (3, 0.4, -2.0)]\n\nState 4 options:\nAction 'walk': [(5, 1.0, -1.0)]\nAction 'subway': [(8, 0.6, -2.0), (4, 0.4, -2.0)]\n\nState 5 options:\nAction 'walk': [(6, 1.0, -1.0)]\nAction 'subway': [(10, 0.6, -2.0), (5, 0.4, -2.0)]\n\nState 6 options:\nAction 'walk': [(7, 1.0, -1.0)]\n\nState 7 options:\nAction 'walk': [(8, 1.0, -1.0)]\n\nState 8 options:\nAction 'walk': [(9, 1.0, -1.0)]\n\nState 9 options:\nAction 'walk': [(10, 1.0, -1.0)]\n\nState 10 options:\n", "Your MDP Transitions and Rewards don't seem to be correct",5),
              ("Get Actions for State 1", str(mdp.getActions(1)),"['walk', 'subway']","Actions aren't correct",1),
             ("Get Action for State 2", str(mdp.getActions(2)),"['walk', 'subway']","Actions aren't correct",1),
             ("Get Action for State 9", str(mdp.getActions(9)),"['walk']","Actions aren't correct",1),
              ("Get Action for State 10", str(mdp.getActions(10)),"[]","Actions aren't correct",1),
             ]

