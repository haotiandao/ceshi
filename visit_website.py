import requests

def visit_website(url):
    try:
        response = requests.get(url)
        print(f'访问 {url} 返回状态码: {response.status_code}')
    except Exception as e:
        print(f'访问 {url} 失败: {str(e)}')

if __name__ == '__main__':
    visit_website('http://example.com')



