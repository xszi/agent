import os
import hashlib
import turtle
from utils.logger_handler import logger
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader, TextLoader


def get_file_md5_hex(file_path: str) -> str:

    if not os.path.exists(file_path):
        logger.error(f"[md5计算]文件{file_path}不存在")
        return

    if not os.path.isfile(file_path):
        logger.error(f"[md5计算]路径{file_path}不是文件")

    md5_obj = hashlib.md5()

    chunk_size = 4096 # 4kb分片，避免一次性读取大文件爆内存

    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(chunk_size):
                md5_obj.update(chunk)

                """
                chunk = f.read(chunk_size)
                while chunk:
                    md5_obj.update(chunk)
                    chunk = f.read(chunk_size)
                """
                md5_hex = md5_obj.hexdigest()
                return md5_hex
    except Exception as e:
        logger.error(f"计算文件{file_path}md5失败: {str(e)}")
        return

def listdir_with_allowed_type(dir_path: str, allowed_types: tuple[str]) -> tuple[str]: # 返回文件夹内的文件列表（允许的文件后缀）
    files = []

    if not os.path.isdir(dir_path):
        logger.error(f"[listdir_with_allowed_type]{dir_path}不是文件夹")
        return tuple(files)
    
    for f in os.listdir(dir_path):
        if f.endswith(allowed_types):
            files.append(os.path.join(dir_path, f))

    return tuple(files)

def pdf_loader(file_path: str, passwd: str=None) -> list[Document]:
    return PyPDFLoader(file_path, passwd).load()

def txt_loader(file_path: str) -> list[Document]:
    return TextLoader(file_path, encoding='utf-8').load()