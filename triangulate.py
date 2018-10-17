def triangulate(locs, strengths):
	lengths = [strength_to_length(x) for x in strengths]
	x = (lengths[0]**2 - lengths[1]**2)/2 - 1
	y = sqrt(lengths[1]**2 - x**2)
	print("got location and it's the following:")
	print (x,y)

	return (x,y)


def strength_to_length(x):
	return 10**((27.55 - (20 * math.log10(2412)) + math.abs(x))/20)