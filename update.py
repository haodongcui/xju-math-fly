# from utils.update_index import *
from utils.update_resource import *
# from utils.update_survive import *
# from utils.copy_to_page import *


# 生成资源页面
resource_path = '课程资料'
# resource_html_path = 'resource.html'
resource_html_path = 'index.html'
base_url = "https://haodongcui.github.io/xju-math-fly/课程资料"
generate_resource_html(resource_path, resource_html_path, base_url)
