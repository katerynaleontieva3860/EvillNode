import time
import matplotlib.pyplot as plt
import numpy as np
import random
import pylab
import numpy.random as rand
from numpy.random import choice

# assert(len(nodes_pool) == len(nodes_pool_E + nodes_pool_G))
# def epoch():
#     years = 100
#     month = years * 12
#     days = month * 30
#     hours = days * 24   
#     minuts = hours * 60
#     seconds = minuts * 60

def sim(N): # Simulation should run N epochs
    amount_good_nodes = 700000 
    amount_evil_nodes = 300000

    nodes_pool_E = np.ones(amount_evil_nodes, dtype=int) #1 evil_node TRUE
    nodes_pool_G = np.zeros(amount_good_nodes, dtype=int) # 0  good_nodes FALSE

    nodes_pool = np.concatenate((nodes_pool_G,nodes_pool_E)) # add array n_nodes_E+ n_nodes_G
    np.random.shuffle(nodes_pool) #make random 
    x = []
    y = []
    for i in range(1, N+1): # amount of N epochs run 
        x.append(i)
        amount_active_pool = 0
        cur_amount_evils = 0
        cur_pool = []
        amount_active_pool = np.random.randint(10,1000) # random nodes in the active pool
        
        for j in range(1, amount_active_pool+1):
            a = np.random.choice(nodes_pool) # choose new random nodes in the pool
            cur_pool.append(a) # add to current evil pool 
            for l in range(0, len(nodes_pool)-1): # delete node which was chosen early
                if nodes_pool[l] == a:
                    nodes_pool = np.delete(nodes_pool, [l])
                    break
        for k in cur_pool: #if he majority in the pool is evil
            if k == 1:
                cur_amount_evils += 1
                	
        y.append(cur_amount_evils)
        if cur_amount_evils / amount_active_pool >= 0.3: #we should print the event with details of configuration that ran.
            print("Evilnodes:", cur_amount_evils,"Amount nodes in active pool:", amount_active_pool,len(nodes_pool)) #vse vivesti tyt
        else:
            print("Goodnodes",len(nodes_pool))
    plt.figure(figsize=(12, 7))
    plt.title('Evil Nodes', fontsize=20, fontname='Times New Roman')

    plt.xlabel('Amount active pool',color='gray')
    plt.ylabel('Current Evil nodes ',color='gray')

    plt.grid(True)#cell
    plt.grid(which="major", linewidth=1.2)
    plt.grid(which="minor", linestyle="--", color="gray", linewidth=0.5)

    plt.plot(x, y,'v-.g', label="EvilNodes", mec='m', lw=1, mew=0.2, ms=8)
    plt.legend()
    plt.show()

sim(100) # 100 iterations,1000 iterations 

