import numpy as np

#function for changing H:M:S to decimal degree
def hms2dec(a,b,c):
    return (15*(a + b/60 + c/3600))

#convert D:M:S to decimal degree
def dms2dec(a,b,c):
    if (a>0):
        return (a + b/60 + c/3600)
    else:
        return (-1*(abs(a) + b/60 + c/3600))

#measering the angular distance between two given point in celestial sphere
def angular_dist(ra1,dec1,ra2,dec2):
    r1 = np.radians(ra1)
    r2 = np.radians(ra2)
    d1 = np.radians(dec1)
    d2 = np.radians(dec2)
    
    a = np.sin(np.abs(d1-d2)/2)**2
    b = np.cos(d1) * np.cos(d2) * np.sin(np.abs(r1-r2)/2)**2
    
    d = 2*np.arcsin(np.sqrt(a+b))
    d = np.degrees(d)
    return d


# From the AT20G bright source sample survey (http://cdsarc.u-strasbg.fr/viz-bin/Cat?J/MNRAS/384/775), 
# we'll be using the file table2.dat under the section FTP
# this function imports the AT20G BSS and returns a list of tuples containing the object's ID (an integer)
# and the coordinates in degrees.

def import_bss():
    bss_array = np.loadtxt('bss.dat',usecols=range(1,7))
    bss = []
    for i in range(len(bss_array)):
        bss.append((i+1, hms2dec(bss_array[i][0], bss_array[i][1], bss_array[i][2]), dms2dec(bss_array[i][3], bss_array[i][4], bss_array[i][5])))
    return bss

# The original data is available on SuperCOSMOS all-sky catalogue (http://ssa.roe.ac.uk/allSky)
# in a package called SCOS_XSC_mCl1_B21.5_R20_noStepWedges.csv.gz. 
# As this catalogue is so large, we've cut down to 500 data in a file named super.csv.
# This function imports the super.csv as a list of tuples containing the object's ID (an integer) and the coordinates in degrees.
def import_super():
    super_array = np.loadtxt('super.csv',delimiter=',',skiprows=1,usecols=[0,1])
    super = []
    for i in range(len(super_array)):
        super.append((i+1,super_array[i][0],super_array[i][1]))
    return super

# function that takes a catalogue and the position of a target source (a right ascension and declination) 
# and finds the closest match for the target source in the catalogue
# this function returns the ID of the closest object and the distance to that object
def find_closest(cat, ra, dec):
    min = angular_dist(cat[0][1],cat[0][2],ra,dec)
    min_id = 1
    for i in range(len(cat)):
        dist = angular_dist(cat[i][1], cat[i][2], ra, dec)
        if ( dist < min):
            min = dist
            min_id = cat[i][0]       
    return (min_id, min)

# The function crossmatches two catalogues within a maximum distance. 
# It returns a list of matches and non-matches for the first catalogue against the second.

# The list of matches contains tuples of the first and second catalogue object IDs and their distance. 
# The list of non-matches contains the unmatched object IDs from the first catalogue only. 
# Both lists are ordered by the first catalogue's IDs.
def crossmatch(cat1, cat2, max_dist):
    matches = []
    no_matches = []
    for i in cat1:
        id, dist = find_closest(cat2, i[1], i[2])
        if (dist <= max_dist):
            matches.append((i[0], id, dist))
        else:
            no_matches.append(i[0])
    return (matches, no_matches)



# Using this to test our function.
if __name__ == '__main__':
  bss_cat = import_bss()
  super_cat = import_super()

  # First example in the question
  max_dist = 40/3600
  matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
  print(matches[:3])
  print(no_matches[:3])
  print(len(no_matches))

  # Second example in the question
  max_dist = 5/3600
  matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
  print(matches[:3])
  print(no_matches[:3])
  print(len(no_matches))
