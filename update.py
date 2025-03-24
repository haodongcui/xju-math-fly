import os

def format_file_size(size_in_bytes):
    """将文件大小转换为易读格式"""
    if size_in_bytes >= 1024 * 1024:
        return f"{size_in_bytes/(1024*1024):.2f} MB"
    elif size_in_bytes >= 1024:
        return f"{size_in_bytes/1024:.2f} KB"
    else:
        return f"{size_in_bytes} B"

def generate_index_html(folder_path, output_file, base_url=""):
    """
    生成带文件大小和GitHub链接的目录结构
    """
    with open(output_file, 'w', encoding='utf-8') as html_file:
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
            --text-muted: #6c757d;
        }

        body {
            font-family: 'Segoe UI', system-ui, sans-serif;
            line-height: 1.6;
            margin: 2rem;
            background: #f8f9fa;
        }

        .header-container {
            margin-bottom: 2rem;
        }

        h1 {
            color: var(--primary-color);
            margin-bottom: 0.5rem;
        }

        .github-link {
            display: inline-flex;
            align-items: center;
            color: var(--text-muted);
            text-decoration: none;
            transition: color 0.2s;
        }

        .github-link:hover {
            color: var(--secondary-color);
        }

        .github-icon {
            width: 20px;
            height: 20px;
            margin-right: 8px;
        }

        /* 保持原有样式... */
        .file-info {
            display: flex;
            align-items: baseline;
            gap: 12px;
        }

        .file-size {
            color: var(--text-muted);
            font-size: 0.9em;
            font-family: monospace;
        }

    </style>
</head>
<body>
    <div class="header-container">
        <h1>📂 课程资料目录结构</h1>
        <a href="https://github.com/haodongcui/xju-math-fly" class="github-link">
            <svg class="github-icon" viewBox="0 0 16 16" fill="currentColor">
                <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/>
            </svg>
            项目源代码仓库
        </a>
    </div>
    <div class="tree">\n''')

        # 文件夹遍历逻辑
        for root, dirs, files in os.walk(folder_path):
            relative_path = os.path.relpath(root, folder_path)
            if relative_path == '.':
                continue

            html_file.write(f'<div class="folder">\n')
            html_file.write(f'    <div class="folder-title">{os.path.basename(root)}</div>\n')
            html_file.write('    <ul class="file-list">\n')

            for file in files:
                full_path = os.path.join(root, file)
                file_size = os.path.getsize(full_path)
                formatted_size = format_file_size(file_size)
                
                file_path = os.path.join(relative_path, file)
                link = os.path.join(base_url, file_path).replace("\\", "/") if base_url else file_path.replace("\\", "/")
                
                html_file.write(f'''      <li class="file-item">
            <div class="file-info">
                <span class="file-name">{file}</span>
                <span class="file-size">{formatted_size}</span>
            </div>
            <a href="{link}" target="_blank" class="action-link preview">预览</a>
            <a href="{link}" download class="action-link download">下载</a>
        </li>\n''')

            html_file.write('    </ul>\n</div>\n')

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
