import datetime
t1 = datetime.datetime.now()
import reviewextraction
import reviewvectorize
from sklearn.cluster import KMeans
from sklearn import preprocessing

x = reviewvectorize.vector.astype(float)

print("Scaling..")

x = preprocessing.normalize(x)
x =preprocessing.scale(x)

print("Scaled.")

print("Started kmeans....")


kmeans = KMeans(n_clusters=10 ,random_state= 0).fit(x)

print("Kmeans done..")

# trans = kmeans.cluster_centers_.argsort()[:,::-1]
# output = []
# for i in range(len(trans)):
#     translist = []
#     for index in list(trans[i, :5]):
#         translist.append(reviewvectorize.common_words_with_count[index])
#     output.append(translist)
# print("Output clusters with top 5 words:")
# print(output)

tran = kmeans.cluster_centers_.argsort()[:,::-1]
output = []
output_feature_val = []
for i in range(len(tran)):
    tlist = []
    outputtranslist = []
    for index in list(tran[i, :5]):
        tlist.append(reviewvectorize.common_words[index])
        outputtranslist.append(kmeans.cluster_centers_[i, index])
    output.append(tlist)
    output_feature_val.append(outputtranslist)

print(output)

f = open("clusters.txt", "w")
for i in range(len(output)):
    f.write("Clustering " + str(i+1)+"\n")
    for j in range(len(output[i])):
        f.write(output[i][j] + " - " + str(output_feature_val[i][j]) + "\n")
    f.write("\n\n")


t2 = datetime.datetime.now()
time = t2 -t1
print("Total time: %s seconds"%time.seconds)


# # df = pd.read_pickle("words.pickle")
#
# total_instances = len(df[:-1])
# #
# data_frame = pd.DataFrame(columns=df[0])
#
#
# for i in range(1,total_instances):
#      data_frame.loc[i-1] = df[i]
#
#
# print(data_frame.describe())
# print(data_frame.head())