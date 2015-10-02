import sys
import argparse

import lxml.etree as etree
import re
from subprocess import check_output
from antlr4.InputStream import InputStream

from util import pretty_print, xslt
from antrl_helper import antrl_parse, tree2xml
from xml_helper import resolve_vars, fix_self_referencing_assigns, create_or_blocks, set_pritool_descriptions, remove_duplicate_gotolines
from preprocess_helper import preprocess_calc_file


def process_converter(filename, form_xml, debug, cl_path):
    debug = True
    if not filename:
        return None
    form = form_xml.xpath('/CALC/FORMSET/FORM/@val')[0].upper()

    preprocessed = preprocess_calc_file(filename, debug=True, cl_path=cl_path)

    input_stream = InputStream(preprocessed)
    tree = antrl_parse(input_stream, debug)
    xml = tree2xml(tree)
    if debug:
        pretty_print(xml)
    withforms = xml.xpath('//WithForms[ID[1][@val="%s"]]' % form)
    if not withforms:
        return

    withforms = withforms[0]
    fedform = withforms.xpath("ID[2]/@val")[0].upper()
    for each in withforms.xpath(".//Assign"):
        each.set('fed', '1')
        id = each.getchildren()[0]
        id.set('val', "%s.%s" % (form, id.get('val').upper()))

        for id in each.getchildren()[1].xpath('.//ID'):
            id.set('val', "%s.%s" % (fedform, id.get('val').upper()))


    #Cleanup boolean\literal assigns
    for each in withforms.xpath(".//IfStruct/Assign[Boolean|Literal]"):
        each.remove(each.getchildren()[1])
        ids = each.xpath('../*[1]//ID')
        if len(ids)>1:
            or_node = etree.SubElement(each, "or")
            for id in ids:
                or_node.append(id)
        else:
            each.append(ids[0])

    pretty_print(withforms)
    import ipdb;ipdb.set_trace()

    form_xml.append(withforms)

