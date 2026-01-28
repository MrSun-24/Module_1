import cv2
import matplotlib.pyplot as plt
cat_image = cv2.imread("binary_cat.png", 0)   # đọc ảnh ở chế độ grayscale
# cv2.imshow("Cat Image", cat_image)            # hiển thị ảnh
# cv2.waitKey(0)                                # chờ phím bất kỳ để đóng
# cv2.destroyAllWindows()                       # đóng tất cả cửa sổ

# x = 0
# y = 0
# pixel_value = cat_image[0][0]
# print(pixel_value)

counts = dict()
height, width = cat_image.shape
for row in range(height):
    for col in range(width):
        counts[cat_image[row,col]] = counts.get(cat_image[row, col], 0) + 1 #get(cat_image[row, col], 0) lay ra gt neu co nguoc lai la 0

names = list(counts.keys())
values = list(counts.values())

plt.bar(range(len(counts)), values, tick_label = names)
plt.show()