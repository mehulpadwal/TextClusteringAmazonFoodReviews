import re

# product/productId: B001E4KFG0
# review/userId: A3SGXH7AUHU8GW
# review/profileName: delmartian
# review/helpfulness: 1/1
# review/score: 5.0
# review/time: 1303862400
# review/summary: Good Quality Dog Food
# review/text: I have bought several of the Vitality canned dog food products and have found them all to be of good quality. The product looks more like a stew than a processed meat and it smells better. My Labrador is finicky and she appreciates this product better than  most.

print("Extracting Reviews from foods.txt...")

data = open("foods.txt")

line = data.readline()

counter = 0

f = open("reviews.txt", "w")

while line != "":
    if(re.findall(r'review/text', line)):
        counter +=1

        review = re.findall(r'^review/text: .*$', line)[0].split("review/text: ")

        f.write("%s,\n"%review[1].lower())

    #
    # if counter ==  1000:
    #     break
    line = data.readline()

print("Reviews Extracted from foods.txt: %s"%counter)