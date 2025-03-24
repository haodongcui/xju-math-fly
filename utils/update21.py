import os

def generate_index_html(folder_path, output_file, base_url=""):
    """
    遍历指定文件夹，生成一个 HTML 文件，列出所有子文件夹和文件，并为每个文件添加预览和下载链接。
    
    :param folder_path: 要遍历的文件夹路径
    :param output_file: 输出的 HTML 文件名
    :param base_url: 文件的访问基础路径（可选，默认为空）
    """
    with open(output_file, 'w', encoding='utf-8') as html_file:
        html_file.write('<!DOCTYPE html>\n')
        html_file.write('<html lang="en">\n')
        html_file.write('<head>\n')
        html_file.write('<meta charset="UTF-8">\n')
        html_file.write('<title>课程资料目录</title>\n')
        html_file.write('<style>\n')
        html_file.write('body { font-family: Arial, sans-serif; }\n')
        html_file.write('h1 { color: 333; }\n')
        html_file.write('ul { list-style-type: none; padding: 0; }\n')
        html_file.write('li { margin: 5px 0; }\n')
        html_file.write('a { margin-left: 8px; text-decoration: none; }\n')
        html_file.write('a:hover { text-decoration: underline; }\n')
        html_file.write('</style>\n')
        html_file.write('</head>\n')
        html_file.write('<body>\n')
        html_file.write('<h1>课程资料目录</h1>\n')
        html_file.write('<ul>\n')

        for root, dirs, files in os.walk(folder_path):
            relative_path = os.path.relpath(root, folder_path)
            if relative_path == '.':
                continue
            html_file.write(f'<li><strong>{os.path.basename(root)}</strong></li>\n')
            html_file.write('<ul>\n')
            for file in files:
                file_path = os.path.join(relative_path, file)
                if base_url:
                    link = os.path.join(base_url, file_path).replace("\\", "/")
                else:
                    link = file_path.replace("\\", "/")
                # 每个文件项添加预览和下载链接
                html_file.write(
                    f'<li>{file} '
                    f'<a href="{link}" target="_blank">预览</a> '
                    f'<a href="{link}" download>下载</a>'
                    '</li>\n'
                )
            html_file.write('</ul>\n')

        html_file.write('</ul>\n')
        html_file.write('</body>\n')
        html_file.write('</html>\n')

folder_path = '../课程资料/'
output_file = '../index.html'
base_url = "https://haodongcui.github.io/xju-math-fly/课程资料"

generate_index_html(folder_path, output_file, base_url)
print(f"HTML 文件已生成：{output_file}")
