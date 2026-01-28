# Viết function lựa chọn regression loss function để tính loss:

# MAE =  1n∑ni=1|yi−y^i| 

# MSE =  1n∑ni=1(yi−y^i)2 

# RMSE =  MSE−−−−−√  =  1n∑ni=1(yi−y^i)2−−−−−−−−−−−−−−√ 

# n chính là số lượng samples (num_samples), với i là mỗi sample cụ thể. Ở đây các bạn có thể hiểu là cứ mỗi i thì sẽ có 1 cặp  yi  là target và  y^  là predict.

# Input:

# Người dùng nhập số lượng sample (num_samples) được tạo ra (chỉ nhận integer numbers)
# Người dùng nhập loss name (MAE, MSE, RMSE-(optional)) chỉ cần MAE và MSE, bạn nào muốn làm thêm RMSE đều được.
# Output:

# Print ra loss name, sample, predict, target, loss
# loss name: là loss mà người dùng chọn
# sample: là thứ tự sample được tạo ra (ví dụ num_samples=5, thì sẽ có 5 samples và mỗi sample là sample-0, sample-1, sample-2, sample-3, sample-4)
# predict: là số mà model dự đoán (chỉ cần dùng random tạo random một số trong range [0,10))
# target: là số target mà momg muốn mode dự đoán đúng (chỉ cần dùng random tạo random một số trong range [0,10))
# loss: là kết quả khi đưa predict và target vào hàm loss
# note: ví dụ num_sample=5 thì sẽ có 5 cặp predict và target.
# Note: Các bạn lưu ý

# Dùng .isnumeric() method để kiểm tra num_samples có hợp lệ hay không (vd: x='10', num_samples.isnumeric() sẽ trả về True ngược lại là False). Nếu không hợp lệ print 'number of samples must be an integer number' và dừng chương trình.
# Dùng vòng lặp for, lặp lại num_samples lần. Mỗi lần dùng random modules tạo một con số ngẫu nhiên trong range [0.0, 10.0) cho predict và target. Sau đó predict và target vào loss function và print ra kết quả mỗi lần lặp.
# Dùng random.uniform(0,10) để tạo ra một số ngẫu nhiên trong range [0,10)
# Giả xử người dùng luôn nhập đúng loss name MSE, MAE, và RMSE (đơn giảng bước này để các bạn không cần check tên hợp lệ)
# Dùng abs() để tính trị tuyệt đối ví dụ abs(-3) sẽ trả về 3
# Dùng math.sqrt() để tính căn bậc 2

def cacl_ae(target, predict):
    return abs(target - predict)

def calc_se(target, predict):
    return (target - predict) ** 2

def calc_loss(num_samples, loss_name):
    import random
    import math

    num_samples = int(num_samples)
    total_loss = 0
    for i in range(num_samples):
        target = random.uniform(0, 10)
        predict = random.uniform(0, 10)

        if loss_name == 'MAE':
            loss = cacl_ae(target, predict)
        elif loss_name == 'MSE':
            loss = calc_se(target, predict)
        elif loss_name == 'RMSE':
            loss = math.sqrt(calc_se(target, predict))
        else:
            print(f"{loss_name} is not supported")
            return
        total_loss += loss
        print(f"loss name: {loss_name}, sample-{i}, predict: {predict}, target: {target}, loss: {loss}")
    if loss_name == 'MAE':
        print(f"Final {loss_name}: {total_loss / num_samples}")
    elif loss_name == 'MSE':
        print(f"Final {loss_name}: {total_loss / num_samples}")
    elif loss_name == 'RMSE':
        print(f"Final {loss_name}: {math.sqrt(total_loss / num_samples)}")
    
# Example usage:
num_samples = input('Input number of samples (integer number) wich are generated: ')
if not num_samples.isnumeric():
    print('number of samples must be an integer number')
    exit()

loss_name = input('Input loss name (MAE, MSE, RMSE): ')
calc_loss(num_samples, loss_name)
