from utils.update_index import *
from utils.update_resource import *
from utils.update_survive import *
from utils.copy_to_page import *


# 生成资源页面
resource_path = '课程资料'
resource_html_path = 'docs/resource.html'
base_url = "https://github.com/haodongcui/xju-math-fly/课程资料"
generate_resource_html(resource_path, resource_html_path, base_url)

# 复制resource.html为index.html
source_path = 'docs/resource.html'
target_path = 'docs/index.html'
copy_and_rename(source_path, target_path)
