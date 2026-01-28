# Sigmoid

# Sigmoid Function: Sigmoid Function, hay còn được gọi là logistic function, là một trong
# những activation functions cơ bản nhất trong machine learning và neural networks. Hình
# dạng của nó giống như chữ "S". Sigmoid chuyển đổi mọi giá trị đầu vào thành một giá trị
# đầu ra nằm trong khoảng 0 và 1.
# Ứng Dụng: Sigmoid Function thường được sử dụng trong các bài toán phân loại nhị phân,
# nơi mà mục tiêu là phân loại đầu vào thành một trong hai lớp.
# Ưu Điểm:
# – Dễ hiểu và triển khai: Do tính chất đơn giản và phổ biến, Sigmoid được triển khai
# trong nhiều loại mạng neuron.
# – Đầu ra nằm trong khoảng [0,1]: Giá trị đầu ra luôn nằm trong khoảng từ 0 đến 1,
# giúp dễ dàng diễn giải như là xác suất.
# Nhược điểm:
# – Vanishing gradient problem: Khi đầu vào có giá trị lớn hoặc nhỏ, đạo hàm của
# Sigmoid tiệm cận đến 0, dẫn đến vấn đề vanishing gradient (độ dốc biến mất), làm chậm quá trình học của
# mạng.
# – Tâm đối xứng không tại 0: Tâm đối xứng không nằm tại điểm 0, điều này có thể gây
# ra vấn đề trong việc điều chỉnh trọng số trong quá trình học.

def sigmoid(x):
    import math
    return 1. / (1 + math.exp(-x))

# print(sigmoid(0))  # Output: 0.5
# print(sigmoid(2))  # Output: 0.8807970779778823

# ReLU

# ReLU Function: ReLU, viết tắt của "Rectified Linear Unit", là một hàm kích hoạt rất
# phổ biến trong neural networks. Được đánh giá cao vì tính đơn giản nhưng hiệu quả, ReLU
# được sử dụng rộng rãi để giúp neural networks học được những đặc trưng phức tạp mà không
# gặp phải vấn đề biến mất gradient. ReLU hoạt động dựa trên nguyên tắc rất đơn giản: nếu
# đầu vào là số âm, hàm sẽ trả về giá trị 0, còn nếu đầu vào là số dương, hàm sẽ trả về chính
# giá trị đó.
# Ứng dụng: ReLU phổ biến trong các ứng dụng như nhận dạng hình ảnh và xử lý ngôn ngữ
# tự nhiên, nơi ReLU giúp cải thiện tốc độ học và giảm thiểu vấn đề biến mất gradient. 
# ReLU cũng rất quan trọng trong học tăng cường và các tác vụ phân loại, cung cấp một phương
# pháp hiệu quả để xử lý thông tin phi tuyến tính.
# Ưu điểm:
# – Tính toán đơn giản: Do cấu trúc đơn giản, ReLU nhanh và hiệu quả hơn trong việc
# tính toán so với các hàm kích hoạt phi tuyến tính khác.
# – Giảm mất mát gradient: ReLU giúp giảm thiểu vấn đề biến mất gradient, một điểm
# mạnh quan trọng trong quá trình huấn luyện neural networks.
# Nhược điểm:
# – Vấn đề dying ReLU: Đôi khi neuron có thể chỉ trả về giá trị 0 cho tất cả các đầu vào,
# dẫn đến hiện tượng "dying ReLU", khi đó neuron trở nên không hoạt động.
# – Không đối xứng tại zero: Do ReLU không phải là hàm có giá trị trung bình bằng 0
# nên có thể gây ra vấn đề trong quá trình tối ưu hóa mạng.

def relu(x):
    if x <= 0:
        return 0
    else:
        return x
# print(relu(-5))  # Output: 0
# print(relu(5))   # Output: 5

# ELU

# ELU Function: ELU, viết tắt của Exponential Linear Unit, là một loại activation function
# được sử dụng trong neural network. Được đề xuất bởi Djork-Arné Clevert và các cộng sự vào
# năm 2015, ELU nhằm mục đích giải quyết một số vấn đề của các activation functions trước
# đây như ReLU. ELU giảm thiểu vấn đề vanishing gradient ở các giá trị âm, đồng thời vẫn
# duy trì tính phi tuyến cần thiết cho quá trình học sâu.
# Ứng Dụng: ELU chủ yếu được sử dụng trong các mạng neuron sâu, đặc biệt là những
# nơi cần giải quyết vấn đề vanishing gradient. 
# ELU thường được áp dụng trong các mô hình học sâu phức tạp như convolutional neural networks (CNNs) và recurrent neural networks
# (RNNs) để cải thiện tốc độ học và hiệu suất của mô hình.
# Ưu Điểm:
# – Hiệu suất cao: Trong một số trường hợp, ELU cho thấy hiệu suất tốt hơn so với các
# activation functions khác như ReLU và Leaky ReLU, đặc biệt trong các mạng sâu.
# – Có đầu ra âm: Việc này giúp duy trì một phân phối đầu ra cân bằng hơn, có thể cải
# thiện khả năng học của mô hình.
# Nhược Điểm:
# – Tính toán phức tạp hơn: Do cấu trúc phức tạp của công thức, ELU đòi hỏi nhiều chi
# phí tính toán hơn so với ReLU.
# – Lựa chọn α: Việc lựa chọn giá trị của α có thể ảnh hưởng đáng kể đến hiệu suất của
# mô hình và nó không có một quy tắc cụ thể nào, đòi hỏi phải thử nghiệm để tìm ra giá
# trị phù hợp.

def elu(x, alpha=0.01):
    import math
    if x > 0:
        return x
    else:
        return alpha * (math.exp(x) - 1)
print(elu(-1))
# • Kiểm tra activation function name có hợp lệ hay không nằm trong 3 tên (sigmoid,
# relu, elu). Nếu không print ’ten_function_user is not supported’ (vd người dùng
# nhập ’belu’ thì print ’belu is not supported’)
# • Convert x sang float type
# • Thực hiện theo công thức với activation name tương ứng. Print ra kết quả
# • Dùng math.e để lấy số e
# • α = 0.01

def is_number(x):
    try: 
        float(x)
    except ValueError: 
        return False
    return True

def activation_function(x, activation_name):
    valid_functions = ['sigmoid', 'relu', 'elu']

    if activation_name not in valid_functions:
        return f"{activation_name} is not supported"
    
    if not is_number(x):
        return "x must be a number"
    
    x = float(x)

    if activation_name == 'sigmoid':
        return sigmoid(x)
    elif activation_name == 'relu':
        return relu(x)
    elif activation_name == 'elu':
        return elu(x)
    
print(activation_function(3, 'sigmoid'))  # Output: 0.7310585786300049
print(activation_function(-1, 'relu'))    # Output: 0
print(is_number(1))
print(is_number('n'))