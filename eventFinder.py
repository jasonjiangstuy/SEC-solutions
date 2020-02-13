#import urllib2
#reading from nycgovparks
#using python2
#nycparks = urllib2.urlopen('https://www.nycgovparks.org/events/volunteer')
#nycparks.read
#print(nycparks)

#using python3
import urllib.request, urllib.error
import urllib.robotparser as robot

#testing if we are allowed to robo request the nycgovparks website
reader = robot.RobotFileParser()
reader.set_url('https://www.nycgovparks.org/robots.txt')
reader.read()
can_fetchnycparks = reader.can_fetch("*", "https://www.nycgovparks.org")
print(can_fetchnycparks)

print()
print()
print()
urllib.request.urlcleanup()
if can_fetchnycparks:
#reading from nycgovparks
    #nycparkweb = urllib.request.URLopener('https://www.nycgovparks.org/events/volunteer')

    #planning purposes
    myUrl = 'https://www.nycgovparks.org/events/volunteer'
    #nycgovparks_read , headers = urllib.request.urlretrieve(myUrl)
    # html

    nycparks = urllib.request.urlopen('https://www.nycgovparks.org/events/volunteer').read()
    nycparks = nycparks.decode()
    #print(nycparks)

    def CaseError(Value):
        if not Value[0]:
            raise ValueError(str(Value[1]) + ' not found in: ' + str(myUrl))

    def myPart(throwisleft, seperator):
        #print(myUrl)
        global nycparks
        if throwisleft:
            if seperator in nycparks:
                throw, throw, nycparks = nycparks.partition(seperator)
                return([True])
            else:
                return False, seperator
        if not throwisleft:
            if seperator in nycparks:
                nycparks, throw, throw = nycparks.partition(seperator)
                return([True])
            else:
                return False, seperator

    CaseError(myPart(True, 'Volunteer Events'))
    CaseError(myPart(False, '<div class="cleardiv"></div>'))

    print("------ starting finding events from " + str(myUrl) + '-------')
    print(nycparks)

    EventDates = []
    while '<h2' in nycparks:
        throw, throw, nycparks = nycparks.partition('Volunteer Events')



    # tagisfound = False
    # for i in nycparks:
    #     if not tagisfound:
    #         if i == "<":
    #             print('tag start found')
    #             tagisfound = True
    #
    #         #else:
    #
    #             #b
    #     #else:


    #put in temp file for coding purposes
