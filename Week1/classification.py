# Precision = TP / (TP + FP)
# Recall = TP / (TP + FN)
# F1-score = 2 ∗ (Precision ∗ Recall/ Precision + Recall)
# Input: function nhận 3 giá trị tp, fp, fn
# Output: print ra kết quả của Precision, Recall, và F1-score

# Accuracy= (TP+TN) / (TP+TN+FP+FN)

# Precision: Độ chính xác của dự đoán Positive (tích cực)
# Recall: Khả năng phát hiện đúng các trường hợp Positive (tích cực)
# F1-score: Trung bình điều hòa của Precision và Recall, cung cấp một cái nhìn tổng thể về hiệu suất của mô hình.
# Accuracy: Tỷ lệ dự đoán đúng trên tổng số dự đoán.
# Ưu tiên dùng F1-score khi dữ liệu không cân bằng.
def classification_metrics(tp, fp, fn):
    dict_check = {'tp': tp, 'fp': fp, 'fn': fn}

    for key, value in dict_check.items():
        if not isinstance(value, int):
            return f"{key} must be int"
        if value <= 0:
            return "tp and fp and fn must be greater than zero"
    
    precision = tp / (tp + fp) if (tp + fp) != 0 else 0
    recall = tp / (tp + fn) if (tp + fn) != 0 else 0
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) != 0 else 0
        
    print(f"Precision is: {precision}")
    print(f"Recall is: {recall}")
    print(f"F1_score is: {f1_score}")
    return precision, recall, f1_score

# Test case

# precision, recall, f1_score = classification_metrics('a', 3, 4)

print(classification_metrics(2, 4, 5))