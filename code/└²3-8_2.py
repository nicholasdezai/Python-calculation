from itertools import groupby

scores = [89, 70, 49, 87, 92, 84, 73, 71, 78, 81, 90, 37,
          77, 82, 81, 79, 80, 82, 75, 90, 54, 80, 70, 68, 61]
def classify(score):
    if score >= 90: return '优秀'
    elif score >= 80: return '良'
    elif score >= 70: return '中'
    elif score >= 60: return '及格'
    else: return '不及格'

##groups = {category:len(tuple(score))
##          for category, score in groupby(sorted(scores), classify)}
##print(groups)
for category, score in groupby(sorted(scores), classify):
    print(category, tuple(score))
