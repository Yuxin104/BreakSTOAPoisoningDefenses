# -*- coding: utf-8 -*- 
import sys
import torch
from torch import nn
import torchvision
from tqdm import tqdm
from torchvision import transforms
from torch.utils.data import DataLoader
from torch.utils.data import Dataset
import copy
import numpy as np


def CC_attack(a_updates, n_attackers, tau, dev_type='unit_vec'): 
    
    if dev_type == 'sign':
        deviation = torch.sign(a_updates) 

    r = torch.Tensor([10.0]).cuda()

    threshold_diff = 1e-5
    step = r
    r_succ = 0

    while torch.abs(r_succ - r) > threshold_diff:
        mal_update = (a_updates - r * deviation)

        if torch.norm(mal_update)<=tau: 
            r_succ = r
            r = r + step / 2
        else:
            r = r - step / 2

        step = step / 2

    mal_update = (a_updates - r_succ * deviation)

    return mal_update

