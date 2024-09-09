import sys
import difflib

def read_file(file_path):
    """读取文件内容"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"文件未找到: {file_path}")
        return None

def calculate_similarity(text1, text2):
    """计算两个文本的相似度"""
    matcher = difflib.SequenceMatcher(None, text1, text2)
    return matcher.ratio()

def main():
    # 从命令行获取文件路径
    if len(sys.argv) != 4:
        print("使用方法: python main.py <原文文件路径> <抄袭版文件路径> <输出文件路径>")
        return

    original_file = sys.argv[1]
    plagiarized_file = sys.argv[2]
    output_file = sys.argv[3]

    # 读取原文和抄袭版文件
    original_text = read_file(original_file)
    plagiarized_text = read_file(plagiarized_file)

    if original_text is None or plagiarized_text is None:
        return

    # 计算相似度
    similarity = calculate_similarity(original_text, plagiarized_text)

    # 将相似度写入输出文件
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(f"{similarity:.2f}")

    print(f"相似度计算完成，结果已写入 {output_file}")

if __name__ == "__main__":
    main()
