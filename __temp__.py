import pandas as pd
import numpy as np
import sys
import os
import time, glob
import json
import subprocess
try:
    import winsound
except ImportError:
    import os
    if sys.platform == "darwin":
        def beep(freq, duration):
            # brew install SoX --> install SOund eXchange universal sound sample translator on mac
            os.system(f"play -n synth {duration/1000} sin {freq} >/dev/null 2>&1")
    else:
        def beep(freq, duration):
            # apt-get install beep  --> install beep package on linux distros before running
            os.system("beep -f %s -l %s" % (freq, duration))
else:
    def beep(freq, duration):
        winsound.Beep(freq, duration)
import shutil
import ctypes

choice = input("Enter q/Q to quit, or press Return to continue - ")
if choice.lower() == "q":
    sys.exit()
else:
    print("\033[1;37;40m")
    print("[Start]: Start of Processing")
    contextFilePath = open(r"config/Configurations.csv")
    read_as_lines = contextFilePath.readlines()
    for iterations in read_as_lines:
        if 'Path_of_Configuration_File' in iterations:
            ContextFileName=iterations.split('=')
            ContextFile=ContextFileName[1]
            ContextFile=str(ContextFile)
            ContextFile=ContextFile.replace("\\","/")
            ContextFile2=ContextFile.replace("C:","C\\:")
            print(ContextFile2)
    ##########################################################
    #           REPLACE CONTEXT IN TALEND CONFIG             #
    ##########################################################
    reading_file = open(r"src/__pipe1__/talend_code_quality_toolkit/data_quality/talend_code_quality_toolkit_0_1/contexts/Default.properties")#Change
    new_file_content = ""
    for line in reading_file:
        stripped_line = line.strip()
        new_line = stripped_line.replace("Path_of_Configuration_File=", "Path_of_Configuration_File={}".format(ContextFile2))
        new_file_content += new_line +"\n"
    reading_file.close()
    writing_file = open(r"src/__pipe1__/talend_code_quality_toolkit/data_quality/talend_code_quality_toolkit_0_1/contexts/Default.properties", "w")#Change
    writing_file.write(new_file_content)
    writing_file.close()
    ##########################################################
    #         CALLING TALEND JOB TO CREATE METADATA          #
    ##########################################################
    if sys.platform == "darwin":
        subprocess.run([r'src\__pipe1__\talend_code_quality_toolkit\talend_code_quality_toolkit_run.sh'], shell=True)
    elif sys.platform == "Linux":
        subprocess.run([r'src\__pipe1__\talend_code_quality_toolkit\talend_code_quality_toolkit_run.sh'], shell=True)
    else:
        subprocess.call([r'src\__pipe1__\talend_code_quality_toolkit\talend_code_quality_toolkit_run.bat'])
    ##########################################################
    #         MERGING CSV FILES INTO A RESULTANT FILE        #
    ##########################################################
    extension = 'csv'
    all_filenames = [i for i in glob.glob('temp/final/*.{}'.format(extension))]
    combined_csv = pd.concat([pd.read_csv(f, sep='|') for f in all_filenames])
    combined_csv.to_csv(r"OUT/All_Merged_Py.csv", index=False, sep='|', encoding='utf-8-sig')
    def isAdmin():
        try:
            is_admin = (os.getuid() == 0)
        except AttributeError:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        return is_admin
    if(isAdmin()):
        print("\033[1;31;40m")
        beep(1000, 2000)
        print("[Warn]: You are Running this application as an Administrator. \nThe Developer of this application does not intend to run this application as Administrator")
        print("\033[1;37;40m")
    else:
        print("\033[1;32;40m")
        print("[Success]: End of Processing")
        print("\033[1;37;40m")