opcode = {
	'ADD' : [3 , '18'],
	'ADDF' : [3 , '58'],
	'ADDR' : [2 , '90'],
	'AND' : [3 , '40'],
	'CLEAR' : [2 , 'B4'],
	'COMP' : [3 , '28'],
	'COMPF' : [3 , '88'],
	'COMPR' : [2 , 'A0'],
	'DIV' : [3 , '24'],
	'DIVF' : [3 , '64'],
	'DIVR' : [2 , '9C'],
	'FIX' : [1 , 'C4'],
	'FLOAT' : [1 , 'C0'],
	'HIO' : [1 , 'F4'],
	'J' : [3 , '3C'],
	'JEQ' : [3 , '30'],
	'JGT' : [3 , '34'],
	'JLT' : [3 , '38'],
	'JSUB' : [3  , '48'],
	'LDA' : [3 , '00'],
	'LDB' : [3 , '68'],
	'LDCH' : [3 , '50'],
	'LDF' : [3 , '70'],
	'LDL' : [3 , '08'],
	'LDS' : [3 , '6C'],
	'LDT' : [3 , '74'],
	'LDX' : [3 , '04'],
	'LPS' : [3 , 'D0'],
	'MUL' : [3 , '20'],
	'SUBR' : [2 , '94'],
	'SVC' : [2 , 'B0'],
	'TD' : [3 , 'E0'],
	'TIO' : [1 , 'F8'],
	'TIX' : [3 , '2C'],
	'TIXR' : [2 , 'B8'],
	'WD' : [3 , 'DC'],
	'MULF' : [3 , '60'],
	'MURL' : [2 , '98'],
	'NORM' : [1 , 'C8'],
	'OR' : [3 , '44'],
	'RD' : [3 , 'D8'],
	'RMO' : [2 , 'AC'],
	'RSUB' : [3 , '4C'],
	'SHIFTL' : [2 , 'A4'],
	'SHIFTR' : [2 , 'A8'],
	'SIO' : [1 , 'F0'],
	'SSK' : [3 , 'EC'],
	'STA' : [3 , '0C'],
	'STB' : [3 , '78'],
	'STCH' : [3 , '54'],
	'STF' : [3 , '80'],
	'STI' : [3 , 'D4'],
	'STL' : [3 , '14'],
	'STS' : [3 , '7C'],
	'STSW' : [3 , 'E8'],
	'STT' : [3 , '84'],
	'STX' : [3 , '10'],
	'SUB' : [3 , '1C'],
	'SUBF' : [3 , '5C']
}

loc = 0

file_name = input("Please input file name : ")
with open(file_name,"r") as infile:
	with open("output.txt","w") as outfile:
		for i in infile:
			line = i.split()
			for j in range(0,len(line)):
				p = 0
				if line[j][0] == '+':
					p = 1
					line[j] = line[j][1:]
				if line[j] == 'START':
					outfile.write(hex(loc)[2:].zfill(4).upper()+'\t'+i)
					if line[j+1][0] != '#':
						loc = int(line[j+1])
					else:
						loc = int(line[j+1][1:],16)
					break
				elif line[j] == 'END' or line[j] == 'BASE' or line[j] == '.':
					outfile.write('    \t'+i)
					break
				elif line[j] == 'BYTE':
					if line[j+1][0] == 'X':
						outfile.write(hex(loc)[2:].zfill(4).upper()+'\t'+i)
						loc += 1
					elif line[j+1][0] == 'C':
						outfile.write(hex(loc)[2:].zfill(4).upper()+'\t'+i)
						loc += 3
					break
				elif line[j] == 'WORD':
					outfile.write(hex(loc)[2:].zfill(4).upper()+'\t'+i)
					loc += 3
					break
				elif line[j] == 'RESW':
					outfile.write(hex(loc)[2:].zfill(4).upper()+'\t'+i)
					if line[j+1][0] != '#':
						loc += (3*int(line[j+1]))
					else:
						loc += (3*int(line[j+1][1:],16))
					break
				elif line[j] == 'RESB':
					outfile.write(hex(loc)[2:].zfill(4).upper()+'\t'+i)
					if line[j+1][0] != '#':
						loc += int(line[j+1])
					else:
						loc += int(line[j+1][1:],16)
					break
				elif str(opcode.get(line[j])) != 'None':
					outfile.write(hex(loc)[2:].zfill(4).upper()+'\t'+i)
					loc += (opcode[line[j]][0] + p)
					break