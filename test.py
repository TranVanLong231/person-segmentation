from dataset.datasets import LIPDataSet,LIPDataValSet
import torchvision.transforms as T
import torch
transform = T.Compose([
        T.ToTensor(),
        T.Normalize(mean = [0.485, 0.456, 0.406], std = [0.229, 0.224, 0.225])
    ])
train =LIPDataValSet('./datasets/CIHP','val',transform=transform)

for i in range(len(train)):
    if(i==182):
        s=1
    input, label_parsing, hgt,wgt,hwgt, meta =train[i]
    a= torch.unique(label_parsing)
    
    print(f"Loss {i} {a[a==22]}")
