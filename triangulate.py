import math

a = 55.6

def triangulate(locs, strengths):
	lengths = [strength_to_length(x) for x in strengths]
	print ("here are the lengths that we got: ")
	print (lengths)
	x = abs(lengths[0]**2 - lengths[1]**2 + (a**2))/(a*2)
	print (x)
	try:
	    y = math.sqrt(lengths[0]**2 - x**2)
	    print("got location and it's the following:")
            print (x,y)

            return (x,y)

        except:
            print ("couldn't calculate the location because of bad readings") 


def strength_to_length(x):
	return 10**((27.55 - (20 * math.log10(2412)) + abs(x))/20)
