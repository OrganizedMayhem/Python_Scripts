import requests
import time
import selenium


r = requests
s = selenium
r.get("https://hawks.brooklyn.aspect-cloud.net/manux/auth")
print r.get("https://hawks.brooklyn.aspect-cloud.net/manux/auth")
s.webdriver.Firefox.start_session()
s.webdriver.Firefox.get(self, "https://hawks.brooklyn.aspect-cloud.net/manux/auth")
