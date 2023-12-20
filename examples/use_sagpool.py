import torch
from ml_wg.classification.sagpool import SAGPool
from torch_geometric.data import Data

num_features = 3
num_classes = 2
model = SAGPool(num_features, num_classes)

# Example data
x = torch.randn((4, num_features))
edge_index = torch.tensor([[0, 1], [1, 2], [2, 3], [3, 0]], dtype=torch.long).t()
data = Data(x=x, edge_index=edge_index)

output = model(data)
print("Output from SAGPool: ", output)
