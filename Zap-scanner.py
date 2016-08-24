import time, collections, prettytable, zapv2
from zapv2 import ZAPv2
from collections import defaultdict
from time import sleep

# p = Popen('ZAP.exe', cwd='C:\Program Files (x86)\OWASP\Zed Attack Proxy')
# stdout, stderr = p.communicate()

zap = ZAPv2()

print "Starting ZAP..."

# This is the API Key (Change if needed)
key = ''

# Enable Auto Re-Authentication
zap.auth.auto_reauth_on(apikey=key)

print 'Must include http(s):// in target URL'
target = raw_input('URL to Scan? ')

# Variables used in Authentication (HTTP/NTLM Authentication)
port = raw_input('Port? ')

# Request Username and Password for Application login
username = raw_input('Username? ')
password = raw_input('Password? ')

# Configure Authentication
print ''
print 'Select an Authentication Method: '
print ''
print '1. Form Based Authentication'
print '2. HTTP/NTLM Authentication'

AuthenticationMethod = input('Input Line Item from Above: ')

# Input Validation (Checks for Valid selection)
if AuthenticationMethod == 1:
	print ''
	print 'Setting Authentication Method to Form-Based Authentication'
	print ''
	zap.authentication.set_authentication_method(contextid=1, authmethodname='formBasedAuthentication',
												 authmethodconfigparams=('loginURL=' + target + '&username=' + username
																		 + '&password=' + 'password'))
elif AuthenticationMethod == 2:
	print ''
	print 'Setting Authentication Method to httpAuthentication'

	zap.authentication.set_authentication_method(contextid=1, authmethodname='httpAuthentication',
												 authmethodconfigparams=('hostname=' + target + '&port=' + port),
												 apikey=key)
else:
	AuthenticationMethod = input(prompt='Invalid Entry...Try Again.')

print 'Adding User ' + username + ' to Context.'
zap.users.new_user(contextid=1, name=username, apikey=key)
zap.users.set_authentication_credentials(contextid=1, userid=0, authcredentialsconfigparams=('username=' + username +
																							 '&password=' + password),
										 apikey=key)
print ''
print 'Enabling user ' + username
zap.users.set_user_enabled(contextid=1, userid=0, enabled=True, apikey=key)
print ''


print 'Adding ' + target + ':' + port + ' to scope of scan.'
zap.context.include_in_context(contextname='Default Context', regex=(target + ".*"), apikey=key)

spider = zap.spider.scan_as_user(url=target, contextid=1, userid=0, apikey=key)

print 'Spider Status print'

# Prints Spider status percentage every 1 second (Not working)
while zap.spider.status < 100:
	print zap.spider.status
	time.sleep(1)

print '100 Complete'

print ''
time.sleep(5)
print 'Start Active Scanning'
zap.ascan.scan(url=target, recurse=False, inscopeonly=True, apikey=key)
while (int(zap.ascan.status)) < 100:
	print zap.ascan.status
	time.sleep(1)

print '100 Complete'
print ''
time.sleep(5)

print 'Do you want to save your session?'
Save = raw_input('y/n').lower()
if Save == 'y':
	SessionName = raw_input('Name of Session?')
	zap.core.save_session(name=SessionName, overwrite=False, apikey=key)
	print 'Session has been saved to C:\Users\{username}\OWASP ZAP\session'
	zap.core.shutdown(self, apikey=key)
elif Save == 'n':
	print "You've decided to not save your session."
	print 'Shutting Down ZAP in 10 Seconds..'
	x = 10
	while x != 0:
		print x
		threading.sleep(1)
		x -= 1
	zap.core.shutdown(self, apikey=key)