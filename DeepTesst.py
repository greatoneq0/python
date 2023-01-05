import numpy as np

# org_array = np.array([3,1,9,5])
# #sort_indices = np.argsort(org_array)
# sort_indices = np.argsort(org_array)[::-1]
# print(type(sort_indices))
# print('행렬 정렬 시 원본 행렬의 인덱스:', sort_indices)

name_array = np.array(['john', 'mike', 'sarah', 'kate', 'samuel'])
score_array = np.array([78, 95, 84, 98, 88])

sort_indices_asc = np.argsort(score_array)
print('성적 오름차순 정렬 시 score_array인덱스:', sort_indices_asc)
print('성적 오름차순으로 name_array의 이름 출력:', name_array[sort_indices_asc])