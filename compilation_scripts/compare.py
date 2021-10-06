import os, sys

analysis_lines = []
patent_lines = []
new_lines_from_patents = []
cwd = os.getcwd()

full_dirname = ''.join([cwd, '/docs/tasks/implementation/'])
for cur, _dirs, files in os.walk(full_dirname):
	for directory in _dirs:
		if directory in ['functions', 'interfaces']:
			full_dirname2 = '/'.join([full_dirname, directory])
			for cur2, dirs2, files2 in os.walk(full_dirname2):
				for filename2 in files2:
					if '.py' in filename2:
						full_filename = ''.join([cur2, '/', filename2])
						with open(full_filename, 'r') as f:
							print('opening full_filename', full_filename)
							lines = f.readlines()
							if len(lines) > 0:
								for line in lines:
									letters = ''.join([char for char in line.strip().lower() if char in 'abcdefghijklmnopqrstuvwxyz '])
									if len(letters) > 0:
										analysis_lines.append(letters)

for cur, _dirs, files in os.walk(cwd):
	for filename in files:
		if filename in ['interface_analysis_notes.py', 'solution_automation_notes.py']:
			full_filename = ''.join([cur, '/', filename])
			with open(full_filename, 'r') as f:
				print('opening full_filename', full_filename)
				lines = f.readlines()
				if len(lines) > 0:
					for line in lines:
						letters = ''.join([char for char in line.strip().lower() if char in 'abcdefghijklmnopqrstuvwxyz '])
						if len(letters) > 0:
							patent_lines.append(line)
							if letters not in analysis_lines:
								if line not in new_lines_from_patents:
									new_lines_from_patents.append(line)

print('analysis lines', len(analysis_lines), analysis_lines[0])
print('patent lines', len(patent_lines), patent_lines[0])
print('new lines', len(new_lines_from_patents), new_lines_from_patents[0])
open('new_lines.txt', 'w').write('\n'.join(new_lines_from_patents))