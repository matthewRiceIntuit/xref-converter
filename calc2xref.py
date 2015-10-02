import sys
import argparse
import lxml.etree as etree
import re
from subprocess import check_output
from antlr4.InputStream import InputStream
import json

from util import pretty_print, xslt
from antrl_helper import antrl_parse, tree2xml
from xml_helper import resolve_vars, fix_self_referencing_assigns, create_or_blocks, set_pritool_descriptions, remove_duplicate_gotolines
from preprocess_helper import preprocess_calc_file
from converter_helper import process_converter


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('--pref', action='store', dest='pref_file',
                        help='The preferences file to use.',
                        required=False,
                        default='calc2xref.pref')

    parser.add_argument("--debug", help="Show parsing steps", default=False)
    arg = parser.parse_args()
    debug = arg.debug
    print "\n....Loading preferences from: %s" %  arg.pref_file
    with open(arg.pref_file) as settings_file:
        settings = json.load(settings_file)
    print "\n\n....Settings:"
    print json.dumps(settings,indent=4)
    print "\n\n"


    preprocessed = preprocess_calc_file(settings['calc_filename'], debug=debug, cl_path=settings['cl_path'])

    print "\n\n\n"

    input_stream = InputStream(preprocessed)

    tree = antrl_parse(input_stream, debug)

    root = tree2xml(tree)

    if debug:
        print "##ParseTreeWalker##"
        pretty_print(root)

    #process_converter(settings['cvt_filename'], form_xml=root, debug=debug, cl_path=settings['cl_path'])

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

    set_pritool_descriptions(root, pritool_path=settings['formset_dir'], fed_pritool_path=settings['fedformset_dir'])

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

    if settings['output_filename']:
        with open(settings['output_filename'], 'w') as f:
            f.write(text)
    else:
        print text





