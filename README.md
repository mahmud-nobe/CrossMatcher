# CrossMatcher
Cross Matcher of selected portion of two astronomical catalogs (radio-wavelength  and optical)

This is done as an assignment of week 2 in the course named 'Data-driven Astronomy' offered by University of Sydney through Coursera. 

In astronomy, often we need to match two catalogs of sky observed in different wavelenght to understand and analyze the information. 
We compare the coordinates (right ascension and declination) of each identified sources of the two different catalogs. 
If two objects from different catalogs are very very close, we conclude them as the same object. Then we used these matched objects to cross-match the whole catalogs.

Here, we first import two catalogs (radio and optical wavelenght) 
The final code inputs  these two catalogs and the max_distance of same objects in different catalogs due to error and precisness,
and outputs the matched and no-matched object list.
