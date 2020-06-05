import os,sys
from reaction_tools import get_number_of_reaction

# usage: python submit.py inputfile [number of jobs]

submit_sh = "run_kyushu.sh"
argvs = sys.argv
inp   = argvs[1]
rxn_num = get_number_of_reaction(inp)

if len(argvs)==3:
	# -- specify number of jobs
	num_jobs = int(argvs[2])
	each = rxn_num // num_jobs
else:
	# --  specify reactions per jobs
	each = 5

print("rxn_num = %d, rxns per jobs = %d" % (rxn_num, each))

# remove old files
os.system("rm -rf beef-vdw*")
os.system("rm -rf tsdir")
os.system("rm tmp.db")
os.system("rm std*")

st = 0
ed = 1

finish = False
while True:
	ed = st + each
	if ed >= rxn_num:
		#
		# the end reaction number is lager than rxn_num ... the last node
		#
		ed = rxn_num - 1 # adjustment: ed+1 -1 = rxnnum
		finish = True

	command = "pjsub -x \"INP={0}\" -x \"ST={1}\" -x \"ED={2}\" {3}".format(inp, st, ed+1, submit_sh) # add one to include the last reaction
	print(command)
	os.system(command)

	if finish:
		break
	st = ed + 1

