import requests
import httplib

url = ""
response = requests.get('http://www.' + url)

# Apache #
Server = response.headers['Server']
Application, Version = Server.split('/')
print ''
print 'Application is ' + Application
AVersion, BlackHole = Version.split(' ')
BlackHole = ''
print 'Version is ' + AVersion

PoweredBy = response.headers['X-Powered-By']
Language, LVersion = PoweredBy.split('/')
FinalVersion, OperatingSystem = LVersion.split('-')
print 'Programming Language used is ' + Language
print 'Version is ' + FinalVersion




