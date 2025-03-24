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
    <h1>📂 课程资料目录</h1> 
    <a href="https://github.com/haodongcui/xju-math-fly" class="github-link">
            <svg class="github-icon" viewBox="0 0 16 16" fill="currentColor">
                <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/>
            </svg>
            项目源代码仓库
        </a>
    </div>
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
