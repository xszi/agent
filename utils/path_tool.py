"""
@File    :   path_tool.py
@Time    :   2026/05/26 15:35:12
@Author  :   lulu 
@Version :   1.0
@Desc    :   None
为整个工程提供统一的绝对路径
"""

import os
from py_compile import main

def get_project_root() -> str:
    """
    获取工程所在根目录
    return 字符串根目录
    """

    # 当前文件的绝对路径
    current_file_path = os.path.abspath(__file__)
    # print(current_file_path)
    # 获取工程的根目录，先获取文件所在的文件夹绝对路径
    current_dir = os.path.dirname(current_file_path)
    # print(current_dir)
    # 再获取工程的根目录，即当前文件夹的父文件夹
    project_root = os.path.dirname(current_dir)

    # aaa = os.path.dirname(project_root)
    # print(aaa)
    return project_root


def get_abs_path(relative_path: str) -> str:
    """
    获取相对于工程根目录的绝对路径
    return 字符串绝对路径
    """
    project_root = get_project_root()
    return os.path.join(project_root, relative_path)

if __name__ == '__main__':
    print(get_abs_path("config/config.txt"))