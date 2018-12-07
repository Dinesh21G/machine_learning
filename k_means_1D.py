import random
def  mean(LIST):
    if LIST is None or LIST == []:
        return 0
    return sum(LIST) / len(LIST)
def abs_max(LIST):
    MAX=0
    for x in LIST:
        if abs(x)>MAX:
            MAX=abs(x)
    return MAX
def get_centroids(cluster):
    cetroid_set=[]
    for key in cluster.keys():
        cetroid_set.append(cluster[key]['centroid'])
    return cetroid_set
def rearrange(cluster,s):
    model_cluster={}
    for key in cluster.keys():
        model_cluster[key]={}
        model_cluster[key]['centroid']=mean(cluster[key]['data'])
        model_cluster[key]['data']=[]
    return fill_data(model_cluster,s)
def display(cluster):
    print "#"*80
    print "CENTROIDS :", get_centroids(cluster)
    for key in cluster.keys():
        print key, ' : ', cluster[key]['centroid'], ' : ', cluster[key]['data']
def fill_data(model_cluster,s):
    MAX_DIST=abs_max(s)
    for x in s:
        MIN_DIFF=MAX_DIST
        CLUSTER_KEY=0
        for key in model_cluster.keys():
            diff = abs(model_cluster[key]['centroid'] - x)
            if  diff < MIN_DIFF:
                MIN_DIFF = diff
                CLUSTER_KEY = key
        #print 'model_cluster[',CLUSTER_KEY,'][data].append(',x,')'
        #print CLUSTER_KEY,' : ', x
        model_cluster[CLUSTER_KEY]['data'].append(x)
                
    return model_cluster
if __name__ == '__main__':
    k=10
    limit=100
    s=[random.randint(-limit,limit) for x in xrange(limit)]
    c=[random.randint(min(s),max(s)) for x in xrange(k) ]
    #print s
    #print c
    model_cluster={}
    i=0
    for x in c:
        model_cluster[i]={}
        model_cluster[i]['centroid']=x
        model_cluster[i]['data']=[]
        i=i+1
    cluster=fill_data(model_cluster,s)
    display(cluster)
                           
    old_centroid_set=get_centroids(cluster)
                           
    cluster=rearrange(cluster,s)
    new_centroid_set=get_centroids(cluster)
                           
    while new_centroid_set != old_centroid_set:
        display(cluster)
                               
        old_centroid_set=get_centroids(cluster)
                               
        cluster=rearrange(cluster,s)
        new_centroid_set=get_centroids(cluster)
