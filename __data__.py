import pandas as pd
import numpy as np
import sys
import os
import time, glob
import json
import subprocess
import shutil
import ctypes
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
from datetime import datetime
read_previous_temp_file = pd.read_csv(r'OUT/All_Merged_Py.csv',sep='|',encoding='utf-8-sig')
read_previous_temp_file['Component_Name'] = read_previous_temp_file['Component_Name'].str.replace('\d+', '')
read_previous_temp_file['Component_Name'] = read_previous_temp_file['Component_Name'].str.replace('_', '')
read_rulebook = pd.read_csv(r'config/rulebook.csv',sep=',',encoding='utf-8')
date = datetime.now().strftime("%Y_%m_%d_%I_%M_%S_%p")
directory = r'OUT/Results_By_Component/{}'.format(date)
if not os.path.exists(directory):
    os.makedirs(directory)
for index, row in read_rulebook.iterrows():
    ok = read_previous_temp_file.loc[(read_previous_temp_file['Component_Name'] == row['Name']) & (read_previous_temp_file['value'] == 'true')]
    ok.drop_duplicates(keep=False,inplace=True)
    ok.to_csv(r"OUT/Results_By_Component/{}/{}_{}.csv".format(date,row['Name'],date), index=False, sep=",")
beep(500, 150)
os.remove(r'OUT/All_Merged_Py.csv')