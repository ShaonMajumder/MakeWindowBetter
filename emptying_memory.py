import winshell
import ctypes, sys
import os

def is_winapp_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_with_UAC_permission(func):
	if is_winapp_admin():
	    # Code of your program here
	    func()
	else:
	    # Re-run the program with admin rights
	    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

def empty_recycle_bin():
	winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)

def main():
	temp_link = 'C:\\Windows\\Temp'
	percent_temp_link = 'C:\\Users\\'+os.getlogin()+'\\AppData\\Local\\Temp'
	prefetch_link = 'C:\\Windows\\Prefetch'

	try:
		empty_recycle_bin()
	except:
		pass

	os.system("explorer "+temp_link)
	os.system("explorer "+percent_temp_link)
	os.system("explorer "+prefetch_link)



run_with_UAC_permission(main)