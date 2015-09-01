from tokenizer import *
from cooccurence import *
from kmeans import *
from operator import itemgetter


arrmain = [',', '.', '|', '(', ')', '"']

def get_arr(token_arr):
    arr = []
    for each in token_arr:
        if each not in arrmain:
            arr.append(each)
    return arr

def main():
    token_dic, token_arr = token_it('Hindi.txt')
    arr = []
    j = 0
    for each in token_dic:
        if each not in arrmain:
            if j == 50:
                break
            arr.append(each)
            j += 1

    token_arr = get_arr(token_arr)
    test = co_occurence_matrix()
    test.set_row_index(arr)
    test.set_column_index(token_arr)
    mat = test.fill_matrix(1)
    print 'matrix got, clustering begins'
    groups, centroid = kmeans_cluster(mat, 50)

    indexarr = test.get_reverse_index()

    arr = [[] for i in xrange(0, 50)]
    for each in groups:
        ind = groups[each]
        arr[ind].append(each)

    arr2 = [[] for i in xrange(0, 50)]
    for i in xrange(0, 50):
        central = centroid[i]
        for each in arr[i]:
            if len(arr2[i]) > 0:
                arr2[i].sort(key=itemgetter(1), reverse=True)
            if len(arr2[i]) < 25:
                arr2[i].append((each, get_euclidean_distance(mat[each], central)))
            else:
                dist1 = get_euclidean_distance(mat[each], central)
                dist2 = arr2[i][0][1]
                if dist1 < dist2:
                    arr2[i][0] = (each, dist1)

    for each in arr2:
        for every in each:
            print indexarr[every[0]], ' , ',
        print '\n'

def main2():
    token_dic, token_arr = token_it('Hindi.txt')
    arr = []
    j = 0
    fp = open('hindi_stopwords.txt')
    line = fp.readlines()
    ff = {}
    for each in line:
        ff[each.split('\n')[0]] = 'p'

    for each in token_dic:
        if each not in arrmain:
            if j == 50:
                break
            if not ff.has_key(each):
                arr.append(each)
                j += 1

    token_arr = get_arr(token_arr)
    test = co_occurence_matrix()
    test.set_row_index(arr)
    test.set_column_index(token_arr)
    mat = test.fill_matrix(1)
    print 'matrix got, clustering begins'
    groups, centroid = kmeans_cluster(mat, 50)

    indexarr = test.get_reverse_index()

    arr = [[] for i in xrange(0, 50)]
    for each in groups:
        ind = groups[each]
        arr[ind].append(each)

    arr2 = [[] for i in xrange(0, 50)]
    for i in xrange(0, 50):
        central = centroid[i]
        for each in arr[i]:
            if len(arr2[i]) > 0:
                arr2[i].sort(key=itemgetter(1), reverse=True)
            if len(arr2[i]) < 25:
                arr2[i].append((each, get_euclidean_distance(mat[each], central)))
            else:
                dist1 = get_euclidean_distance(mat[each], central)
                dist2 = arr2[i][0][1]
                if dist1 < dist2:
                    arr2[i][0] = (each, dist1)

    for each in arr2:
        for every in each:
            print indexarr[every[0]], ' , ',
        print '\n'

def main3():
    token_dic, token_arr = token_it('Hindi.txt')
    arr = []
    j = 0
    for each in token_dic:
        if each not in arrmain:
            if j == 300:
                break
            if j >= 50:
                arr.append(each)
            j += 1

    token_arr = get_arr(token_arr)
    test = co_occurence_matrix()
    test.set_row_index(arr)
    test.set_column_index(token_arr)
    mat = test.fill_matrix(1)
    print 'matrix got, clustering begins'
    groups, centroid = kmeans_cluster(mat, 50)

    indexarr = test.get_reverse_index()

    arr = [[] for i in xrange(0, 50)]
    for each in groups:
        ind = groups[each]
        arr[ind].append(each)

    arr2 = [[] for i in xrange(0, 50)]
    for i in xrange(0, 50):
        central = centroid[i]
        for each in arr[i]:
            if len(arr2[i]) > 0:
                arr2[i].sort(key=itemgetter(1), reverse=True)
            if len(arr2[i]) < 25:
                arr2[i].append((each, get_euclidean_distance(mat[each], central)))
            else:
                dist1 = get_euclidean_distance(mat[each], central)
                dist2 = arr2[i][0][1]
                if dist1 < dist2:
                    arr2[i][0] = (each, dist1)

    for each in arr2:
        for every in each:
            print indexarr[every[0]], ' , ',
        print '\n'

#print '1'
#main()
#print '2'
#main2()
print '3'
main3()
