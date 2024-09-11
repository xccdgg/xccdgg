import difflib
import re

def read_file(file_path):
    """读取文件内容"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"文件未找到: {file_path}")
        return None

def preprocess_text(text):
    """预处理文本，去除所有非字母数字字符并转换为小写"""
    text = re.sub(r'[^\w\s]', '', text)  # 移除所有非字母数字字符
    text = text.lower()  # 转为小写
    return text

def calculate_similarity(text1, text2):
    """计算两个文本的相似度"""
    matcher = difflib.SequenceMatcher(None, text1, text2)
    return matcher.ratio()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("使用方法: python main.py <原始文件路径> <修改后文件路径> <输出结果路径>")
        sys.exit(1)
    
    orig_path, mod_path, output_path = sys.argv[1], sys.argv[2], sys.argv[3]
    
    orig_text = read_file(orig_path)
    mod_text = read_file(mod_path)
    
    if orig_text is None or mod_text is None:
        sys.exit("读取文件时发生错误，请检查文件路径。")
    
    orig_processed = preprocess_text(orig_text)
    mod_processed = preprocess_text(mod_text)
    
    similarity = calculate_similarity(orig_processed, mod_processed)
    
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(f"相似度: {similarity:.2f}\n")
