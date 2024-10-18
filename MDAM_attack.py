import torch 
import utils
import models
import math
import copy
import numpy as np
from agent import Agent
from tqdm import tqdm
from options import args_parser
from aggregation import Aggregation
from torch.utils.tensorboard import SummaryWriter
from torch.utils.data import DataLoader
import torch.nn as nn
from time import ctime
from torch.nn.utils import parameters_to_vector, vector_to_parameters
from utils import H5Dataset
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import pdist
import copy 

torch.backends.cudnn.enabled = True
torch.backends.cudnn.benchmark = True

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
            

     
    
    
      
              