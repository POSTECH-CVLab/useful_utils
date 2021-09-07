import numpy as np
import torch
import random
"""
Author: Boseung Jeong and Yoonwoo Jeong
Description: Fixing the seed. When deterministic is true, the seed is 
    completely fixed, but the speed of programs might be slower.
Input (Optional): 
    int seed : seed to fix
    bool deterministic: fix the torch.backends.cudnn.deterministic
Output (Optional): None
Requirements (Optional): 
    numpy, torch, random
"""
def fix_seed(seed, deterministic=True):
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed) # if use multi-GPU
    torch.backends.cudnn.deterministic = deterministic
    torch.backends.cudnn.benchmark = False
    np.random.seed(seed)
    random.seed(seed)