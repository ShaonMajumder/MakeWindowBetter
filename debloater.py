import subprocess as Popen
import subprocess as sp
from utility import *
import ctypes, sys
import os
import shaonutil


def is_winapp_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def get_UAC_permission():
	if is_winapp_admin():
	    # Code of your program here
	    pass
	else:
	    # Re-run the program with admin rights
	    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)


get_UAC_permission()

filename = 'config.ini'
config = read_configuration_ini(filename)

debloater_url = config['urls']['bloater_power_shell_script']
debloating_meta_command = config['urls']['debloating_command']
debloating_command = debloating_meta_command.replace('<debloater_url>',debloater_url)

#windowuser_name = config['urls']['username_folder_name']
windowuser_name = os.getlogin()
user_startup_folder_link = config['urls']['startup_url'].replace('<username_folder_name>',windowuser_name)
common_startup_folder_link = config['urls']['common_startup_url']

os.system(debloating_command)




