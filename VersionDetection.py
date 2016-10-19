import requests
import httplib

TargetURL = raw_input("Target URL? ")
response = requests.get(TargetURL)

# Apache #
Server = response.headers['Server']
# Application/AVersion are used in final.
# Version is overwritten.
Application, Version = Server.split('/')
print ''
if Application == 'Apache':
    print 'Application is ' + Application
    AVersion, Version = Version.split(' ')
    Version = ''
    print 'Version is ' + AVersion

    # PoweredBy is Used to parse out the 'X-Powered-By' Header
    PoweredBy = response.headers['X-Powered-By']

    # Displays
    Language, LVersion = PoweredBy.split('/')
    FinalVersion, Version = LVersion.split('-')
    Version = ''
    print 'Language used is ' + Language
    print 'Version is ' + FinalVersion

elif Application == 'Microsoft-IIS':
    print 'Application is ' + Application
    print 'IIS Version ' + Version
    print ''

    #PoweredBy is Used to parse out the 'X-Powered-By' Header
    PoweredBy = response.headers['X-Powered-By']
    print PoweredBy
    AspNetVersion = response.headers['X-AspNet-Version']
    print AspNetVersion

