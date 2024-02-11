import os
import re

# 路径设置
posts_dir = './all_collections/_posts'
assets_dir = '/assets/images'

def rename_assets_folder_and_update_links():
    # 遍历Markdown文件
    for filename in os.listdir(posts_dir):
        if filename.endswith('.md'):
            # 解析出新的文件夹名（即Markdown文件的标题部分）
            new_folder_name = filename.split('-', 3)[-1].rstrip('.md')
            
            # 构建旧的资源文件夹路径模式
            old_folder_pattern = re.compile(r'/assets/images/([^/]+)/')
            
            # 读取Markdown文件内容
            md_path = os.path.join(posts_dir, filename)
            with open(md_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # 查找并重命名资源文件夹
            for old_folder in old_folder_pattern.findall(content):
                old_folder_path = os.path.join(assets_dir, old_folder)
                new_folder_path = os.path.join(assets_dir, new_folder_name)
                if os.path.exists(old_folder_path) and not os.path.exists(new_folder_path):
                    os.rename(old_folder_path, new_folder_path)
                    print(f'Renamed folder from {old_folder} to {new_folder_name}')
                
                # 更新Markdown文件中的链接
                new_content = old_folder_pattern.sub(f'/assets/images/{new_folder_name}/', content)
                if new_content != content:
                    with open(md_path, 'w', encoding='utf-8') as file:
                        file.write(new_content)
                    print(f'Updated links in {filename}')

if __name__ == '__main__':
    rename_assets_folder_and_update_links()
