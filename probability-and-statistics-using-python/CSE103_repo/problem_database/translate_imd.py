## Written by Zipeng Yan and Zhen Zhai
## Translate imd files to xml
## Can have math expressions wrapped with $$ \math $$
## and also inline math expression $ \math $
## Use variables in html by having \$ at front

import markdown
import json
import sys

def read_md(contents):
    '''
    Given source string, split python code and convert the rest md to html
    input:
        contents: source file string

    output:
        python_code: python code string
        html_code: converted html
    '''

	if "```python\n" in contents:
		start_index = contents.index("```python\n")
		end_index = contents.index("```\n")
		python_code = contents[start_index+1:end_index]
		python_code = "".join(python_code)
		md_code = contents[end_index+1:]
	else:
		python_code = ""
		md_code = contents

	inline = 0  # open or closed parantheses
	double = 0  # open or closed brackets
	inlineSub = ['\\\\\\(', '\\\\\\)']
	doubleSub = ['\\\\\\[', '\\\\\\]']
	for j in xrange(len(md_code)):
		line = md_code[j]
		while line[0] == " ":
			line = line[1:]
		while len(line) > 3 and line[-2] == " ":
			line = line[:-2] + line[-1]
		line = line.replace('\\$','\001')   # record dollar sign in $var by a safe substitute
		i=0
		while i < len(line):
			if line[i:i+2] == '$$':
				line = line[:i]+doubleSub[double]+line[i+2:]
				double = 1-double
				i += 4
				continue
			if line[i] == '$':
				line = line[:i]+inlineSub[inline]+line[i+1:]
				inline = 1-inline
				i += 4
				continue
			i += 1
		line = line.replace('\001','$')
		md_code[j] = line
	html_code = markdown.markdown("".join(md_code), extensions=['markdown.extensions.tables'], output_format="HTML")

	f.close()
	return python_code, html_code

def convert_html(html_code, py_code, template):
	html_code = html_code.splitlines()
	py_code = py_code.splitlines()

	start_index = template.index('    <customresponse cfn="check" expect="\\[$solution1\\]">\n')
	end_index = start_index+4
	answer_box_xml_code = template[start_index:end_index]
	template = template[:start_index] + template[end_index:]

	start_index2 = template.index('    <optionresponse>\n')
	end_index = start_index2+3
	drop_down_box_xml_code = template[start_index2:end_index]
	template = template[:start_index] + template[end_index:]

	start_index3 = template.index('    <choiceresponse>\n')
	end_index = start_index3+4
	choice_box_xml_code = template[start_index3:end_index]
	choice_code = choice_box_xml_code[:]
	template = template[:start_index] + template[end_index:]

	updated_html_code = []
	part_id = 1
	for line in html_code:
		if '<p>[_choice]</p>' == line:
			updated_html_code += ['\n', '\n']
			xml_code = drop_down_box_xml_code[:]
			for s in py_code:
				if '=' not in s:
					continue
				strip_start_index = s.index('=')
				strip_s = s[:strip_start_index+1].replace(" ", "") + s[strip_start_index+1:]
				sol_str = 'solution'+str(part_id)+"="
				opt_str = 'option'+str(part_id)+"="
				if sol_str in strip_s:
					sol_index = strip_s.index(sol_str)
					sol = strip_s[sol_index+len(sol_str):]
					while sol[0] == ' ':
						sol = sol[1:]
					sol = sol.replace('\n','')
					sol = sol.replace('"','')
					sol = sol.replace("'", "")
				elif opt_str in strip_s:
					opt_index = strip_s.index(opt_str)
					opt = strip_s[opt_index+len(opt_str):]
					while opt[0] == ' ':
						opt = opt[1:]
					opt = opt.replace("\n","")

			xml_code[1] = xml_code[1].replace('$sol', sol)
			xml_code[1] = xml_code[1].replace('$opt', opt)
			updated_html_code += xml_code
			updated_html_code += ['\n', '\n']
			part_id += 1
		elif '<p>[_]</p>' == line:
			xml_code = answer_box_xml_code[:]
			updated_html_code += ['\n', '\n']
			xml_code[0] = xml_code[0].replace('solution1', 'solution'+str(part_id))
			updated_html_code += xml_code
			updated_html_code += ['\n', '\n']
			part_id += 1
		elif '[ ]' in line or '[x]' in line:
			if '<p>' in line:
				updated_html_code += ['\n', '\n']
				line = line[3:]
			choice_insert = '<choice correct="true">Urdu</choice>\n'
			choice_context = line[3:]
			if '</p>' in line:
				end_index = line.index("</p>")
				choice_context = line[3:end_index]
			while choice_context[0] == ' ':
				choice_context = choice_context[1:]
			while choice_context[-1] == ' ':
				choice_context = choice_context[:-1]
			choice_insert = choice_insert.replace('Urdu', choice_context)
			if '[ ]' in line:
				choice_insert = choice_insert.replace('true', 'false')

			choice_code = choice_code[:-2] + [choice_insert] + choice_code[-2:]

			if '</p>' in line:
				updated_html_code += choice_code
				updated_html_code += ['\n', '\n']
				part_id += 1
				choice_code = choice_box_xml_code[:]
		else:
			updated_html_code.append(line)
			updated_html_code.append("\n")
	updated_html_code = "".join(updated_html_code)
	template.insert(start_index, updated_html_code)
	return template




if __name__ == "__main__":
	if sys.argv[1] == "--help":
		print "Please type in parameters as follow(if you have variables type in 1 at the end):"
		print "python translate.py <Week ID> <Problem ID> <1>"
		sys.exit()

	var = ""
	if len(sys.argv) == 3:
		week, problem = sys.argv[1:]
	elif len(sys.argv) == 4:
		week, problem, var = sys.argv[1:]
	else:
		sys.exit("Error, see 'python translate.py --help' for input requirement")

    # get source file name
	mapping = json.loads(open("problems_mapping.json").read())
	mapping_key = "Week{0}_Problem{1}".format(week, problem)
	file_name = mapping[mapping_key]
	input_file_name = "problem_source_files/{0}".format(file_name)
	output_file_name = "problem_XML_files/{0}.xml".format(mapping_key)

    # get template
	if var:
		template_file = "template_w_variables.xml"
	else:
		template_file = "template.xml"

	f = open(template_file, "r")
	template = f.readlines()
	f.close()

    # for testing 
	# input_file_name = "problem_source_files/zhipengyan/{}.imd".format(sys.argv[1])
	# output_file_name = "problem_source_files/zhipengyan/{}.xml".format(sys.argv[1])
	f = open(input_file_name, "r")
	contents = f.readlines()
	f.close()

	print "generating XML"

	py_code, html_code = read_md(contents)
	template.insert(3, py_code)
	template = convert_html(html_code, py_code, template)

	print "writing files ..."

	f = open(output_file_name, "w")
	f.write("".join(template))
	f.close()

	print "Done! XML files saved in output_files folder!"
