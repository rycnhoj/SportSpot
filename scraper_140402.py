#!/usr/bin/python
# -*- coding: utf-8 -*-

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
 
def getHtml(str_url):
    r_html = Render(str_url)  
    html = r_html.frame.toHtml()
 
    return html

str_url = 'http://http://teamsideline.com/fsu'
 
str_html = getHtml(str_url)
 
print str_html
