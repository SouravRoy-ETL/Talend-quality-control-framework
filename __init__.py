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
print("\033[1;32;40m\n")
beep(500, 150)
print("""##############################################################################
                            TALEND CODE QUALITY TOOL KIT
                     Framework Created with - Python & Talend Open Studio
                   License - Open Source Toolkit (Requires No Specific Licensing)
                           
                               Authors - Sourav Roy
##############################################################################
""")
print("\033[1;37;40m")
print("[Start]: Start TALEND CODE VALIDATION TOOLKIT")
print("[Info]: Reading Settings from Quality_Checker.csv file")
print("\033[1;31;40m")
print("""
[Warn]: The Script Demands Human Interaction 
""")