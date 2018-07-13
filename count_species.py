import sys
from reaction_tools import *
#
# count species
#
argvs = sys.argv
reactionfile = argvs[1]

speciesfile  = "species.txt"

fspecies = open(speciesfile, "w")

(r_ads, r_site, r_coef,  p_ads, p_site, p_coef) = get_reac_and_prod(reactionfile)

species = []
rxnnum = len(r_ads)
for irxn in range(rxnnum):
	#
	# reactant
	#
	for imol,mol in enumerate(r_ads[irxn]):
		mol  = mol[0]
		site = r_site[irxn][imol]
		site = site[0]
		try:
			site, site_pos = site.split(".")
		except:
			site_pos = "x1y1"

		if site != 'gas':
			mol = mol + "_surf" # Not distinguish different sites. Reconsideration may be needed.

		if '-SIDE' in mol:
			mol = mol.replace('-SIDE','')
		if '-FLIP' in mol:
			mol = mol.replace('-FLIP','')

		species.append(mol)

	#
	# product
	#
	for imol,mol in enumerate(p_ads[irxn]):
		mol  = mol[0]
		site = p_site[irxn][imol]
		site = site[0]
		try:
			site, site_pos = site.split(".")
		except:
			site_pos = "x1y1"

		if site != 'gas':
			mol = mol + "_surf"

		if '-SIDE' in mol:
			mol = mol.replace('-SIDE','')
		if '-FLIP' in mol:
			mol = mol.replace('-FLIP','')

		species.append(mol)


# species = [item for sublist in species for item in sublist]
species = list(set(species)) # remove duplication
species.sort()

surf = [i for i in species if 'surf' in i]
gas  = [i for i in species if not 'surf' in i]

species = gas + surf

# put 'surf' to the last
for item in species:
	if item == 'surf':
		species.remove(item)
		species.append(item)

fspecies.write(str(species))
fspecies.close()

