#!/usr/bin/env python

__author__ = "Stefan Lieberth"
__copyright__ = "Copyright 2016"
__credits__ = [""]
__license__ = "MIT/Expat"
__version__ = "0.6"
__maintainer__ = "Stefan Lieberth"
__email__ = "stefan@lieberth.net"
__status__ = "beta"


import io
from lxml import etree
import sys

def parse (*args,**kwargs):
    return juniperXmlParser._parse(*args,**kwargs)

class juniperXmlParser:

    def __init__(self):
        pass

    @classmethod
    def _parse(self,xmlCliOutput):

        def _extractXmlContentFromCliReply(cliOutput): 
            myLines = cliOutput.split("\n")  
            startLine = 0
            endLine = 0
            thisLine = 0
            for myLine in myLines:
                if "<rpc-reply" in myLine: startLine = thisLine                    
                if '</rpc-reply' in myLine: endLine = thisLine   
                thisLine += 1
            return "\n".join (myLines[startLine:endLine+1]) 

        def _removeNamespaces(xmlTree):
            xslt='''<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
            <xsl:output method="xml" indent="no"/>

            <xsl:template match="/|comment()|processing-instruction()">
                <xsl:copy>
                  <xsl:apply-templates/>
                </xsl:copy>
            </xsl:template>

            <xsl:template match="*">
                <xsl:element name="{local-name()}">
                  <xsl:apply-templates select="@*|node()"/>
                </xsl:element>
            </xsl:template>

            <xsl:template match="@*">
                <xsl:attribute name="{local-name()}">
                  <xsl:value-of select="."/>
                </xsl:attribute>
            </xsl:template>
            </xsl:stylesheet>
            '''

            xslt_doc=etree.parse(io.BytesIO(xslt.encode()))
            transform=etree.XSLT(xslt_doc)
            returnTree=transform(xmlTree)
            return returnTree

        cleanXmlString = _extractXmlContentFromCliReply(xmlCliOutput)
        etreeWithNamespaces = etree.XML(cleanXmlString)
        self.etreeWithOutNamespaces = _removeNamespaces(etreeWithNamespaces)
        return self.etreeWithOutNamespaces

