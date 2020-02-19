#format of the event element:
#[[date][website its from][name][linktoaddtogooglecalender][starttime]
#[endtime][description][lat][long][locationname][price][organizername]
#[phonenumber][email]]

def allevents():
    events = []
    events.append(eventsfromnycparks())
    #more scraping programs
    return(events)

def eventsfromnycparks():
    import urllib.request, urllib.error
    import urllib.robotparser as robot
    from codecs import decode
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
    activeURL = ""
    EventDates = []
    hold = canifetch('https://www.nycgovparks.org')
    print(hold)
    if hold:#testing if we are allowed to robo request the nycgovparks website
        activeURL
        #reading from nycgovparks
        #nycparkweb = urllib.request.URLopener('https://www.nycgovparks.org/events/volunteer')
        myUrl = 'https://www.nycgovparks.org/events/volunteer'
        #nycgovparks_read , headers = urllib.request.urlretrieve(myUrl)
        # html

        nycparks = urllib.request.urlopen('https://www.nycgovparks.org/events/volunteer').read()
        nycparks = nycparks.decode()
        #print(nycparks)


        def myPart(throwisleft, seperator, string, activeURL = activeURL):
            #print(myUrl)
            x = string
            if throwisleft:
                if seperator in x:
                    throw, throw, x = x.partition(seperator) #if true get rid of the left side
                    return x
                else:
                    raise ValueError('seperator not found in: ' + str(activeURL))

            if not throwisleft:
                if seperator in x:
                    x, throw, throw = x.partition(seperator)
                    return x
                else:
                    raise ValueError('seperator not found in: ' + str(activeURL))


        #triming the total amount of source code to make the search functions faster
        nycparks = myPart(True, '</h2><div id="catpage_events_list">', nycparks)
        nycparks = myPart(False, '<div class="cleardiv"></div>', nycparks)

        print("------ starting finding events from " + str(myUrl) + '-------')
        activeURL = myUrl
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
        def betweenthetag(seperator, string, removefront=""):
            x = string
            x = myPart(True, seperator + removefront + '>', x)
            between, throw, x = x.partition('</' + seperator + '>')
            return(between, x)

        def addEventDetail(detail, EventDates = EventDates):
            EventDates[(len(EventDates) - 1)].append(detail)


        # from urllib.parse import urlsplit, urlunsplit
        # myBaseUrl = urlsplit(myUrl)
        # myBaseUrl

        myBaseUrl = myUrl[0 : myUrl.rindex('/')]
        myBaseUrl = myBaseUrl[0 : myBaseUrl.rindex('/')]

        while '<h2 id=' in nycparks: #while we can still find another event date
            activeURL = myUrl
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
            eventWebsite = urllib.request.urlopen(eventWebsiteLink).read()
            eventWebsite = eventWebsite.decode()
            print(eventWebsiteLink)
            activeURL = eventWebsiteLink
            #print(eventWebsite)

            eventWebsite = myPart(True, 'Yahoo! Calendar</a></li><li>', eventWebsite) #getting to the specific a href tag

            #get link to add event to google calender
            save = ""
            if '<a href=' in eventWebsite:
                eventWebsite = myPart(True, '<a href=', eventWebsite)
                save, throw, eventWebsite = eventWebsite.partition('>')
                save = combinedStrip(save)
            EventDates[(len(EventDates) - 1)].append(save)

            #get starttime of event
            #print(eventWebsite)

            eventWebsite = myPart(True, '</p><p>', eventWebsite)

            save = ""
            if 'strong' in eventWebsite:
                save, eventWebsite = betweenthetag('strong', eventWebsite)
                #print(save)
                EventDates[(len(EventDates) - 1)].append(save)
                #get endtime of event
                save, eventWebsite = betweenthetag('strong', eventWebsite)
                #print(save)
            EventDates[(len(EventDates) - 1)].append(save)

            #get blurb
            eventWebsite = myPart(True, '<div itemprop="description" class="description">', eventWebsite)
            save = ""
            eventWebsite = eventWebsite.lstrip()
            #print(eventWebsite[0:3])
            while eventWebsite[0:3] == "<p>":
                hold, eventWebsite = betweenthetag('p', eventWebsite)
                save = save + hold
                eventWebsite = eventWebsite.lstrip()
                #eventWebsite = eventWebsite.lstrip('\r\n')
            addEventDetail(save)

            #get the location of the event + get the coords of the events
            lat = ""
            longitude = ""
            address = ""
            if 'strong' in eventWebsite:
                eventWebsite = myPart(True, '<span class="map_locations" id=', eventWebsite)
                save, throw, eventWebsite = eventWebsite.partition('>')
                save = combinedStrip(save)
                lat, longitude, address = save.split("__", 2)
            addEventDetail(lat) #coord + location // fix tmr
            addEventDetail(longitude)
            addEventDetail(address)

            eventWebsite = myPart(True, '<h3>Cost</h3>', eventWebsite)

            #get cost of event, should be 0 but u never know :P
            save = ""
            if '<p>' in eventWebsite:
                save, eventWebsite = betweenthetag('p', eventWebsite)
                addEventDetail(save)
                #get the name of the coordinator
                save, eventWebsite = betweenthetag('p', eventWebsite)
            addEventDetail(save)

            #get the phone number of the coordinator
            save = ""
            if 'Contact Number' in eventWebsite:
                save, eventWebsite = betweenthetag('p', eventWebsite)
            addEventDetail(save)
            #print(eventWebsite)
            #get the emaillink of the coordinator
            save = ""
            if 'Contact Email' in eventWebsite:
                #print(eventWebsite)
                eventWebsite = myPart(True, '<a href=', eventWebsite)
                save, throw, eventWebsite = eventWebsite.partition('>')
                save = combinedStrip(save)
                save = save.lstrip('mailto:')
                save = save.replace("&#x", "")
                save = save.replace(";","")
                save = save.replace('%', "")
                print(save)
                save = decode(decode(save, "hex"), 'ascii')
                addEventDetail(save)
            else:
                addEventDetail(save)
            #get email of coordinator


        #print('all event dates:')
        #print(EventDates)
        return(EventDates)

        #print(len(EventDates))
print(allevents())
#
