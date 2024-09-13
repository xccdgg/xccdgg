import sys
import re
from difflib import SequenceMatcher

def read_file(file_path):
    """读取文件内容，如果文件不存在，返回None。"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"文件未找到: {file_path}")
        return None

def preprocess_text(text):
    """预处理文本，去除所有非字母数字字符并转换为小写。"""
    return re.sub(r'[^\w\s]', '', text).lower()

def calculate_similarity(text1, text2):
    """计算两个文本的相似度，使用difflib库。"""
    if not text1 or not text2:
        return 0.0
    return SequenceMatcher(None, text1, text2).ratio()

def main():
    if len(sys.argv) != 4:
        print("使用方法: python main.py <原始文件路径> <抄袭版文件路径> <输出文件路径>")
        sys.exit(1)
    
    original_file, plagiarized_file, output_file = sys.argv[1], sys.argv[2], sys.argv[3]
    
    original_text = read_file(original_file)
    plagiarized_text = read_file(plagiarized_file)
    
    if original_text is None or plagiarized_text is None:
        print("一个或多个文件未找到。")
        sys.exit(1)
    
    original_processed = preprocess_text(original_text)
    plagiarized_processed = preprocess_text(plagiarized_text)
    
    similarity = calculate_similarity(original_processed, plagiarized_processed)
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(f"相似度: {similarity:.2f}\n")
    
    print(f"相似度计算完成，结果已写入 {output_file}")

if __name__ == "__main__":
    main()