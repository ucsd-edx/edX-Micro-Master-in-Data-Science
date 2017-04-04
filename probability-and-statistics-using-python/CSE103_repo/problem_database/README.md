## Markdown files to XML files

* ```problem_XML_files``` has problems in XML outputed from ```translate.py```

* ```problem_information_from_WebWork``` has informations gathered from WebWork for each assignment.

* ```problem_source_files``` has problems written in markdown

* ```translate.py``` is used to generate XML files from markdown files using ```template.xml``` as problem template.

* ```translate_w_variables.py``` is used to generate XML files from markdown files using ```template_w_variables.xml``` as problem template. This is used specifically for problems with variables in solution.


## How to write problem and tranlate to XML ([Tutorial Video](https://www.youtube.com/watch?v=5IE5V39dE4E))

### Writing problem.md (See sample.md)
1. Writing python code
	* Wrap the python code with the following with no space at front.

		\`\`\`python

		\`\`\`

	* First define random variables (if needed). You don't need to import random library.

	* Then define your solutions for all your parts. Name the solution variable with part id at the end. For example, 'solution1' will be the solution for part 1, 'solution2' will be solution for part 2.

		* You can't assign a variable to solutions. Solution variables have to be assigned with a string directly. For example, you can't do

				a = "3*5"
				solution1 = a

			instead, you need to do

				solution1 = "3*5"

	* Each solution variable should be a string with variable values plugged in. Recommend using ```.format()```.

		* When there is power operation "\*\*", change it to "^". Also wrap the exponent with {{}} when you use format. For example, 2^n will be "2^{{{0}}}".format(n)

		If you are not using format, you only need one {}. For example: 2^{10}.

		* If you see exponential expression, skip the problem.

	* Then group your solutions in a list. Make sure you name the list **solutions**.

2. Writing problem content
	* Please format the problem nicely using markdown syntax. Bullet points are highly recommended.

		* When there is math expression. If you want to have inline math expression use "$" and "$$". If you want math expression in a new line, use "$$" and "$".

	* Place ```[_]``` where you want a input box to appear. Make sure your input box is in a newline. In Markdown, you need to have a newline above and a newline below ```[_]``` in order to be in a newline. We don't want to have inline input box.

	* After you finish the problem, double check to make sure the solutions you defined in your python code match the order of the parts. The first input box should be matched with ```solution1``` and so on.

	* When using the variables defined in the python, e.g. a, use "\$a". There are "\$a" apples in "\$b" trees.

	* Here is a sample for checkbox

		* You can use variables like this: \$n and \$k

				[ ] This is a wrong choice
				[x] This is a right choice
				[ ] This is another wrong choice
				[x] This is another right choice

3. Save your file as "WeekId_ProblemId.imd". For example: "Week3_Problem12.imd" in folder markdown_files


### Running translator script
* open terminal to run

		python translate_imd.py <week_id> <problem_id>

* find output file in ```output_files``` folder

* copy paste content to edX to test
