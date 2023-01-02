### Environment

same as https://github.com/WongKinYiu/yolov7

### Weight file

https://drive.google.com/drive/folders/1pP6w4vPQ6MU4zVU4pygws-sUPLvBdiF3?usp=share_link

### Run code

move /data to /code/data
cd code

> For one GPU:

python train.py --workers 8 --device {your GPU number} --batch-size 6 --data data/coco.yaml --img 640 640 --cfg cfg/training/yolov7.yaml --weights '{weight_file}.pt' --name yolov7-custom --hyp data/hyp.scratch.custom.yaml

> For multiple GPU:

python -m torch.distributed.launch --nproc_per_node 2 --master_port 9527 train.py --workers 8 --device {your GPU number e.g. 0,1} --sync-bn --batch-size 8 --data data/coco.yaml --img 640 640 --cfg cfg/training/yolov7.yaml --weights '{weight_file}.pt' --name yolov7 --hyp data/hyp.scratch.custom.yaml
