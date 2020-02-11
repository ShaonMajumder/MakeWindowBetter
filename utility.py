from PIL import Image,ImageDraw,ImageFont,ImageOps
from urllib.parse import unquote
from datetime import date
import sys
import codecs
import configparser
import json
import string
import re
import random
import string
import reconium
import os
import glob
import platform
import subprocess
import pprint
import gummybear

def execute_shell(cmd):
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True)
    for stdout_line in iter(popen.stdout.readline, ""):
        yield stdout_line 
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)
        
def execute_command(command):
	print("IN <", command)
	process = subprocess.Popen(command, stdin = subprocess.PIPE, stdout=subprocess.PIPE)
	output, error = process.communicate()
	output = output.decode("utf-8")
	return output
def Oldwinexecute_command(command):
	print("IN <", command)
	process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
	output, error = process.communicate()
	output = output.decode("utf-8")
	return output




def getLoc_syspath(search_object):
	if os.path.exists(search_object):
		return search_object
	else:
		for path in sys.path:
			search_path = os.path.join(path,search_object)
			if os.path.exists(search_path):
				return search_path
		return False
	
def change_dic_key(dic,old_key,new_key):
	dic[new_key] = dic.pop(old_key)
	return dic

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    for c in range(10):
        letters = letters + str(c)

    return ''.join(random.choice(letters) for i in range(stringLength))

def read_json(filename):
	with codecs.open(filename, "r", encoding="utf-8") as fp:
		data = json.load(fp)
	#Print Formatted Dictionary
	#print(json.dumps(data, indent=4))
	return data

def write_json(obj,filename):
	with codecs.open(filename, "w", encoding='utf-8') as fp:
	    json.dump(obj, fp, indent=1)




class configdom:
	"""docstrinconfigdomssName"""
	def __init__(self):
		self.configObj = configparser.ConfigParser()
		self.comment_map = ''
		self.config_filename = ''

	def __getitem__(self, item):
		return self.configObj[item]

	def read_file(self,config_file):
		self.config_filename = config_file
		self.comment_map = self.save_comments(config_file)
		return self.configObj.read_file(codecs.open(config_file, "r", "utf8"))

	def options(self,section):
		return self.configObj.options(section)

	def get(self, section, option):
		return self.configObj.get(section, option)

	def write(self,fileObj):
		self.configObj.write(fileObj)
		fileObj.close()
		self.restore_comments(self.config_filename, self.comment_map)

	def save_comments(self,config_file,comment_prefix=';'):
	    """Save index and content of comments in config file and return dictionary thereof"""
	    comment_map = {}
	    with open(config_file, 'r') as file:
	        i = 0
	        lines = file.readlines()
	        for line in lines:
	            if re.match( r'^\s*'+comment_prefix+'.*?$', line):
	                comment_map[i] = line
	            i += 1
	    
	    return comment_map

	def restore_comments(self, config_file, comment_map):
	    """Write comments to config file at their original indices"""
	    #def write_configuration_ini(configs_par,filename, f_mode='w'):
		#	with open(filename, f_mode) as configfile:    # save
		#		configs_par.write(configfile)

	    with open(config_file, 'r') as file:
	        lines = file.readlines()
	    
	    for (index, comment) in sorted(comment_map.items()):
	    	lines.insert(index, comment)
	    
	    with open(config_file, 'w') as file:
	        file.write(''.join(lines))

def read_configuration_ini(filename):
	# set comment_prefixes to a string which you will not use in the config file
	#config = configparser.ConfigParser()
	config = configdom()
	config.read_file(filename)
	#ConfigParser(comment_prefixes=';', allow_no_value=True)
	#config.read_file(codecs.open(filename, "r", "utf8"))
	return config

def read_configuration_inip(filename):
	# set comment_prefixes to a string which you will not use in the config file
	config = configparser.ConfigParser()
	#config = configdom()
	#ConfigParser(comment_prefixes=';', allow_no_value=True)
	config.read_file(codecs.open(filename, "r", "utf8"))
	#config.read_file(filename)
	return config

def read_safecase_configuration_ini(filename):
	config = CaseConfigParser()
	config.read_file(codecs.open(filename, "r", "utf8"))
	return config

def write_configuration_ini(configs_par,filename, f_mode='w'):
	with open(filename, f_mode) as configfile:    # save
		configs_par.write(configfile)

def read_file(filename):
	with codecs.open(filename, "r", encoding="utf-8") as file_reader:
		lines = file_reader.readlines()

	def filtering___(lines):
		ill_chars = ['\r','\n']
		_ = []
		for line in lines:
			for ic in ill_chars:
				line = line.replace(ic,'')
			_.append(line)
		filtered_lines = _
		return filtered_lines

	return filtering___(lines)

def write_file(filename, strs,mode="w"):
	with codecs.open(filename, mode, encoding='utf-8') as file_appender:
		file_appender.writelines(strs)






Months_List = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def td_format(td_object):
    seconds = int(td_object.total_seconds())
    periods = [
        ('year',        60*60*24*365),
        ('month',       60*60*24*30),
        ('day',         60*60*24),
        ('hour',        60*60),
        ('minute',      60),
        ('second',      1)
    ]

    strings=[]
    for period_name, period_seconds in periods:
        if seconds > period_seconds:
            period_value , seconds = divmod(seconds, period_seconds)
            has_s = 's' if period_value > 1 else ''
            strings.append("%s %s%s" % (period_value, period_name, has_s))

    return ", ".join(strings)



def nicely_print(dictionary,print=True):
	# Prints the nicely formatted dictionary
	if print: pprint.pprint(dictionary)

	# Sets 'pretty_dict_str' to 
	return pprint.pformat(dictionary)



def url_encoding_to_utf_8(url):
    url = unquote(url)
    return url


def check_valid_url(url):
	regex = re.compile(
	        r'^(?:http|ftp)s?://' # http:// or https://
	        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
	        r'localhost|' #localhost...
	        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
	        r'(?::\d+)?' # optional port
	        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

	return re.match(regex, url) is not None

def record_sessions_video(driver,fps,function_,parameters):
    rc = reconium.Recorder(driver,fps)
    rc.start()
    result = function_(*parameters)
    rc.stop()
    return result

def change_image_size_ratio(img_name,out_name,percent):
	im = Image.open(img_name)
	width, height = im.size
	Iwidth, Iheight = int(width + width*(percent/100)) , int(height + height*(percent/100))
	im = im.resize((Iwidth, Iheight), resample=Image.ANTIALIAS)
	im.save(out_name)

def draw_text(img,text,fnt_name,fnt_size):
	d = ImageDraw.Draw(img)
	fnt = ImageFont.truetype(fnt_name, fnt_size)
	d.text((0,0), text, font=fnt, fill=(0,0,0))
	del d
	return img

def merge_horizontally(images):
	widths, heights = zip(*(i.size for i in images))

	total_width = sum(widths)
	max_height = max(heights)

	new_im = Image.new('RGB', (total_width, max_height))

	x_offset = 0
	for im in images:
		new_im.paste(im, (x_offset,0))
		x_offset += im.size[0]

	return new_im

def merge_vertically(images):
	widths, heights = zip(*(i.size for i in images))

	max_width = max(widths)
	total_height = sum(heights)

	new_im = Image.new('RGB', (max_width, total_height))

	y_offset = 0
	for im in images:
		new_im.paste(im, (0,y_offset))
		y_offset += im.size[1]

	return new_im


def give_screenshot_caption(img_name,text,fnt_path):
	img1 = Image.open(img_name)

	width,height = img1.size
	x0,y0=0,0
	x1=width
	y1=height*(5/100)
	fnt_size = int(y1)

	#img_with_border = ImageOps.expand(img1,border=fnt_size,fill='blue')
	new_im = Image.new('RGB', (width, fnt_size), (0,0,255))
	img_text = draw_text(new_im,text,fnt_path,fnt_size)
	
	img__ = merge_vertically([img_text,img1])
	img__.save(img_name, "PNG", quality=75)


def ConfigSectionMap(Config, section):
    dict1 = {}
    options = Config.options(section)

    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

class CaseConfigParser(configparser.SafeConfigParser):
    def optionxform(self, optionstr):
        return optionstr

def get_last_file_of_dir(filename):
	list_of_files = glob.glob(filename)
	latest_file = max(list_of_files, key=os.path.getctime)
	return latest_file

def open_file_with_default_app(filepath):
	import subprocess
	if platform.system() == 'Darwin':       # macOS
	    subprocess.call(('open', filepath))
	elif platform.system() == 'Windows':    # Windows
	    os.startfile(filepath)
	elif platform.system() == 'Windows':    # Windows
		subprocess.call(('xdg-open', filepath))
	else:                                   # linux variants
	    subprocess.call(('xdg-open', filepath))



def mean(li):
	return sum(li)/len(li)

def td_format_2_seconds(time_str_):

	periods = [
	    ('year',        60*60*24*365),
	    ('month',       60*60*24*30),
	    ('day',         60*60*24),
	    ('hour',        60*60),
	    ('minute',      60),
	    ('second',      1)
	]

	def search_here(key):
		return [v for p,v in periods if p == key][0]

	total_sec = 0
	dic = {}
	li = [c.strip().split(' ') for c in time_str_.split(',')]
	for c in li:
		if c[1][-1] == 's':
			c[1]=c[1][:-1]
		dic[c[1]]=c[0]
		total_sec = total_sec + float(c[0])*search_here(c[1])
		
	return total_sec


def td_format_2_delta(time_str_):
	return datetime.timedelta(seconds=td_format_2_seconds(time_str_))