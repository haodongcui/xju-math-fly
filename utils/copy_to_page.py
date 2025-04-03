import os
import shutil

def copy_and_rename(source_path, target_path):
    """
    复制文件并重命名
    
    Args:
        source_path (str): 源文件路径
        target_path (str): 目标文件路径（包含新的文件名）
    """
    try:
        # 确保源文件存在
        if not os.path.exists(source_path):
            raise FileNotFoundError(f"源文件不存在：{source_path}")
            
        # 确保目标目录存在
        target_dir = os.path.dirname(target_path)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
            
        # 复制文件并重命名
        shutil.copy2(source_path, target_path)
        print(f"文件已成功复制并重命名：{target_path}")
        
    except Exception as e:
        print(f"复制文件时发生错误：{str(e)}")