from collections import Counter
import pandas as pd

df = pd.read_csv('iphone_reviews.csv')

all_reviews = ' '.join(df['Review Text'])

words = all_reviews.split()
word_counts = Counter(words)

best_keywords = word_counts.most_common(10)
worst_keywords = word_counts.most_common()[:-11:-1] 

print("Best Keywords:", best_keywords)
print("Worst Keywords:", worst_keywords)