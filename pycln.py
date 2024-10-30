import ast
import astunparse
import argparse

def remove_unnecessary_stuff(file_path):
    # 读取文件
    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.read()

    # 解析为抽象语法树
    tree = ast.parse(code)

    # 转回 Python 代码
    new_code = astunparse.unparse(tree)

    # 写回文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_code)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="The path of the Python file to clean up")
    args = parser.parse_args()

    remove_unnecessary_stuff(args.file_path)

if __name__ == "__main__":
    main()
