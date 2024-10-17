import os
import time
from xml.etree.ElementTree import Element, SubElement, tostring
from urllib.parse import urljoin
from datetime import datetime, timedelta
import git

root_dir = os.getcwd().replace("src", "")
base_url = 'https://savchenkosolutions.com/'

def mark_verified(file_path):
    print(file_path)

repo = git.Repo("C:/Users/melnichenkaa/OneDrive - Berea College/Documents/GitHub/savchenko-physics.github.io")

def get_file_creation_date(repo_path, file_path):
    repos_nick = file_path.split("savchenko-physics.github.io\\")[1]
    text_svc_file = "sitemap\\verified"
    if os.path.exists(text_svc_file):
        with open(text_svc_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                saved_nick, saved_date = line.strip().split()
                if saved_nick == repos_nick:
                    return saved_date

    """Get the creation date of the file from git history."""

    print(repos_nick)


    # The first commit that includes the file is the creation date
    try:
        commits = list(repo.iter_commits(paths=file_path))

        creation_commit = commits[-1]
        creation_date = datetime.fromtimestamp(creation_commit.committed_datetime.timestamp())
        formatted_creation_date = creation_date.strftime('%Y-%m-%dT%H:%M:%SZ')

        with open(text_svc_file, 'a') as f:
            f.write(f"{repos_nick} {formatted_creation_date}\n")
    except:
        creation_time = os.path.getctime(file_path)
        creation_date = datetime.fromtimestamp(creation_time)
        formatted_creation_date = creation_date.strftime('%Y-%m-%dT%H:%M:%SZ')

    return formatted_creation_date


def generate_sitemap():
    print("Generating sitemap")

    xml_header = """<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n    xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"\n    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n    xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9\n        http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd\n        http://www.google.com/schemas/sitemap-image/1.1\n        http://www.google.com/schemas/sitemap-image/1.1/sitemap-image.xsd">\n"""
    xml_footer = "</urlset>"

    recent_urls = []
    older_urls = []

    # Generate a list of redirect-pages
    excluded_urls = [f"{base_url}{i}/" for i in range(1, 15)]
    excluded_urls.append(f"{base_url}en/")

    # Calculate the cutoff date
    cutoff_date = datetime.now() - timedelta(days=3)

    urls = []

    for dirpath, _, filenames in os.walk(root_dir):
        if 'index.html' in filenames:
            file_path = os.path.join(dirpath, 'index.html')
            file_mod_time = os.path.getctime(file_path)

            lastmod = get_file_creation_date(root_dir, file_path)

            # Create the relative and full URL
            relative_path = os.path.relpath(file_path, root_dir).replace(os.sep, '/')
            url_path = relative_path.replace('index.html', '')
            full_url = urljoin(base_url, url_path)

            # Skip excluded URLs
            if full_url in excluded_urls:
                continue

            # Determine if the file is recent or older
            file_mod_datetime = datetime.fromtimestamp(file_mod_time)  # Corrected usage here
            url_entry = f"      <url>\n        <loc>{full_url}</loc>\n        <lastmod>{lastmod}</lastmod>\n      </url>"

            if file_mod_datetime >= cutoff_date:
                recent_urls.append((lastmod, url_entry))
            else:
                older_urls.append((lastmod, url_entry))

    # Sort the URLs by lastmod in descending order (newest first)
    recent_urls.sort(key=lambda x: x[0], reverse=True)
    older_urls.sort(key=lambda x: x[0], reverse=True)

    # Generate the content for sitemap_recent.xml and sitemap_1.xml
    recent_sitemap_content = xml_header + "\n".join([url for _, url in recent_urls]) + "\n" + xml_footer
    older_sitemap_content = xml_header + "\n".join([url for _, url in older_urls]) + "\n" + xml_footer

    # Write the recent URLs to sitemap_recent.xml
    with open(f'{root_dir}sitemap_recent.xml', 'w', encoding='utf-8') as f:
        f.write(recent_sitemap_content)

    # Write the older URLs to sitemap_1.xml
    with open(f'{root_dir}sitemap_1.xml', 'w', encoding='utf-8') as f:
        f.write(older_sitemap_content)

def generate_base_sitemap():
    sitemap_time = get_file_creation_date(root_dir, f"{root_dir}sitemap_1.xml")

    sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
      <sitemap>
         <loc>https://savchenkosolutions.com/sitemap_recent.xml</loc>
         <lastmod>{sitemap_time}</lastmod>
      </sitemap>
      <sitemap>
         <loc>https://savchenkosolutions.com/sitemap_1.xml</loc>
         <lastmod>{sitemap_time}</lastmod>
      </sitemap>
</sitemapindex>"""

    with open(f"{root_dir}sitemap.xml", 'w', encoding='utf-8') as f:
        f.write(sitemap_content)


if __name__ == "__main__":
    generate_sitemap()
    generate_base_sitemap()