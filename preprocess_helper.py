import sys
import re
from subprocess import check_output

def preprocess_calc_file( calc_filename, debug, cl_path ):
    with open(calc_filename) as f:
        unpreproccessed = f.read()

    print "\n\n\n"


    unpreproccessed = re.sub('\nsection\s+', '\nSECTION ', unpreproccessed, flags=re.I)
    sections = unpreproccessed.split('\nSECTION ')

    first_section = re.match("\w+", sections[1]).group()


    try:
        if not cl_path:
            cl_path='cl.exe'
        preproccessed = check_output([cl_path, '/EP', '-DPRO', '-DWIN', calc_filename],shell=True)
        preproccessed = re.sub('\n\s+\n','\n',preproccessed)
    except Exception, e:
        print "###### ERROR #####"
        print e

        if "/" not in   calc_filename:
            exit()

        with open(calc_filename.split('/')[-1]) as f:
            preproccessed = f.read()




    preproccessed = re.sub('\nsection\s+', '\nSECTION ', preproccessed, flags=re.I)
    sections = preproccessed.split('\nSECTION ')
    sections[0] = re.sub('function', '\nFUNCTION ', sections[0], flags=re.I)
    sections[0] = sections[0].split('\nFUNCTION ')[0]

    text = sections[0]

    bfound = False
    for each in sections[1:]:

        if not bfound and first_section != re.match("\w+", each).group():
            continue
        bfound = True
        text += "\n\nsection " + each

    if debug:
        print "######## PreProcessor ###########"
        print text
        print "\n\n\n\n"
        if  "/" not in   calc_filename:
            with open(calc_filename.split('\\')[-1],'w') as f:
                f.write(text)

    return text
