# SET 
# collection of elements, without duplicates, unordered

developers = {'A825662', 'A825663', 'A825664', 'A825665'}
testers = {'A825662', 'A825666', 'A825667', 'A825665'}
cloud_engineers = {'A825662', 'A825668', 'A825669', 'A825661'}

all_empl = developers.union(testers, cloud_engineers)
print(all_empl)

print(developers.intersection(testers))

print(developers)
# print(developers[0]) # This will raise an error because sets are unordered

developers.add('A825662')
print(developers)
developers.add('A789789')
print(developers)

print(testers.difference(developers))

print(developers.intersection(testers & cloud_engineers))

print(cloud_engineers - developers - testers)

