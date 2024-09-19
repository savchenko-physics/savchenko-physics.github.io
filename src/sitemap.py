import os
import time
from xml.etree.ElementTree import Element, SubElement, tostring
from urllib.parse import urljoin

def generate_sitemap(root_dir, base_url, output_file):
    xml_header = """<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n    xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"\n    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n    xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9\n        http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd\n        http://www.google.com/schemas/sitemap-image/1.1\n        http://www.google.com/schemas/sitemap-image/1.1/sitemap-image.xsd">\n"""
    xml_footer = "</urlset>"
    
    urls = []
    
    for dirpath, _, filenames in os.walk(root_dir):
        if 'index.html' in filenames:
            file_path = os.path.join(dirpath, 'index.html')
            
            lastmod = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(os.path.getmtime(file_path)))

            relative_path = os.path.relpath(file_path, root_dir).replace(os.sep, '/')
            url_path = relative_path.replace('index.html', '')  # Assuming URLs don't include 'index.html'
            
            full_url = urljoin(base_url, url_path)

            urls.append(f"      <url>\n        <loc>{full_url}</loc>\n        <lastmod>{lastmod}</lastmod>\n      </url>")

    sitemap_content = xml_header + "\n".join(urls) + "\n" + xml_footer
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(sitemap_content)


def generate_base_sitemap(root_dir, base_url, output_file):
    sitemap_time = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(os.path.getmtime(sitemap1_file)))

    sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
      <sitemap>
         <loc>http://savchenkosolutions.com/sitemap_1.xml</loc>
         <lastmod>{sitemap_time}</lastmod>
      </sitemap>
</sitemapindex>"""

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(sitemap_content)


root_dir = os.getcwd().replace("src", "")
base_url = 'http://savchenkosolutions.com/'
sitemap_file = f'{root_dir}sitemap.xml'
sitemap1_file = f'{root_dir}sitemap_1.xml'

generate_sitemap(root_dir, base_url, sitemap1_file)
generate_base_sitemap(root_dir, base_url, sitemap_file)