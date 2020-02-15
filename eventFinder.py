#import urllib2
#reading from nycgovparks
#using python2
#nycparks = urllib2.urlopen('https://www.nycgovparks.org/events/volunteer')
#nycparks.read
#print(nycparks)

#using python3
import urllib.request, urllib.error
import urllib.robotparser as robot



def canifetch(URL):
    reader = robot.RobotFileParser()
    reader.set_url(URL + '/robots.txt')
    reader.read()
    can_fetchnycparks = reader.can_fetch("*", URL)
    return(can_fetchnycparks)


print()
print()
print()
urllib.request.urlcleanup()

hold = canifetch('https://www.nycgovparks.org')
print(hold)
if hold:#testing if we are allowed to robo request the nycgovparks website

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
        if not Value:
            raise ValueError('seperator not found in: ' + str(myUrl))


    def myPart(throwisleft, seperator):
        #print(myUrl)
        global nycparks
        if throwisleft:
            if seperator in nycparks:
                throw, throw, nycparks = nycparks.partition(seperator) #if true get rid of the left side
                return True
            else:
                return False
        if not throwisleft:
            if seperator in nycparks:
                nycparks, throw, throw = nycparks.partition(seperator)
                return True
            else:
                return False

    def myPart(throwisleft, seperator, string):
        #print(myUrl)
        x = string
        if throwisleft:
            if seperator in x:
                throw, throw, x = x.partition(seperator) #if true get rid of the left side
                return x
            else:
                raise ValueError('seperator not found in: ' + str(myUrl))

        if not throwisleft:
            if seperator in x:
                x, throw, throw = x.partition(seperator)
                return x
            else:
                raise ValueError('seperator not found in: ' + str(myUrl))


    #triming the total amount of source code to make the search functions faster
    nycparks = myPart(True, '</h2><div id="catpage_events_list">', nycparks)
    nycparks = myPart(False, '<div class="cleardiv"></div>', nycparks)

    print("------ starting finding events from " + str(myUrl) + '-------')
    #print(nycparks)
    #global myUrl

    def combinedStrip(subject):
        x = subject
        while x.startswith(('\"',"\'", " ")):
            #print(x)
            x = x.replace("\'", '')
            x = x.replace('\"', '')
            x = x.strip()
        return(x)

    EventDates = []
    # from urllib.parse import urlsplit, urlunsplit
    # myBaseUrl = urlsplit(myUrl)
    # myBaseUrl

    myBaseUrl = myUrl[0 : myUrl.rindex('/')]
    myBaseUrl = myBaseUrl[0 : myBaseUrl.rindex('/')]

    while '<h2 id=' in nycparks: #while we can still find another event date
        nycparks = myPart(True, '<h2 id=', nycparks)
        save, throw, nycparks = nycparks.partition('class="clearleft">')
        save = combinedStrip(save)
        #print(date)
        EventDates.append([save])#event date added to database

        #get the link for event details
        nycparks = myPart(True, '<a href=', nycparks)
        save, throw, nycparks = nycparks.partition('>')
        save = combinedStrip(save)
        save = myBaseUrl + save
        eventWebsiteLink = save
        EventDates[(len(EventDates) - 1)].append(save)

        #get the name of the events
        save, throw, nycparks = nycparks.partition('</a>')
        save = combinedStrip(save)
        EventDates[(len(EventDates) - 1)].append(save)

            #scan the event website
        #eventWebsite = urllib.request.urlopen(eventWebsiteLink).read().decode()
        #print(eventWebsite)

        #get starttime of event
            #CaseError(myPart(True, '<p><strong>'))
        #get blurb
            #CaseError(myPart(True, '<div itemprop="description" class="description">'))
        #get note

        #get the location of the event

        #get the coords of the events

        #get the name of the coordinator

        #get the email of the coordinator


    print('all event dates:')
    print(EventDates)
    print(len(EventDates))
    print(myBaseUrl)
    for i in EventDates:
        print(i)
    print(EventDates[0])
    #print(combinedStrip(' "this is a test " '))


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
