def compute_iou(box1, box2):
    x1_1, y1_1, x2_1, y2_1 = box1
    x1_2, y1_2, x2_2, y2_2 = box2

    xx1 = max(x1_1, x1_2)
    yy1 = max(y1_1, y1_2)
    xx2 = min(x2_1, x2_2)
    yy2 = min(y2_1, y2_2)

    w = max(0, xx2 - xx1 + 1)
    h = max(0, yy2 - yy1 + 1)

    common_area = w * h 

    box1_area = (x2_1 - x1_1 + 1) * (y2_1 - y1_1 + 1)
    box2_area = (x2_2 - x1_2 + 1) * (y2_2 - y1_2 + 1)


    iou = common_area / float(box1_area + box2_area - common_area)

    return iou

def non_max_suppression(boxes, scores, iou_threshold):
    sorted_indices = sorted(range(len(scores)), key=lambda k: scores[k], reverse=True)
    kept_indices = []

    while sorted_indices:
        i = sorted_indices.pop(0)
        kept_indices.append(i)

        filtered_indices = []
        for j in sorted_indices:
            iou = compute_iou(boxes[i], boxes[j])
            if iou <= iou_threshold:
                filtered_indices.append(j)
        
        sorted_indices = filtered_indices

    return sorted_indices

boxes = [
    [12, 84, 140, 212], 
    [24, 84, 152, 212],
    [36, 84, 164, 212],
    [12, 96, 140, 224], 
    [24, 96, 152, 224],
    [24, 108, 152, 236]
]

confiden_score = [0.3, 0.4, 0.5, 0.6, 0.7]
iou_threshold = 0.3

print(non_max_suppression(boxes, confiden_score, iou_threshold))