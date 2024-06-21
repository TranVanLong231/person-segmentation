#!/bin/bash
uname -a
#date
#env
date
CS_PATH='/mnt/data/humanparsing/LIP'
LR=3.0e-3
WD=5e-4
BS=8
GPU_IDS=0,1,2,3
RESTORE_FROM='./dataset/resnet101-imagenet.pth'
INPUT_SIZE='473,473'  
SNAPSHOT_DIR='./snapshots'
DATASET='train'
NUM_CLASSES=20 
EPOCHS=150

if [[ ! -e ${SNAPSHOT_DIR} ]]; then
    mkdir -p  ${SNAPSHOT_DIR}
fi
python train_simplified.py