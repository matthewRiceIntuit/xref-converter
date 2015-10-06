<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">


    <xsl:output method="XML" encoding="utf-8" indent="yes"/>

    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()" />
        </xsl:copy>
    </xsl:template>

    <xsl:template match="/">
        <SISGML>
        <FORMSET FORMSETID="ALL"/>
        <FIELDSPECIFIC TYPE="Cross Reference">
        <FIELDSPECIFICELEM>
            <xsl:attribute name="FORMIDS"><xsl:value-of select="/xml/@formid"/></xsl:attribute>
            <xsl:apply-templates select="//Assign" />
        </FIELDSPECIFICELEM>
        </FIELDSPECIFIC>
        </SISGML>
    </xsl:template>


    <xsl:template match="Assign[@fed]">
        <xsl:variable name="formid" select="@FORMID"/>

        <xsl:if test="not(*[2]//ID[starts-with(@val,$formid)])">
            <FIELDS>
                <xsl:attribute name="FIELDIDS"><xsl:value-of select="@FIELDIDS"/></xsl:attribute>
                <P>The <bf><xsl:if test="ID/@type='Dollar'">$</xsl:if><VALUEREF><xsl:attribute name="ADDR"><xsl:value-of select="ID/@val"/></xsl:attribute></VALUEREF><xsl:if test="starts-with(ID/@type,'Dec')">%</xsl:if></bf> in <xsl:value-of select="ID/@desc"/> comes from Federal <xsl:apply-templates select="*[2]" /></P>
            </FIELDS>
        </xsl:if>





    </xsl:template>

    <xsl:template match="Assign[Boolean]"/>

    <xsl:template match="Assign">
        <xsl:variable name="formid" select="@FORMID"/>

        <xsl:if test="not(*[2]//ID[starts-with(@val,$formid)])">
        <FIELDS>
            <xsl:attribute name="FIELDIDS"><xsl:value-of select="@FIELDIDS"/></xsl:attribute>
            <P>The <bf><xsl:if test="ID/@type='Dollar'">$</xsl:if><VALUEREF><xsl:attribute name="ADDR"><xsl:value-of select="ID/@val"/></xsl:attribute></VALUEREF><xsl:if test="starts-with(ID/@type,'Dec')">%</xsl:if></bf> in <xsl:value-of select="ID/@desc"/> comes from  <xsl:apply-templates select="*[2]"/></P>

            <xsl:variable name="nodes" select="*[2]//ID[not(.//ArrayIndex)]"/>
            <xsl:if test="$nodes">
            <P></P>
            <P>From:</P>
            <xsl:for-each select="$nodes">
                    <GOTOLINE><xsl:attribute name="ADDR"><xsl:value-of select="@val"/><xsl:if test="../ArrayIndex">[<xsl:apply-templates select="../ArrayIndex/*"/>]</xsl:if></xsl:attribute></GOTOLINE>
            </xsl:for-each>

            </xsl:if>

           
        </FIELDS>
        </xsl:if>

    </xsl:template>




    <xsl:template match="AddSub[@val='+']"><xsl:apply-templates select="*[1]"/> added to  <xsl:apply-templates select="*[2]"/></xsl:template>
    <xsl:template match="AddSub[@val='-']"><xsl:apply-templates select="*[1]"/> subtracted from  <xsl:apply-templates select="*[2]"/></xsl:template>
    <xsl:template match="DivMul[@val='*']"><xsl:apply-templates select="*[1]"/> multiplied by <xsl:apply-templates select="*[2]"/></xsl:template>
    <xsl:template match="DivMul[@val='/']"><xsl:apply-templates select="*[1]"/> divided by <xsl:apply-templates select="*[2]"/></xsl:template>
    <xsl:template match="Call"><xsl:for-each select="./ArgList//VarRef">"<xsl:apply-templates select="." />" and </xsl:for-each></xsl:template>

    <xsl:template match="Max">the maximum of <xsl:apply-templates select="ArgList/*[1]"/> and <xsl:apply-templates select="ArgList/*[2]"/></xsl:template>

    <xsl:template match="Literal"><bf><xsl:value-of select="@val"/></bf></xsl:template>
    <xsl:template match="VarRef"> <xsl:if test="not(.//ArrayIndex)">the <bf><xsl:if test="ID/@type='Dollar'">$</xsl:if><VALUEREF><xsl:attribute name="ADDR"><xsl:value-of select="ID/@val"/></xsl:attribute></VALUEREF><xsl:if test="starts-with(ID/@type,'Dec')">%</xsl:if></bf> in </xsl:if> <xsl:value-of select="ID/@desc"/>
    </xsl:template>

    <xsl:template match="VarRef[ID[@formdesc]]">form <xsl:value-of select="ID/@formdesc" />, <xsl:value-of select="ID/@desc"/></xsl:template>

    <xsl:template match="ArgList|Parens|FunctionCall"><xsl:apply-templates /></xsl:template>

    <xsl:template match="or">
        <xsl:apply-templates select="*[1]"/>
        <CLOSEP/>

        <P><xsl:text> </xsl:text></P><xsl:text>
        </xsl:text>
        <P> -- OR -- </P><xsl:text>
        </xsl:text>
        <P><xsl:text> </xsl:text></P><xsl:text>
        </xsl:text>
        <STARTP/>
        <xsl:apply-templates select="*[2]"/>
    </xsl:template>



</xsl:stylesheet>