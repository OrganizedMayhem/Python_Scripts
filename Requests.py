import requests
import httplib

url = "aspect.com"
response = requests.get('http://www.' + url)

# Apache #
Server = response.headers['Server']
# Application/AVersion are used in final.
# BlackHole is overwritten.

Application, BlackHole = Server.split('/')
print ''
if Application == 'Apache':
    print 'Application is ' + Application
    AVersion, BlackHole = BlackHole.split(' ')
    BlackHole = ''
    print 'Version is ' + AVersion

    # PoweredBy is Used to parse out the 'X-Powered-By' Header
    PoweredBy = response.headers['X-Powered-By']

    # Displays
    Language, LVersion = PoweredBy.split('/')
    FinalVersion, BlackHole = LVersion.split('-')
    BlackHole = ''
    print 'Language used is ' + Language
    print 'Version is ' + FinalVersion

elif Application == 'Microsoft-IIS':
    print 'Application is ' + Application
    print 'IIS Version ' + BlackHole
    print ''

    #PoweredBy is Used to parse out the 'X-Powered-By' Header
    PoweredBy = response.headers['X-Powered-By']
    print PoweredBy
    AspNetVersion = response.headers['X-AspNet-Version']
    print AspNetVersion

