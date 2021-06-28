# Talend-quality-control-framework
> Talend Quality Control Framework is an automated code analysis tool to motivate Talend developers and ETL Testers to design Talend Projects that adheres to a Strong and Solid coding standard. It automates the process of checking Talend components for validation rules such as if CHECK_PROXY, TRIM_ALL has been implemented or not? and spare us humans from this boring (but important) task. Talend Quality Control Framework is ideal for Talend projects that want to enforce coding standards.
> This is a Universal Plug & Play Testing Framework, just configure and Play.

## Installing 
Talend Validation Toolkit can be used for multiple purposes and methods such as;
* __As an Automated Test Suite__ (module: talend-quality-framework-unix)
* __As a Standalone Python Application__ (module: talend-quality-framework)
* __TODO: Include Plugin which will be configured for remote SVN Talend Project__

### As an Automated Test Suit
````
For Unix Users (CronTab) -
01 04 1 1 1 /usr/bin/somedirectory/main.py

For Windows Users -
Step 1 : start C:\Users\userX\Python.exe C:\Users\userX\Desktop\Workspace\TALEND_CODE_Q_SRV\main.py
Step 2 : Open the Task Scheduler and click on the Task Scheduler Library to see the current tasks that are executed. Click on the Create Task option.
Step 3 : In the General tab, put the name of your new task and click on the option Run whether user is logged on or not, check the option Run with highest privileges and make sure to setup the appropriate version of you OS (in my case I picked Windows 7, Windows Server 2008 R2.
Step 4: In the Actions tab, click on the New button and type in the following:

In Program/Scripts you need to look up for the Powershell path that the Task Scheduler will invoke to run the .bat file. In my case, my Powershell path was: C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe

In Add arguments (optional) you need to type the path of the file that will be executed by Powershell. In my case, the path was:

C:\Users\userX\Desktop\run_the_bat_file.bat

In Start in (optional) you need to type the path of the file but without the name of the .bat file, that is:

C:\Users\userX\Desktop\

Step 5: Click on the Triggers tab and select how often you want to execute this task and Finally Click on Triggers Tab
````

### As a Python Application
Please download and install `Python 3.8.0 or Above` from https://python.org . The desktop python application allows developers to locate Talend project clonned locally and validate them. 

![image](https://user-images.githubusercontent.com/85476817/123683074-6ace4200-d869-11eb-909f-62bf246fbb7b.png)

## Development Guide
### Prerequisites
* Python (Version 3.7+)
* Java

### Project Structure and Sub Modules
Talend Validation Toolkit has serveral maven modules for the parent project. The project hierarchy as follows.
````
| Talend-quality-control
|----| config
|----| OUT
|----| src
````
### Module: Talend-quality-control
talend-validation-util is the main artifact of the talend-validation-toolkit which consists of validation logics and validation configurations. Validation configurations are defined in CSV format in resource directory (config/Configurations.csv). Validation rules(config/Rulebook.csv) CSV template as follows;

##### Rule Book Template:
````
Name,Rule
tFileInputDelimited,CSV_OPTION
tFileInputDelimited,TRIMALL
tFileInputDelimited,HEADER
tFileInputDelimited,ENCODING:ENCODING_TYPE
tFileOutputDelimited,CSV_OPTION
tFileOutputDelimited,INCLUDEHEADER
tFileOutputDelimited,ENCODING:ENCODING_TYPE
tFileOutputDelimited,FILE_EXIST_EXCEPTION
tFileList,INCLUDSUBDIR
tRunJob,TRANSMIT_WHOLE_CONTEXT
tRunJob,DIE_ON_CHILD_ERROR
tFileInputExcel,VERSION_2007
tFileInputExcel,HEADER
tFileInputExcel,FIRST_COLUMN
tFileInputExcel,TRIMALL
tFileInputExcel,ENCODING:ENCODING_TYPE
tFileInputExcel,STOPREAD_ON_EMPTYROW
tFileOutputExcel,HEADER
tFileOutputExcel,ENCODING:ENCODING_TYPE
tFileOutputDelimited,SPLIT_EVERY
````
Note: Once a validattion rule is defined as a CSV Rule Book, it should automatically add to the `Validation Rules` which is available in the resource directory. 

##### Available Validators
There are NO BOUNDARIES on validation rules that can be defined in this projec;
* Name of Component _(Rule: Checked TRIM_ALL or Not)
For Example:
````tFileInputDelimited,TRIMALL````

### How to Run this Project/Build/ Run
Use following commands/Instructions to build the project from the project root. 

Step 1 - There shall be two files present in the Project Directory/Config/
![image](https://user-images.githubusercontent.com/85476817/123685116-f5b03c00-d86b-11eb-99f0-e82cdbb389ae.png)

Step 2 - From the above, Open the file Configurations.csv, Then, Change the below parameters according to your Systems Path
![image](https://user-images.githubusercontent.com/85476817/123685321-2db77f00-d86c-11eb-8573-1d4b8eb33e50.png)

Step 3 - After this, Open Rulebook.csv. Add any N no. of Test Cases to test the Code Quality

Step 4 - Install Pandas, Numpy

Step 5 - Run the Script
````
python main.py
````


### Authors
* Sourav Roy (souravroy7864@gmail.com)
