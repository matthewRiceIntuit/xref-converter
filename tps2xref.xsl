<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">


    <xsl:output method="xml" encoding="utf-8" indent="yes"/>

    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()" />
        </xsl:copy>
    </xsl:template>

    <xsl:template match="/">
        <xml>
            <xsl:attribute name="formid"><xsl:value-of select="CALC/FORMSET/FORM/@val"/></xsl:attribute>
            <xsl:apply-templates select="//Assign[not(starts-with(ID/@val,'#'))]"/>
        </xml>
    </xsl:template>


    <xsl:template match="Assign">

        <xsl:copy>
            <xsl:apply-templates select="@*|node()" />
        </xsl:copy>
    </xsl:template>

    <xsl:template match="ID[starts-with(@val,'#')]">
        <xsl:variable name="id" select="@val"/>
        <xsl:for-each select="//Assign[ID/@val=$id]">
             <xsl:apply-templates select="*[2]" />
        </xsl:for-each>
    </xsl:template>







</xsl:stylesheet>