'''
Commutes to Combo Postprocessor
Garrett Dash Nelson and Alasdair Rae, 2016

Read the paper: http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0166083
'''

from os import path

# Check if Combo results are available
if not path.isfile('data-stage1/commutes_comm_comboC++.txt'):
	print 'Failed: Could not find Combo output file at ./data-stage1/commutes_comm_comboC++.txt'
	exit()

if not path.isdir('data-final'):
	print 'Failed: Requires an output directory data-final'
	exit()

comboRawOutput = open('data-stage1/commutes_comm_comboC++.txt')
communities = comboRawOutput.readlines()

outFile = open('data-final/fips_table_with_community_assignments.csv','w')

fipsRawInput = open('data-stage1/fips_table.csv')



fipsRawInput.next() # skip header

outFile.write('serial_id,fips,community\n')

i = 0
for line in fipsRawInput:
	outFile.write(line.rstrip() + ',' + str(communities[i]))
	i = i+1
