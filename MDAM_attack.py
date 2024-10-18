import torch 
import numpy as np
import torch.nn as nn
from scipy.spatial.distance import pdist
import copy 

def MDAM_attack(args,agent_updates_dict,avg_updates,agent_id_id_S,agent_data_sizes,dis,i):
    threshold_diff = 1e-3
    r=torch.Tensor([0.1]).float().cuda() 
    step=r
    r_succ = 0
    while torch.abs(r_succ - r) > threshold_diff:
        lamda=r*(avg_updates-agent_updates_dict[i])
        poison_vector=agent_updates_dict[i]+lamda
        max_dis_poi = 0
        for j in agent_id_id_S:
            if args.num_corrupt <= j < args.num_agents:
                distance = poison_vector.sub(agent_updates_dict[j]).norm().item()
                if distance > max_dis_poi:
                        max_dis_poi = distance
        if max_dis_poi < dis : 
            r_succ=r
            r=r-step/2
        else:
            r=r+step/2
        step=step/2
    lamda=r_succ*(avg_updates-agent_updates_dict[i])
    agent_updates_dict[i]=agent_updates_dict[i]+lamda

    return agent_updates_dict, max_dis_poi
            
              
