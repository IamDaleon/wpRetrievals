import requests
from bs4 import BeautifulSoup

# Replace this with the URL you want to check
url = 'http://flowtech.local/'

# Make a request to the URL and get the HTML content
response = requests.get(url)
html_content = response.text

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the WordPress version in the meta generator tag
wp_version = soup.find('meta', attrs={'name': 'generator'})['content'].split(' ')[1]

# Find the PHP version in the X-Powered-By header
php_version = response.headers['X-Powered-By'].split('/')[1]

# Find the active plugins by looking for script tags that contain 'wp-content/plugins/'
if soup.find('src'):
    plugins = [script['src'] for script in soup.find_all('script') if 'wp-content/plugins/' in script['src']]

scripts = soup.find_all('wp-content')

# Print the results
print(f"WordPress version: {wp_version}")
print(f"PHP version: {php_version}")
# print("Active plugins:")
# for plugin in plugins:
#     print(plugin)
print(scripts)