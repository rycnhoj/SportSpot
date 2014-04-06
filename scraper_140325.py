#!/usr/bin/python
# -*- coding: utf-8 -*-

#---------------------------
# Web Scraper
# John Cyr - If(Score)Win
# March 25, 2013
#---------------------------

import urllib
import re
import sys

from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
from PyQt4.QtWebKit import *

class Render(QWebPage):  
  def __init__(self, url):  
    self.app = QApplication(sys.argv)  
    QWebPage.__init__(self)  
    self.loadFinished.connect(self._loadFinished)  
    self.mainFrame().load(QUrl(url))  
    self.app.exec_()  
  
  def _loadFinished(self, result):  
    self.frame = self.mainFrame()  
    self.app.quit()  

def main():

    url = 'http://teamsideline.com/fsu'  
    r = Render(url)  
    html = r.frame.toHtml()  

    FULL_TEXT = unicode(html)

    allPagesTag = '"/Org/StandingsResults.aspx\?d=zcgua6CzP8c9u9\%2fsmNXw8(.+?)%3d'
    allPagesPat = re.compile(allPagesTag)
    allPagesData = list(re.findall(allPagesPat, FULL_TEXT))

    print FULL_TEXT
##    standingCSV = open('teams.csv','w')
##    scheduleCSV = open('schedule.csv','w')
    
##    for page in allPagesData: # print page
##
##        URL = "http://www.teamsideline.com/Org/StandingsResults.aspx?d=zcgua6CzP8c9u9%2fsmNXw8" + page + "%3d"
##
##        # html link reading from
##        htmlfile = urllib.urlopen(URL)
##        
##        # read site source code into python
##        htmltext = htmlfile.read()
##        
##        #Tags
##        tableCodesTag = 'd_ctl00_ct(.+?)_DateLabel">'
##        sportDivTag = '<td colspan="3" class="pageContentTitle">\r\n *(.+?)&nbsp;\|&nbsp;\r\n *(.+?)&nbsp;'
##        standingsTag = 'id="ctl00_OrgContentUnit_standingsGrid_ctl00__[0-9]*">[\r\n\t]*<td align="center" valign="top" width="25">(.+?)</td><td valign="top" width="175">(.+?)</td><td align="center" valign="top" width="25">(.+?)</td><td align="center" valign="top" width="25">(.+?)</td><td align="center" valign="top" width="25">(.+?)</td><td align="center" valign="top" width="50">(.+?)</td><td align="center" valign="top" width="25">(.+?)</td><td align="center" valign="top" width="25">(.+?)</td><td align="center" valign="top" width="50">(.+?)</td>'
##        dateLabelTag = '<span id="ctl00_OrgContentUnit_.*Grid_ctl00_ct(.+?)_DateLabel">(.+?)</span>'
##        timeLabelTag = '<span id="ctl00_OrgContentUnit_.*Grid_ctl00_ct(.+?)_TimeLabel">(.+?)</span>'
##        homeLabelTag = '<span id="ctl00_OrgContentUnit_.*Grid_ctl00_ct(.+?)_HomeLabel">(.+?)</span>'
##        awayLabelTag = '<span id="ctl00_OrgContentUnit_.*Grid_ctl00_ct(.+?)_AwayLabel">(.+?)</span>'
##        locaLabelTag = '<span id="ctl00_OrgContentUnit_.*Grid_ctl00_ct(.+?)_ScheduleLabel">(.+?)</span>'
##
##        #Patterns
##        tableCodesPat = re.compile(tableCodesTag)
##        sportDivPat = re.compile(sportDivTag)
##        standingsPat = re.compile(standingsTag)
##        dateLabelPat = re.compile(dateLabelTag)
##        timeLabelPat = re.compile(timeLabelTag)
##        homeLabelPat = re.compile(homeLabelTag)
##        awayLabelPat = re.compile(awayLabelTag)
##        locaLabelPat = re.compile(locaLabelTag)
##
##        #Data
##        tableCodesData = list(re.findall(tableCodesPat, htmltext))
##        sportDivData = list(re.findall(sportDivPat, htmltext))
##        standingsData = list(re.findall(standingsPat, htmltext))
##        dateLabelData = list(re.findall(dateLabelPat, htmltext))
##        timeLabelData = list(re.findall(timeLabelPat, htmltext))
##        homeLabelData = list(re.findall(homeLabelPat, htmltext))
##        awayLabelData = list(re.findall(awayLabelPat, htmltext))
##        locaLabelData = list(re.findall(locaLabelPat, htmltext))
##
##        standingsTable = []
##        
##        if standingsData != []:
##            for i in range(0,int(standingsData[-1][0])):
##                standingsTable.append([])
##
##            for i in standingsData:
##                standingsTable[int(i[0])-1].append(i[0])
##                standingsTable[int(i[0])-1].append(i[1])
##                standingsTable[int(i[0])-1].append(i[2])
##                standingsTable[int(i[0])-1].append(i[3])
##                standingsTable[int(i[0])-1].append(i[4])
##                standingsTable[int(i[0])-1].append(i[5])
##                standingsTable[int(i[0])-1].append(i[6])
##                standingsTable[int(i[0])-1].append(i[7])
##                standingsTable[int(i[0])-1].append(i[8])
##            
##        for team in standingsTable:
##            if(sportDivData[0][1][0:6]=='Sunday'):tempNum_1 = 9
##            if(sportDivData[0][1][0:6]=='Monday'):tempNum_1 = 9
##            if(sportDivData[0][1][0:7]=='Tuesday'):tempNum_1 = 10
##            if(sportDivData[0][1][0:9]=='Wednesday'):tempNum_1 = 12
##            if(sportDivData[0][1][0:8]=='Thursday'):tempNum_1 = 11
##            if(sportDivData[0][1][0:6]=='Friday'):tempNum_1 = 10
##            if(sportDivData[0][1][0:8]=='Saturday'):tempNum_1 = 11
##                
##            standingCSV.write("\""+team[1]+'\",\"'+sportDivData[0][1][tempNum_1:]+'\",\"'+sportDivData[0][0]+'\",\"'+team[0]+'\",\"'+team[2]+'\",\"'+team[3]+'\",\"'+team[4]+'\",\"'+team[5]+'\",\"'+team[6]+'\",\"'+team[7]+'\",\"'+team[8]+'\"\n')
##            
##        schedule = {}
##        
##        for key in tableCodesData: # Build all the keys for the dictionary schedule
##            schedule[key] = []
##
##        for i in dateLabelData:
##            if(i[1][0:3]=='<b>'):schedule[i[0]].append(i[1][3:-4])
##            else:schedule[i[0]].append(i[1])
##        for i in timeLabelData:
##            if(i[1][0:3]=='<b>'):schedule[i[0]].append(i[1][3:-4])
##            else:schedule[i[0]].append(i[1])
##        for i in homeLabelData:
##            if(i[1][0:3]=='<b>'):schedule[i[0]].append(i[1][3:-4])
##            else:schedule[i[0]].append(i[1])
##        for i in awayLabelData:
##            if(i[1][0:3]=='<b>'):schedule[i[0]].append(i[1][3:-4])
##            else:schedule[i[0]].append(i[1])
##        for i in locaLabelData:
##            if(i[1][0:3]=='<b>'):schedule[i[0]].append(i[1][3:-4])
##            else:schedule[i[0]].append(i[1])
##
##        schedule = sorted(schedule.items(), key = lambda t:t[0])
##        
##        scheduleCSV.write('\nDate,Time,Home,Away,Location\n')
##
##        for game in schedule:
##            for i in game[1]:
##                
##                scheduleCSV.write(i) # Prints schedule
##                
##                if(i != game[1][-1]):
##                    scheduleCSV.write(',')
##            scheduleCSV.write('\n')
##
##    print "END"

if __name__ == '__main__':
    main()
