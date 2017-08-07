#!/bin/python

"""
The code converts json files to cwl files.
"""

import json
import os
from helper_functions import *
from cwl_generator import cwl_generator

def make_cwl(GATK_json, cwl_dir, cmd_line_options):
    """
    Make a cwl file with a given GATK json file in the cwl directory
    """

    skeleton_cwl = {'id': GATK_json['name'],
           'cwlVersion': 'v1.0',
           'baseCommand': ['java','-jar','/gatk/GenomeAnalysisTK.jar'],
           'class': 'CommandLineTool',
           'requirements': [{"class": "ShellCommandRequirement"},
                            {"class": "InlineJavascriptRequirement",
                            "expressionLib": [
                                "function getFileArgs(f, a){if(a == undefined){return ' ' + f}else{return ':' + a + ' ' + f}}" # Allows you to add annotations
                                # TODO: make this more readable
                            ]},
                            {"dockerPull": "gatk:latest", "class": "DockerRequirement"}]}

    # Create and write the cwl file
    fname = GATK_json['name'] + '.cwl'
    f = open(os.path.join(cwl_dir, fname), 'a')

    cwl_generator(
        GATK_json,
        skeleton_cwl,
        cmd_line_options
    )
    f.write(json.dumps(skeleton_cwl, indent=4, sort_keys=False))  # write the file
    f.close()