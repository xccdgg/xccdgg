import sys

def read_file(file_path):
    """读取文件内容"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"文件未找到: {file_path}")
        return None

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

    # 暂时不做其他操作，只是读取文件并显示
    print("原文内容:", original_text)
    print("抄袭版内容:", plagiarized_text)

if __name__ == "__main__":
    main()

