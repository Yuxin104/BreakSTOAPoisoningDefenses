import torch 
import numpy as np
from scipy.spatial.distance import pdist
            
def FLAME_attack(args,agent_updates_dict,avg_updates,agent_id_id,i,dis):
    threshold_diff = 1e-3
    r=torch.Tensor([0.1]).float().cuda() 
    step=r
    r_succ = 0
    while torch.abs(r_succ - r) > threshold_diff:
        lamda=r*(avg_updates-agent_updates_dict[i])
        agent_updates_dict_temp=agent_updates_dict[i]+lamda
        poison_vector=agent_updates_dict_temp*np.linalg.norm(agent_updates_dict[i].cpu())/np.linalg.norm(agent_updates_dict_temp.cpu())
        max_dis_poi=0
        for j in agent_id_id:
            if args.num_corrupt <= j < args.num_agents:
                vec = np.vstack([agent_updates_dict[j].cpu(),poison_vector.cpu()])
                dis_poi_temp = pdist(vec,'cosine')
                if dis_poi_temp > max_dis_poi:
                    max_dis_poi = dis_poi_temp
                vec = np.vstack([poison_vector.cpu(),agent_updates_dict[j].cpu()])
                dis_poi_temp = pdist(vec,'cosine')
                if dis_poi_temp > max_dis_poi:
                    max_dis_poi = dis_poi_temp
        if max_dis_poi < dis :
            r_succ=r
            r=r-step/2
        else:
            r=r+step/2
        step=step/2
    lamda=r_succ*(avg_updates-agent_updates_dict[i])
    agent_updates_dict_temp=agent_updates_dict[i]+lamda
    agent_updates_dict[i]=agent_updates_dict_temp*np.linalg.norm(agent_updates_dict[i].cpu())/np.linalg.norm(agent_updates_dict_temp.cpu())
    return agent_updates_dict, max_dis_poi


              