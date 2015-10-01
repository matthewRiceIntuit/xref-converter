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
from converter_helper import process_converter


if __name__ == '__main__':


    parser = argparse.ArgumentParser()

    parser.add_argument('--formpath', action='store', dest='formset_dir',
                        help='The directory of a compiled formset (in order to pull Primary Tool Ids)',
                        required=True)
    parser.add_argument('--fedformpath', action='store', dest='fedformset_dir',
                        help='The directory of the federal compiled formset (in order to pull Primary Tool Ids)',
    )

    parser.add_argument('--calcfile', action='store', dest='calc_filename',
                        help='The calc file (.clc) to be converted',
                        required=True)
    parser.add_argument('--cvtfile', action='store', dest='cvt_filename',
                        help='Filename for converter file (.cvt)')

    parser.add_argument('--outfile', action='store', dest='output_filename',
                        help='Filename for output of xref')
    parser.add_argument('--clpath', action='store', dest='cl_path',
                        help='Path to cl.exe.  Usually in c:\Dev\TY15\tools')

    parser.add_argument("--debug", help="Show parsing steps", default=False)
    arg = parser.parse_args()
    debug = arg.debug

    preprocessed = preprocess_calc_file(arg.calc_filename, debug=arg.debug, cl_path=arg.cl_path)

    print "\n\n\n"
    input_stream = InputStream(preprocessed)

    tree = antrl_parse(input_stream, debug)

    root = tree2xml(tree)

    if debug:
        print "##ParseTreeWalker##"
        pretty_print(root)

    process_converter(arg.cvt_filename, form_xml=root, debug=arg.debug, cl_path=arg.cl_path)

    resolve_vars(root, use_tke=False)
    if debug:
        print "##ParseTreeWalker##"
        pretty_print(root)

    fix_self_referencing_assigns(root)

    root = xslt(root, 'tps2xref.xsl')
    if debug:
        print "## tps2xref.xsl ##"
        text = pretty_print(root)

    create_or_blocks(root)

    set_pritool_descriptions(root, pritool_path=arg.formset_dir, fed_pritool_path=arg.fedformset_dir)

    if debug:
        print "## tweaks ###"
        text = pretty_print(root)

    root = xslt(root, 'tps2xref2.xsl')
    if debug:
        print "## tps2xref2.xsl ###"
        text = pretty_print(root)

    remove_duplicate_gotolines(root)

    text = etree.tostring(root, pretty_print=True)

    # HACK: final cleanup
    text = text.replace("<P/>", "<P></P>").replace("and </P>", "</P>").replace("<STARTP/>", "<P>").replace("<CLOSEP/>", "</P>\n")

    if arg.output_filename:
        with open(arg.output_filename, 'w') as f:
            f.write(text)
    else:
        print text





