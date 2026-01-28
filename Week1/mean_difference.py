# Mean Difference of n
# th Root Error: là một kỹ thuật thông dụng
# trong các ứng dụng như phát hiện và theo dõi đối tượng. Ngoài ra, phương pháp này cũng có thể
# được áp dụng cho các bài toán hồi quy khác. Cụ thể, chúng ta sẽ tính căn bậc n của cả yi và yˆi
# trước khi tính toán hàm lỗi, theo công thức sau:
import math
def convert_to_exponent(n, m):
    return math.pow(n, 1 / m)

def loss(y, y_hat, n, p):
    convert_y = convert_to_exponent(y, n)
    convert_y_hat = convert_to_exponent(y_hat, n)
    return math.pow(convert_y - convert_y_hat, p)

# def mean_diference(m, n, y, y_hat, p):
#     for i in range(m):

print(loss(100, 99.5, 2, 1))