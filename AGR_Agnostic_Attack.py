import torch 

def AGR_Agnostic_Attack(args,agent_updates_dict,agent_id_id,avg_updates,i,dis):
    threshold_diff = 1e-3
    r=torch.Tensor([0.1]).float().cuda() 
    step=r
    r_succ = 0
    while torch.abs(r_succ - r) > threshold_diff:
        lamda=r*(avg_updates-agent_updates_dict[i])
        poison_vector=agent_updates_dict[i]+lamda
        max_dis_poi = 0
        for j in agent_id_id:
            if args.num_corrupt <= j < args.num_agents:
                vec=poison_vector-agent_updates_dict[j]
                distance = torch.norm(vec)
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
       
        