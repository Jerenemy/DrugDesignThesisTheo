import dgl
import torch

print(f'DGL version: {dgl.__version__}')
print(f'Torch version: {torch.__version__}')

import dgl.function as fn

# Create a graph with 3 nodes and 2 edges
u, v = torch.tensor([0, 1]), torch.tensor([1, 2])
g = dgl.graph((u, v))

# Initialize node features
g.ndata['h'] = torch.ones(3, 2)

# Define a message function and a reduce function
g.update_all(fn.copy_u('h', 'm'), fn.sum('m', 'h'))

print(g.ndata['h'])
