def caculate_areaA(xAmin,yAmin, xAmax, yAmax):
    return (xAmax - xAmin) * (yAmax - yAmin)

def caculate_areaB(xBmin, yBmin, xBmax, yBmax):
    return (xBmax - xBmin) * (yBmax - yBmin)

def caculate_area(xA,yA,xB,yB):
    return (xB-xA) * (yB - yA)

def caculate_IoU(xAmin,yAmin, xAmax, yAmax, xBmin, yBmin, xBmax, yBmax, xA,yA,xB,yB):
    union_area = caculate_areaA(xAmin,yAmin, xAmax, yAmax) + caculate_areaB(xBmin, yBmin, xBmax, yBmax) - caculate_area(xA,yA,xB,yB)
    return caculate_area(xA,yA,xB,yB) / union_area

xAmin = 0
yAmin = 0
xAmax = 5
yAmax = 5
xBmin = 2.5
yBmin = 2.5
xBmax = 7.5
yBmax = 7.5
xA = max(xAmin, xBmin)
yA = max(yAmin, yBmin)
xB = min(xAmax, xBmax)
yB = min(yAmax, yBmax)

result = caculate_IoU(xAmin,yAmin, xAmax, yAmax, xBmin, yBmin, xBmax, yBmax, xA,yA,xB,yB)
print(result)


def computeIOU(boxA, boxB):
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])

    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])

    common_area = max(0, xB - xA + 1) * max(0, yB - yA + 1)
    
    boxA_area = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
    boxB_area = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)

    iou = common_area / float(boxA_area + boxB_area - common_area)

    return iou

boxA = (0, 0, 5, 5)
boxB = (2.5, 2.5, 7.5, 7.5)
iou = computeIOU(boxA, boxB)
print(iou)