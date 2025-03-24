import os

def generate_index_html(folder_path, output_file, base_url=""):
    """
    遍历指定文件夹，生成层次分明的HTML目录结构
    """
    with open(output_file, 'w', encoding='utf-8') as html_file:
        # 增强的CSS样式
        html_file.write('''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>课程资料目录 - 结构化视图</title>
    <style>
        :root {
            --primary-color: #2c3e50;
            --secondary-color: #3498db;
            --hover-color: #e74c3c;
        }

        body {
            font-family: 'Segoe UI', system-ui, sans-serif;
            line-height: 1.6;
            margin: 2rem;
            background: #f8f9fa;
        }

        h1 {
            color: var(--primary-color);
            border-bottom: 2px solid var(--secondary-color);
            padding-bottom: 0.5em;
            margin-bottom: 1.5rem;
        }

        .tree {
            padding-left: 1rem;
        }

        .folder {
            margin: 1rem 0;
            padding-left: 1.5rem;
            border-left: 2px solid #ddd;
            transition: all 0.3s;
        }

        .folder-title {
            font-size: 1.2em;
            color: var(--primary-color);
            cursor: pointer;
            position: relative;
            padding-left: 28px;
        }

        .folder-title::before {
            content: "📁";
            position: absolute;
            left: 0;
            top: -2px;
        }

        .file-list {
            list-style: none;
            padding-left: 2rem;
            margin: 0.8rem 0;
        }

        .file-item {
            margin: 0.5rem 0;
            padding: 6px 12px;
            background: white;
            border-radius: 4px;
            box-shadow: 0 2px 3px rgba(0,0,0,0.05);
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .file-name {
            flex-grow: 1;
            color: #444;
            font-family: 'Consolas', monospace;
        }

        .action-link {
            color: var(--secondary-color);
            padding: 4px 8px;
            border-radius: 3px;
            transition: all 0.2s;
        }

        .action-link:hover {
            color: var(--hover-color);
            background: rgba(231, 76, 60, 0.1);
            text-decoration: none;
        }

        .download::before {
            content: "⬇️";
            margin-right: 5px;
        }

        .preview::before {
            content: "👁️";
            margin-right: 5px;
        }
    </style>
</head>
<body>
    <h1>📂 课程资料目录结构</h1>
    <div class="tree">\n''')

        # 遍历文件夹结构
        for root, dirs, files in os.walk(folder_path):
            relative_path = os.path.relpath(root, folder_path)
            if relative_path == '.':
                continue  # 跳过根目录

            # 生成文件夹标题
            html_file.write(f'<div class="folder">\n')
            html_file.write(f'    <div class="folder-title">{os.path.basename(root)}</div>\n')
            html_file.write('    <ul class="file-list">\n')

            # 生成文件列表
            for file in files:
                file_path = os.path.join(relative_path, file)
                link = os.path.join(base_url, file_path).replace("\\", "/") if base_url else file_path.replace("\\", "/")
                
                html_file.write(f'''      <li class="file-item">
            <span class="file-name">{file}</span>
            <a href="{link}" target="_blank" class="action-link preview">预览</a>
            <a href="{link}" download class="action-link download">下载</a>
        </li>\n''')

            html_file.write('    </ul>\n</div>\n')

        # 闭合HTML结构
        html_file.write('''    </div>
</body>
</html>''')

# 配置参数
folder_path = './课程资料/'
output_file = './index.html'
base_url = "https://haodongcui.github.io/xju-math-fly/课程资料"

# 生成文件
generate_index_html(folder_path, output_file, base_url)
print(f"✅ HTML文件已生成：{output_file}")
