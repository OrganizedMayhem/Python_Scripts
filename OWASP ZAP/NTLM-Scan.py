import zapv2, time

zap = ZAPv2()

print "Starting ZAP..."

# This is the API Key (Change if needed)
key = ''

# Enable Auto Re-Authentication
zap.auth.auto_reauth_on(apikey=key)

print ''

# Get URL to scan
print 'Must include http(s):// in target URL'
target = raw_input('URL to Scan? ')

# Get Port Number
port = int(input('Port? '))

# Request Username and Password for Application login
username = raw_input('Username? ').lower()
password = raw_input('Password? ')

# Set's authentication Method
zap.authentication.set_authentication_method(contextid=1, authmethodname='httpAuthentication', authmethodconfigparams=('hostname=' + target + '&port=' + port), apikey=key)

# Adding User to Context
print 'Adding User ' + username + ' to Context.'
zap.users.new_user(contextid=1, name=username, apikey=key)
zap.users.set_authentication_credentials(contextid=1, userid=0, authcredentialsconfigparams=('username=' + username +
																							 '&password=' + password),
										 apikey=key)

print ''
print 'Enabling user ' + username
zap.users.set_user_enabled(contextid=1, userid=0, enabled=True, apikey=key)
print ''

# Adding Target to Scope of Scan
print 'Adding ' + target + ':' + port + ' to scope of scan.'
zap.context.include_in_context(contextname='Default Context', regex=(target + ".*"), apikey=key)

# Start's Spidering BaseUrl as User
spider = zap.spider.scan_as_user(url=target, contextid=1, userid=0, apikey=key)

print 'Spider Status (%)'

while spider < 100:
    print spider + '%'
    time.sleep(1)

print ''
print '100%'

time.sleep(5)

# Set Scan Policy
zap.ascan.set_enabled_policies(ids='', apikey=key)

# Start Active scan

ActiveScan = zap.ascan.scan(url=target, recurse=False, inscopeonly=True, apikey=key)
ActiveScanStatus = zap.ascan.status(apikey=key)

while ActiveScanStatus. < 100:
    print ActiveScanStatus + '%'
    time.sleep(1)

print '100% Complete'

# Report Alerts in a table (PrettyTable)




