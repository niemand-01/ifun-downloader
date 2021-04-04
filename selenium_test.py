import json
from selenium import webdriver
import re
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def get_video_url(url):
	caps = DesiredCapabilities.CHROME
	caps['goog:loggingPrefs'] = {'performance': 'ALL'}
	driver = webdriver.Chrome(desired_capabilities=caps)
	driver.get(url)
	browser_log = driver.get_log('performance') 
#print(browser_log[0])

	for entry in browser_log:
		response = json.loads(entry['message'])
		if "media_0" in str(response):
    			authority = response["message"]["params"]["headers"][":authority"]
    			path = response["message"]["params"]["headers"][":path"]
    			break

	vurl = "https://"+authority+path
	driver.close()
	return vurl
#events = [event for event in events if 'Network.response' in event['method']]
#with open('response.txt','w') as out:
#	json.dump(browser_log,out)
#print(events)

"""
print(type(browser_log))
reg_str = 'https:.*media_0\.ts.*\\"'
def get_video_url(entry):
	m = re.search(reg_str,str(entry))
	print(m.group(0))
	return m[0]
get_video_url(browser_log)
"""