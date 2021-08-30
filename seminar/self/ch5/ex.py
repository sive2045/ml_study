import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool
import time
import random

def random_walk_(seed_):
    random.seed(seed_)
    
    fig = plt.figure(figsize=(12,6))
    
    for i in range(1000):
        walk_ = [0]
        for j in range(1000):
            walk_.append(random.uniform(-1,1) + walk_[-1])
        plt.plot(walk_,alpha=0.5)
        
    #plt.savefig(f'{seed_}.png')
    plt.close(fig)
    
    return None

def process_B():
    num_cores = 16
    pool = Pool(num_cores)
    pool.map(random_walk_,range(500))

if __name__ == '__main__':
    start = int(time.time())
    process_B()
    print(int(time.time() - start))
