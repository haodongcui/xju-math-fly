import os

def generate_index_html(folder_path, output_file, base_url=""):
    """
    遍历指定文件夹，生成一个 HTML 文件，列出所有子文件夹和文件，并为文件名添加链接。
    
    :param folder_path: 要遍历的文件夹路径
    :param output_file: 输出的 HTML 文件名
    :param base_url: 文件的访问基础路径（可选，默认为空）
    """
    # 打开输出文件
    with open(output_file, 'w', encoding='utf-8') as html_file:
        # 写入 HTML 文件的头部
        html_file.write('<!DOCTYPE html>\n')
        html_file.write('<html lang="en">\n')
        html_file.write('<head>\n')
        html_file.write('<meta charset="UTF-8">\n')
        html_file.write('<title>课程资料目录</title>\n')
        html_file.write('<style>\n')
        html_file.write('body { font-family: Arial, sans-serif; }\n')
        html_file.write('h1 { color: #333; }\n')
        html_file.write('ul { list-style-type: none; padding: 0; }\n')
        html_file.write('li { margin: 5px 0; }\n')
        html_file.write('</style>\n')
        html_file.write('</head>\n')
        html_file.write('<body>\n')
        html_file.write('<h1>课程资料目录</h1>\n')
        html_file.write('<ul>\n')

        # 遍历文件夹
        for root, dirs, files in os.walk(folder_path):
            # 获取当前文件夹的相对路径
            relative_path = os.path.relpath(root, folder_path)
            if relative_path == '.':
                # 如果是根目录，直接跳过
                continue
            # 写入子文件夹名
            html_file.write(f'<li><strong>{os.path.basename(root)}</strong></li>\n')
            html_file.write('<ul>\n')
            # 写入子文件夹下的文件
            for file in files:
                # 构造文件的完整路径（相对于 base_url）
                file_path = os.path.join(relative_path, file)
                if base_url:
                    link = os.path.join(base_url, file_path).replace("\\", "/")  # 确保路径分隔符为 '/'
                else:
                    link = file_path.replace("\\", "/")  # 确保路径分隔符为 '/'
                # html_file.write(f'<li><a href="{link}" target="_blank">{file}</a></li>\n')
                # 每个文件项添加预览和下载链接
                html_file.write(
                    f'<li>{file} '
                    f'<a href="{link}" target="_blank">预览</a> '
                    f'<a href="{link}" download>下载</a>'
                    '</li>\n'
                )
            html_file.write('</ul>\n')

        # 写入 HTML 文件的尾部
        html_file.write('</ul>\n')
        html_file.write('</body>\n')
        html_file.write('</html>\n')

# 设置文件夹路径和输出文件名
folder_path = './课程资料/'
output_file = './index.html'

# 可选：设置文件的基础访问路径（例如本地服务器路径）
# base_url = "./课程资料"
base_url = "https://haodongcui.github.io/xju-math-fly/课程资料"

# 调用函数生成 HTML 文件
generate_index_html(folder_path, output_file, base_url)

print(f"HTML 文件已生成：{output_file}")
