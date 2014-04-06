#---------------------------
# Web Scraper
# John Cyr - If(Score)Win
# Feb 12, 2013
#---------------------------

import urllib
import re
    
def main():

    # Scrape the full site html page text file
    FULL_SITE = open('FULL_SITE.html', 'r')
    FULL_TEXT = FULL_SITE.read()
    allPagesTag = '"/Org/StandingsResults.aspx\?d=zcgua6CzP8c9u9\%2fsmNXw8(.+?)%3d'
    allPagesPat = re.compile(allPagesTag)
    allPagesData = list(re.findall(allPagesPat, FULL_TEXT))

    for page in allPagesData: # print page        

        #http://www.teamsideline.com/Org/StandingsResults.aspx?d=zcgua6CzP8c9u9%2fsmNXw8SV%2bOForSoI2tJuvAm23Sx6oGX2Mk1zfTJhERokNqUSt73jucRZHcCE%3d
        URL = "http://www.teamsideline.com/Org/StandingsResults.aspx?d=zcgua6CzP8c9u9%2fsmNXw8" + page + "%3d"

        # html link reading from
        htmlfile = urllib.urlopen(URL)
        
        # read site source code into python
        htmltext = htmlfile.read()
        
        #Tags
        tableCodesTag = 'd_ctl00_ct(.+?)_DateLabel">'
        sportDivTag = '<td colspan="3" class="pageContentTitle">\r\n *(.+?)&nbsp;\|&nbsp;\r\n *(.+?)&nbsp;'
        standingsTag = '<td align="center" valign="top" style="width:25px;">(.+?)</td><td valign="top" style="width:175px;">(.+?)</td><td align="center" valign="top" style="width:25px;">(.+?)</td><td align="center" valign="top" style="width:25px;">(.+?)</td><td align="center" valign="top" style="width:25px;">(.+?)</td><td align="center" valign="top" style="width:50px;">(.+?)</td><td align="center" valign="top" style="width:25px;">(.+?)</td><td align="center" valign="top" style="width:25px;">(.+?)</td><td align="center" valign="top" style="width:50px;">(.+?)</td>'
        dateLabelTag = '<span id="ctl00_OrgContentUnit_.*Grid_ctl00_ct(.+?)_DateLabel">(.+?)</span>'
        timeLabelTag = '<span id="ctl00_OrgContentUnit_.*Grid_ctl00_ct(.+?)_TimeLabel">(.+?)</span>'
        homeLabelTag = '<span id="ctl00_OrgContentUnit_.*Grid_ctl00_ct(.+?)_HomeLabel">(.+?)</span>'
        awayLabelTag = '<span id="ctl00_OrgContentUnit_.*Grid_ctl00_ct(.+?)_AwayLabel">(.+?)</span>'
        locaLabelTag = '<span id="ctl00_OrgContentUnit_.*Grid_ctl00_ct(.+?)_ScheduleLabel">(.+?)</span>'
                       
        #Patterns
        tableCodesPat = re.compile(tableCodesTag)
        sportDivPat = re.compile(sportDivTag)
        standingsPat = re.compile(standingsTag)
        dateLabelPat = re.compile(dateLabelTag)
        timeLabelPat = re.compile(timeLabelTag)
        homeLabelPat = re.compile(homeLabelTag)
        awayLabelPat = re.compile(awayLabelTag)
        locaLabelPat = re.compile(locaLabelTag)

        #Data
        tableCodesData = list(re.findall(tableCodesPat, htmltext))
        sportDivData = list(re.findall(sportDivPat, htmltext))
        standingsData = list(re.findall(standingsPat, htmltext))
        dateLabelData = list(re.findall(dateLabelPat, htmltext))
        timeLabelData = list(re.findall(timeLabelPat, htmltext))
        homeLabelData = list(re.findall(homeLabelPat, htmltext))
        awayLabelData = list(re.findall(awayLabelPat, htmltext))
        locaLabelData = list(re.findall(locaLabelPat, htmltext))

        schedule = {}
        
        for key in tableCodesData: # Build all the keys for the dictionary schedule
            schedule[key] = []

        for i in dateLabelData:
            schedule[i[0]].append(i[1])
        for i in timeLabelData:
            schedule[i[0]].append(i[1])
        for i in homeLabelData:
            schedule[i[0]].append(i[1])
        for i in awayLabelData:
            schedule[i[0]].append(i[1])
        for i in locaLabelData:
            schedule[i[0]].append(i[1])

        schedule = sorted(schedule.items(), key = lambda t:t[0])

        print sportDivData # Page Header

        for game in schedule:
             print game[1] 

    print "END"

if __name__ == '__main__':
    main()
