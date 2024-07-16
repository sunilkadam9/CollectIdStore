import os, shutil, re, random, string

#direcories
#CONFIG_fILE='Config/GV.cfg'
CONFIG_fILE='Config/GV2.cfg'
TARGET_fILE='Data/GoldProject.ghp'
OUTPUT_DIR='output'
OUTPUT_PRJ='BlankProject'
OUTPUT_FILE='output/processfile.ghp'
IN_CONNECTION_PHY1='GoldProject/Physical/TIBCO EMS [Non JNDI_%%TIL_JMS_URL%%].edt'
IN_CONNECTION_PHY2='GoldProject/Physical/TIBCO EMS [Non JNDI_%%TIL_JMS_URL%%] - TIBCO Enterprise Message Service (default).prb'
OUT_CONNECTION_PHY1='output/TIBCO EMS [Non JNDI_%%TIL_JMS_URL%%].edt'
OUT_CONNECTION_PHY2='output/TIBCO EMS [Non JNDI_%%TIL_JMS_URL%%] - TIBCO Enterprise Message Service (default).prb'
IN_CONNECTION_LOGI1='GoldProject/Logical/TIL_JMS_SB.icm'
OUT_CONNECTION_LOGI1='output/TIL_JMS_SB.icm'

OUT_DIAGRAMS_FILE='\BlankProject\Diagrams\logical.props'
prefix='-89f536e:190a7da0769:-'
ids = []

#read file 
def read_target_file(file_path):
	with open(file_path,'r') as file:
		return file.read()

#readfile and store in direcory
def read_config(file_path):
	config={}
	with open(file_path,'r') as file:
		for line in file:
			key,value=line.strip().split('::')
			config[key]=value
	return config

def process_target_file(content,config,string_before,string_after):
	linespace="        "
	for key, value in config.items():
		print("key :"+key +"Value :"+value)
		if key not in content:
			end_idx=-500
			start_idx=content.find(string_before)
			print("S_start_idx :"+str(start_idx)+" end_idx"+str(end_idx))
			end_idx=content.find(string_after)#,start_idx)
			print("E_start_idx :"+str(start_idx)+" end_idx"+str(end_idx))
			print("start_idx :"+str(start_idx)+" end_idx"+str(end_idx))
			if start_idx !=-1 and end_idx !=-1:
				insert_position=end_idx+len(string_after)
				content=content[:insert_position] + linespace + value +"\n"+ content[insert_position:]
				print("Content after update inside looop " +content) 
				
	return content
	
#readfile and store in direcory and list
def read_configSa_Sb(file_path):
	config={}
	with open(file_path,'r') as file:
		for line in file:
			key,value,sa,sb=line.strip().split('::')
			config[key]=[value,sa,sb]
	return config
	

	
#process target file on key value pairs
def process_target_file(content,config,string_before,string_after):
	linespace="\n        "
	for key, [value,sa,sb] in config.items():
		print("key :"+key +"Value :"+value)
		if key not in content:
			end_idx=-500
			start_idx=content.find(sb)
			print("S_start_idx :"+str(start_idx)+" end_idx"+str(end_idx))
			end_idx=content.find(sa)#,start_idx)
			print("E_start_idx :"+str(start_idx)+" end_idx"+str(end_idx))
			print("start_idx :"+str(start_idx)+" end_idx"+str(end_idx))
			if start_idx !=-1 and end_idx !=-1:
				insert_position=end_idx+len(sa)
				content=content[:insert_position] + linespace + value + content[insert_position:]
				print("Content after update inside looop " +content) 
				
	return content
	

def process_env_file(LT_Cfg_path,target_env_path,string_before,string_after):
	#load config file 
	
	#config= read_config(CONFIG_fILE)
	
	
	files = os.listdir(LT_Cfg_path)
	for f in files:
		if os.path.isfile(LT_Cfg_path+'/'+f):
			#config=read_config(LT_Cfg_path+'/'+f)
			config=read_configSa_Sb(LT_Cfg_path+'/'+f)
			if os.path.isfile(target_env_path+'/'+f):
				targe_content=read_target_file(target_env_path+'/'+f)
				update_content=process_target_file(targe_content,config,string_before,string_after)
				with open(target_env_path+'/'+f,'w') as file: 
					file.write(update_content)
					print("SSSSSSSuccess")
			else:
				dest =shutil.copyfile(LT_Cfg_path+'/copy_ghe/'+f, target_env_path+'/'+f)
				print("File copy pested "+dest)
				
	
	#load target file 
	#targe_content=read_target_file(TARGET_fILE)
	
	#define string before and after to value to be inserted
	
	
	#update_content=process_target_file(targe_content,config,string_before,string_after)
	#print(update_content)
	
	
	
	print("SSSSSSSuccess22")
	
	
def process_projectghp_file(config_file,projectghp_file,string_before,string_after):
	#config= read_config(config_file)
	config= read_configSa_Sb(config_file)
	print(config_file + " == " )#+ config)
	targe_content=read_target_file(projectghp_file)
	print(projectghp_file + " == " + targe_content)
	update_content=process_target_file(targe_content,config,string_before,string_after)
	print("after content update " + update_content)
	with open(OUTPUT_FILE,'w') as file: 
		file.write(update_content)
	
	print("SSSSSSSuccess_project ghp")

# creating a variable and storing the text 
def findandreplace_method(file_path,search_text,replace_text):
	# Opening our text file in read only 
# mode using the open() function 
	print(file_path)
	with open(file_path, 'r') as file: 
	  
		# Reading the content of the file 
		# using the read() function and storing 
		# them in a new variable 
		data = file.read() 
	  
		# Searching and replacing the text 
		# using the replace() function 
		data = data.replace(search_text, replace_text) 
		print(data)
	  
	# Opening our text file in write only 
	# mode to write the replaced content 
	with open(file_path, 'w') as file: 
	  
		# Writing the replaced data in our 
		# text file 
		file.write(data) 
	  
	# Printing Text replaced 
	print("Text replaced")
	return 0
	

	
	
def ifnotfindthenplace_method(file_path,if_not_text,search_text,replace_text):
	# Opening our text file in read only 
# mode using the open() function 
	with open(file_path, 'r') as file: 
	  
		# Reading the content of the file 
		# using the read() function and storing 
		# them in a new variable 
		data = file.read() 
		res=data.find(if_not_text)
	  
		# Searching and replacing the text 
		# using the replace() function
		if res==-1:
			data = data.replace(search_text, replace_text) 
	  
	# Opening our text file in write only 
	# mode to write the replaced content 
	with open(file_path, 'w') as file: 
	  
		# Writing the replaced data in our 
		# text file 
		file.write(data) 
	  
	# Printing Text replaced 
	print("Text replaced")
	return 0


def createConnection(id_ph1,id_ph2,id_lg1):
	dest =shutil.copyfile(IN_CONNECTION_PHY1, OUT_CONNECTION_PHY1)
	print("File copy pested "+dest)
	findandreplace_method(dest,'$$$TIL_EMS_SB_Con_PH1$$$',id_ph1)
	dest =shutil.copyfile(IN_CONNECTION_PHY2, OUT_CONNECTION_PHY2)
	print("File copy pested "+dest)
	findandreplace_method(dest,'$$$TIL_EMS_SB_Con_PH1$$$',id_ph1)
	findandreplace_method(dest,'$$$TIL_EMS_SB_Con_PH2$$$',id_ph2)
	destination = shutil.copytree(IN_CONNECTION_LOGI1, OUT_CONNECTION_LOGI1)
	print("File copy pested "+destination)
	findandreplace_method(destination + '//config.icm','$$$TIL_EMS_SB_Con_LG1$$$',id_lg1)
	ifnotfindthenplace_method(OUTPUT_PRJ + '''/Diagrams/logical.props''',id_lg1,'''</properties>''','''<entry key="''' + id_lg1 +'''>1515.0,433.0</entry>\n</properties>''')


	ifnotfindthenplace_method(OUTPUT_PRJ + '''/Custom/TILLT1.ghe''','''<evbindings>''','''</resourceConfig>''','''<evbindings></evbindings></resourceConfig>''')
	ifnotfindthenplace_method(OUTPUT_PRJ + '''/Custom/TILLT2.ghe''','''<evbindings>''','''</resourceConfig>''','''<evbindings></evbindings></resourceConfig>''')
	ifnotfindthenplace_method(OUTPUT_PRJ + '''/Custom/TILLT3.ghe''','''<evbindings>''','''</resourceConfig>''','''<evbindings></evbindings></resourceConfig>''')

	ifnotfindthenplace_method(OUTPUT_PRJ + '''/Custom/TILLT1.ghe''','''<evbinding evLogicalItemId="''' + id_lg1 +'''" evPhysicalItemId="''' + id_ph1 +'''"/>''','''</evbindings>''','''<evbinding evLogicalItemId="''' + id_lg1 +'''" evPhysicalItemId="''' + id_ph1 +'''"/></evbindings>''')

	ifnotfindthenplace_method(OUTPUT_PRJ + '''/Custom/TILLT2.ghe''','''<evbinding evLogicalItemId="''' + id_lg1 +'''" evPhysicalItemId="''' + id_ph1 +'''"/>''','''</evbindings>''','''<evbinding evLogicalItemId="''' + id_lg1 +'''" evPhysicalItemId="''' + id_ph1 +'''"/></evbindings>''')

	ifnotfindthenplace_method(OUTPUT_PRJ + '''/Custom/TILLT3.ghe''','''<evbinding evLogicalItemId="''' + id_lg1 +'''" evPhysicalItemId="''' + id_ph1 +'''"/>''','''</evbindings>''','''<evbinding evLogicalItemId="''' + id_lg1 +'''" evPhysicalItemId="''' + id_ph1 +'''"/></evbindings>''')	
	return 0


def find_ids_in_file(file_path):
    """
    Reads a file and extracts all 'id' occurrences using regular expressions.
    Assumes the 'id' is in the format 'id: <value>' or 'id = <value>'.
    """
    ids = []
    id_pattern = re.compile(r'''\sid="(.*)[,(.*)|"$]''', re.IGNORECASE)

    try:
        with open(file_path, 'r') as file:
            content = file.read()
            ids.extend(id_pattern.findall(content))
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")

    return ids

def collect_ids(directory):
    """
    Recursively traverse the directory and subdirectories to find and collect all ids.
    """
    all_ids = []

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_ids = find_ids_in_file(file_path)
            all_ids.extend(file_ids)

    return all_ids

def generate_random_hex_chars(num_chars):
    # Define the set of hexadecimal characters
    hex_chars = string.hexdigits.lower()
    
    # Generate the random string
    random_hex_string = ''.join(random.choices(hex_chars, k=num_chars))
    print(random_hex_string)
    return random_hex_string	

def generate_unique_id(num_chars,prefix,collection):
	id=prefix + generate_random_hex_chars(4)
	if id in collection:
		print(id + "is present in collection")
		return generate_unique_id(num_chars,prefix,collection)
	else:
		#ids.append(id)
		#print(f'ssssssssssssssss {ids}')
		return id
	
def main():
	if not os.path.exists(OUTPUT_DIR):
		os.mkdir(OUTPUT_DIR)
		
	ids = collect_ids(OUTPUT_PRJ)
	print(f"Collected IDs: {ids}")
	
	#id_prefix='-89f536e:190a7da0769:-'
	#print(id_prefix)
	
	next_id=generate_unique_id(4,prefix,ids)
	print(next_id)
	ids.append(next_id)
	id_ph1=generate_unique_id(4,prefix,ids)
	id_ph2=generate_unique_id(4,prefix,ids)
	id_lg1=generate_unique_id(4,prefix,ids)
	ids.append(id_ph1)
	ids.append(id_ph2)
	ids.append(id_lg1)
	print(f"Collected IDs: {ids}")
	
	
	#define string before and after to value to be inserted
	string_before='''<environmentVariable evdescription='''
	string_after='''overridingSecretsNamespace="">'''
	#update project ghp 
	#process_projectghp_file(CONFIG_fILE,OUTPUT_FILE,string_before,string_after)
	
	#update env 
	#process_env_file('Config/LT',OUTPUT_DIR,string_before,string_after)
	
	#create connection
	resultcopy=createConnection(id_ph1,id_ph2,id_lg1)
	#print(resultcopy)
	
	#add connection to daigram
	
	#map binding to each env 
	
	#

if __name__=="__main__":
	main()
		
