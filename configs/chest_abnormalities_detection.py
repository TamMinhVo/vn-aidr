class ChestAbnormalitiesDetectron2Config:
    weights = "trained_models/chest_xray_detection_detectron/chest_xray_abnormalities_20200118.pth"
    labels = [
        'Aortic enlargement',
        'Atelectasis',
        'Calcification',
        'Cardiomegaly',
        'Consolidation',
        'ILD',
        'Infiltration',
        'Lung Opacity',
        'Nodule/Mass',
        'Other lesion',
        'Pleural effusion',
        'Pleural thickening',
        'Pneumothorax',
        'Pulmonary fibrosis',
    ]

class ChestAbnormalitiesYOLOv5Config:
    weights = ["trained_models/chest_xray_detection_yolov5/chest_xray_abnomalities_20200123.pt"]
    device = "cpu"
    imgsz = 512
    conf_thres = 0.5
    iou_thres = 0.45
    agnostic_nms = False