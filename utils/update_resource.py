import os

def generate_resource_html(folder_path, output_file, base_url=""):
    """
    遍历指定文件夹，生成包含响应式导航栏的HTML目录结构
    """
    with open(output_file, 'w', encoding='utf-8') as html_file:
        # 生成HTML头部和样式
        html_file.write('''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>课程资料目录</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <style>
        :root {
            --primary-color: #2c3e50;
            --secondary-color: #3498db;
            --hover-color: #e74c3c;
            --nav-height: 60px;
            --bg-color: #f8f9fa;
            --text-color: #444;
            --item-bg: white;
            --border-color: #ddd;
            --shadow-color: rgba(0,0,0,0.05);
            --title-color: var(--primary-color);
        }

        @media (prefers-color-scheme: dark) {
            :root {
                --primary-color: #1a2634;
                --secondary-color: #2980b9;
                --hover-color: #c0392b;
                --bg-color: #1a1a1a;
                --text-color: #e0e0e0;
                --item-bg: #2d2d2d;
                --border-color: #404040;
                --shadow-color: rgba(0,0,0,0.2);
                --folder-title-color: #e0e0e0;
                --title-color: #ffffff;
            }
        }

        body {
            font-family: 'Segoe UI', system-ui, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding-top: var(--nav-height);
            background: var(--bg-color);
            color: var(--text-color);
        }

        .navbar {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            height: var(--nav-height);
            background: var(--primary-color);
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 2rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            z-index: 1000;
        }

        .navbar-brand {
            color: white;
            text-decoration: none;
            font-size: 1.5rem;
            font-weight: bold;
        }

        .navbar-links {
            display: flex;
            gap: 2rem;
            align-items: center;
        }

        .navbar-links a {
            color: white;
            text-decoration: none;
            transition: color 0.3s;
        }

        .navbar-links a:hover {
            color: var(--secondary-color);
        }

        .github-icon {
            font-size: 1.5rem;
        }

        .dropdown {
            display: none;
            position: relative;
        }

        .dropbtn {
            background: none;
            border: none;
            color: white;
            font-size: 1.5rem;
            cursor: pointer;
            padding: 8px;
        }

        .dropdown-content {
            display: none;
            position: absolute;
            right: 0;
            top: 100%;
            background: var(--primary-color);
            min-width: 160px;
            box-shadow: 0 8px 16px rgba(0,0,0,0.2);
            z-index: 1;
        }

        .dropdown-content a {
            color: white;
            padding: 12px 16px;
            text-decoration: none;
            display: block;
            text-align: left;
        }

        .dropdown-content a:hover {
            background: rgba(255,255,255,0.1);
        }

        .show {
            display: block;
        }

        .content {
            padding: 2rem;
        }

        h1 {
            color: var(--title-color);
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
            border-left: 2px solid var(--border-color);
            transition: all 0.3s;
        }

        .folder-title {
            font-size: 1.2em;
            color: var(--primary-color);
            cursor: pointer;
            position: relative;
            padding-left: 28px;
        }

        @media (prefers-color-scheme: dark) {
            .folder-title {
                color: var(--folder-title-color);
            }
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
            background: var(--item-bg);
            border-radius: 4px;
            box-shadow: 0 2px 3px var(--shadow-color);
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .file-name {
            flex-grow: 1;
            color: var(--text-color);
            font-family: 'Consolas', monospace;
            overflow-wrap: anywhere;
            word-break: break-word;
        }

        .action-link {
            color: var(--secondary-color);
            padding: 4px 8px;
            border-radius: 3px;
            transition: all 0.2s;
            font-size: 0.9em;
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

        @media (max-width: 768px) {
            .navbar {
                padding: 0 1rem;
            }
            .navbar-links {
                display: none;
            }
            .dropdown {
                display: block;
            }
            .folder-title {
                font-size: 1.1em;
            }
            .file-item {
                flex-wrap: wrap;
                gap: 8px;
                padding: 8px;
            }
            .file-name {
                flex: 0 0 100%;
                font-size: 0.95em;
            }
            .content {
                padding: 1rem;
            }
            h1 {
                font-size: 1.5em;
            }
            .folder {
                padding-left: 1rem;
            }
            .action-link {
                padding: 3px 6px;
            }
        }
    </style>
</head>
<body>
    <nav class="navbar">
        <a href="https://haodongcui.github.io/xju-math-fly/" class="navbar-brand">飞跃手册</a>
        
        <div class="navbar-links">
            <a href="https://haodongcui.github.io/xju-math-fly/"><span>课程资料</span></a>
            <a href="https://github.com/haodongcui/xju-math-fly" class="github-icon"><i class="fab fa-github"></i></a>
        </div>

        <div class="dropdown">
            <button class="dropbtn"><i class="fas fa-bars"></i></button>
            <div class="dropdown-content">
                <a href="https://haodongcui.github.io/xju-math-fly/index">课程资料</a>
                <a href="https://haodongcui.github.io/xju-math-fly/README.md">编辑资料</a>
                <a href="https://github.com/haodongcui/xju-math-fly"><i class="fab fa-github"></i> GitHub</a>
            </div>
        </div>
    </nav>

    <div class="content">
        <h1>📂 课程资料目录</h1>
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

        # 闭合HTML结构并添加脚本
        html_file.write('''        </div>
    </div>

    <script>
        document.querySelector('.dropbtn').addEventListener('click', function(e) {
            e.stopPropagation();
            document.querySelector('.dropdown-content').classList.toggle('show');
        });

        document.addEventListener('click', function(e) {
            if (!e.target.closest('.dropdown')) {
                document.querySelector('.dropdown-content').classList.remove('show');
            }
        });
    </script>
</body>
</html>''')
        
    print(f"✅ HTML文件已生成：{output_file}")

# 示例用法
if __name__ == "__main__":
    folder_path = '../课程资料/'        # 修改为实际路径
    output_file = '../dist/resource.html' # 输出文件路径
    base_url = "https://haodongcui.github.io/xju-math-fly/课程资料"  # 基础URL
    
    generate_resource_html(folder_path, output_file, base_url)
