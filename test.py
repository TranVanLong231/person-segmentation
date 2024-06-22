from dataset.datasets import LIPDataSet,LIPDataValSet
import torchvision.transforms as T
import torch
from networks.CDGNet import Res_Deeplab
state = torch.load('./dataset/CE2P/LIP_epoch_149.pth')
model = Res_Deeplab(22)
model.load_state_dict(state)
