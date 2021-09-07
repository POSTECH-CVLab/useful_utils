# Utils Collection

## Motivation
When we implement codes, we often search for util functions that are already implemented. 
Here, we are going to share util functions that are often used by others.

## Participation
To participate on this repository, send a message to "Yoonwoo" so that he'll add you as a collaborator.

## Adding Rule
- You should provide a code in folder and short description about the code. 
- Never push on master. We have prohibited direct push on main branch. Use pull request to avoid confusion. 
- After adding an util function, add an item in the list below. 
- Please refer to other formats. 
- It is not necessary to be a python code. Feel free to add util functions. 
- We strongly recommend to add the description as the following format: 

Example 
```
Author: YoonwooJeong
Description: Example for Addition
Input (Optional): 
    torch.Tensor a : the first number to add
    torch.Tensor b : the second number to add
Output (Optional): 
    torch.Tensor out: the addition of "a" and "b". 
Requirements (Optional): 
    numpy >= 0.0.1, torch >= 0.0.1
```

## Util Functions
- Fixing the seed (torch_function/fix_seed.py)
    - A function to completely fix the seeds of torch, numpy, and random.
