import sys, os
import pandas
import getopt
import re

def main(argv):
	'''
	main function
	'''
	script_dir, script_name = os.path.split(os.path.abspath(sys.argv[0]))
	df = pandas.read_csv('{}/example.csv'.format(script_dir))
	options_dict = {}
	format_of_file, output_file = "", ""
	# get the Arguments
	try:
		opts, argv = getopt.getopt(sys.argv[1:],"hf:o:s:y:n:", ["help", "format=", "outputfile=", "sex=", "yob=", "name="])
	except getopt.GetoptError as err:
		print(err)
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('Run script with: -f <format of file> -o <name of file> -s <male/female> -y <year of birth> -n <name of fugitive>')
			sys.exit()
		elif opt in ("-f", "--format"):
			format_of_file = ".{}".format(arg)
		elif opt in ("-o", "--outputfile"):
			output_file = arg
		elif opt in ("-s", "--sex"):
			options_dict.update({"sex": arg})
		elif opt in ("-y", "--yob"):
			options_dict.update({"dob": arg})
		elif opt in ("-n", "--name"):
			options_dict.update({"name": arg})

	print("SCRIPT STARTS WITH PARAMS: {}".format(options_dict))
	
	if format_of_file is None:
		format_of_file = '.json'
	if output_file is None:
		output_file = "default-output-name"

	
	my_new_df = pandas.DataFrame()
	for key, val in options_dict.items():
		for index, row in df.iterrows():
			if re.match(r'{}'.format(val), "{}".format(row[key]), flags=re.I) is not None:
				my_new_df = my_new_df.append(row, ignore_index=True)

	my_new_df.to_json("{}/{}{}".format(script_dir,output_file,format_of_file))

if __name__ == "__main__":
	main(sys.argv[1:])

