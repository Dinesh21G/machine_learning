import random, math
def mean(cordinates):
	if cordinates is None or cordinates == [] or cordinates == {}:
		return (0,0)
	length = len(cordinates)
	X=0
	Y=0
	for point in cordinates:
		x,y=point
		X=X+x
		Y=Y+y
	return (X/length,Y/length)
def abs_max(cordinates):
	X=0
	Y=0
	for point in cordinates:
		x,y=point
		if X < abs(x):
			X=x
		if Y < abs(y):
			Y=y
	return (X,Y)
def get_centroids(cluster):
	centroid_set=[]
	for key in cluster.keys():
		centroid_set.append(cluster[key]['centroid'])
	return centroid_set
def rearrange(cluster,s):
	model_cluster={}
	for key in cluster.keys():
		model_cluster[key]={}
		model_cluster[key]['centroid']=mean(cluster[key]['data'])
		model_cluster[key]['data']=[]
	return fill_data(model_cluster,s)
def display(cluster):
	print "#"*160
	for key in cluster.keys():
		print key, ' : ', cluster[key]['centroid'], ' : ', cluster[key]['data']
def distance(point1,point2):
	x1,y1=point1
	x2,y2=point2
	'''
	   -----------------------------------
	2 /              2                2
	\/    ( x1 - x2 )   +  ( y1 - y2 )
	'''
	return  math.sqrt( (x1-x2)**2 + (y1-y2)**2 )
def fill_data(model_cluster,s):
	''' to fill the element to the closet centrois dict'''
	MAX_DIST=abs_max(s)
	for point in s:
		min_dist=MAX_DIST
		CLUSTER_KEY = 0
		for key in model_cluster.keys():
			DISTANCE = abs( distance( model_cluster[key]['centroid'], point ) )
			if min_dist > DISTANCE:
				min_dist = DISTANCE
				CLUSTER_KEY = key
		model_cluster[CLUSTER_KEY]['data'].append(point)
	return model_cluster
if __name__ == '__main__':
	k=10
	limit=100
	sample   = [ ( random.randint(-limit,limit), random.randint(-limit,limit) ) for x in range(limit)]
	centroid = [ ( random.randint(-limit,limit), random.randint(-limit,limit) ) for x in range(k)]
	model_cluster = {}
	i=0
	for c in centroid:
		model_cluster[i]={}
		model_cluster[i]['centroid'] = c
		model_cluster[i]['data'] = []
		i=i+1
	cluster = fill_data(model_cluster, sample)
	display(cluster)

	old_centroid_set=get_centroids(cluster)
						   
	cluster=rearrange(cluster,sample)
	new_centroid_set=get_centroids(cluster)
						   
	while new_centroid_set != old_centroid_set:
		display(cluster)
							   
		old_centroid_set=get_centroids(cluster)
							   
		cluster=rearrange(cluster,sample)
		new_centroid_set=get_centroids(cluster)