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

# remove 'surf' from adsorbate list
for lst in [r_ads, p_ads]:
	for ads in lst:
		if 'surf' in ads:
			ads.remove('surf')

species = []
rxnnum = len(r_ads)
for irxn in range(rxnnum):
	for imol,mol in enumerate(r_ads[irxn]):
		site = r_site[irxn][imol]
		try:
			site, site_pos = site.split(".")
		except:
			site_pos = "x1y1"

		if site != 'gas':
			mol = mol + "_surf" # Not distinguish different sites. Variant may exist.

		species.append(mol)

	for imol,mol in enumerate(p_ads[irxn]):
		site = p_site[irxn][imol]
		try:
			site, site_pos = site.split(".")
		except:
			site_pos = "x1y1"

		if site != 'gas':
			mol = mol + "_surf"

		species.append(mol)


# species = [item for sublist in species for item in sublist]
species = list(set(species)) # remove duplication

fspecies.write(str(species))
fspecies.close()

