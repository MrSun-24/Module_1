import torch

def nms(P, thresh_iou):
    x1 = P[:, 0] #tensor([ 30,  35, 200])
    x2 = P[:, 1]
    y1 = P[:, 2]
    y2 = P[:, 3]

    #confidence score
    scores = P[:, 4]

    # x1 = P[:, 0]  # tensor([12, 24, 36, 12, 24, 24])
    # x2 = P[:, 1]  # tensor([ 84,  84,  84,  96,  96, 108])
    # y1 = P[:, 2]  # tensor([140, 152, 164, 140, 152, 152])
    # y2 = P[:, 3]  # tensor([212, 212, 212, 224, 224, 236])
    # scores = P[:, 4]  # tensor([0.3, 0.4, 0.5, 0.6, 0.7, 0.8])

    #Tinh dien tich cac boxes
    areas = (x2 - x1) * (y2 - y1)
    # areas = tensor([5184, 3600, 2304, 7056, 5184, 7056])

    # sap xep tang dan lai "index" (ko phai giá trị) cac box theo confidence core
    order = scores.argsort()
    # order = [0, 1, 2, 3, 4, 5]

    keep = []

    # tim box co diem score cao nhât trong tạp P
    while len(order) > 0:
        idx = order[-1] # lấy index của box có confidence cao nhất
        #idx = 5

        keep.append(P[idx]) # đưa box đó vào tập keep
        # [(24,108,152,236,0.8)]

        order = order[:-1] # Xóa box đó ra khỏi tập P
        # order = [0,1,2,3,4]
        
        # Lay toa do cac box con lai trong P
        xx1 = torch.index_select(x1, dim=0, index=order)
        # xx1= [12, 24, 36, 12, 24]
        xx2 = torch.index_select(x2, dim=0, index=order)
        yy1 = torch.index_select(y1, dim=0, index=order)
        yy2 = torch.index_select(y2, dim=0, index=order)

        xx1 = torch.max(xx1, x1[idx])
        #xx1= torch.max([12,24,36,12,24], 24) = [24,24,36,24,24]
        yy1 = torch.max(yy1, y1[idx])
        xx2 = torch.min(xx2, x2[idx])
        #xx2 = [84,84,84,96,96] → min với 108 → [84,84,84,96,96]
        yy2 = torch.min(yy2, y2[idx])

        w = xx2 - xx1
        h = yy2 - yy1

        w = torch.clamp(w, min=0.0) #[60,60,48,72,72]
        h = torch.clamp(h, min=0.0) #[60,60,48,72,72]

        inter = w*h #[3600,3600,2304,5184,5184]

        rem_areas = torch.index_select(areas, dim = 0, index = order) #[5184, 3600, 2304, 7056, 5184, 7056]
        union = (rem_areas - inter) + areas[idx] #([5184,3600,2304,7056,5184] - [3600,3600,2304,5184,5184]) + 7056
        IoU = inter / union #[0.4166, 0.5102, 0.3266, 0.5808, 0.7346]

        mask = IoU < thresh_iou # < 0.14 → [False, False, False, False, False]
        order = order[mask]

    return keep

P = torch.tensor([
    (12, 84, 140, 212, 0.3),
	(24, 84, 152, 212, 0.4),
	(36, 84, 164, 212, 0.5),
	(12, 96, 140, 224, 0.6),
	(24, 96, 152, 224, 0.7),
	(24, 108, 152, 236, 0.8)
])

print(nms(P, 0.14))