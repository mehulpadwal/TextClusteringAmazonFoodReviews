# TextClusteringAmazonFoodReviews
Making keyword clusters with Amazon Food review data

Prerequisites:
1. Install Python 3.6 or lower which is tensorflow compatible (Python 3.7 is not compatible as of this time)
2. Install tensorflow(pip install tensorflow)
3. Install sklearn( pip install scikit-learn)

Steps:
1. Download the fine foods dataset from: http://snap.stanford.edu/data/web-FineFoods.html
2. Extract foods.txt it to a new folder
3. Copy files stopwords.txt, reviewextraction.py, reviewvectorize.py and reviewcluster.py to the
newly created folder such that you have total of 5 files.
4. Open Command-Line and change directory to the folder
5. Run reviewcluster.py

Output Clusters examples:
['chips', 'potato', 'chip', 'vinegar', 'salt']
['bulk', 'reading', 'reviews', 'buying', 'buy']
['coffee', 'cup', 'roast', 'keurig', 'cups']
['product', 'order', 'amazon', 'price', 'arrived']
['jerky', 'beef', 'meat', 'chicken', 'spicy']
['tea', 'drink', 'teas', 'drinking', 'water']
['dog', 'food', 'treats', 'dogs', 'cat']
['snack', 'gluten', 'bars', 'free', 'bar']
['peanut', 'butter', 'fat', 'almond', 'jar']
['larger', 'size', 'smaller', 'small', 'bags']
