import os
import numpy as np
import matplotlib.pyplot as plt

#
# # 2. Dyskretyzacja
#
# f = 10
# fs = [20, 21, 30, 45, 50, 100, 150, 200, 250, 1000]
#
# for i in range(len(fs)):
# 	t = np.arange(0, 1, 1/fs[i])
# 	plt.plot(t, np.sin(2*np.pi*f*t))
# 	plt.show()
#
# print("Twierdzenia Kotielnikowa-Shannona")
#
#
# # 3. Kwantyzacja
#
# fotka = plt.imread(os.path.join(os.path.dirname(__file__), 'image.png'))
# fotka1 = fotka
# fotka2 = fotka1
# fotka3 = fotka1
#
# print(np.ndim(fotka1))
# print(np.shape(fotka1))
#
# for i in fotka1:
# 	for j in i:
# 		jas = (np.max(j) + np.min(j) / 2)
# 		j[0] = jas
# 		j[1] = jas
# 		j[2] = jas
#
# plt.imshow(fotka1)
# plt.show()
#
# for i in fotka2:
# 	for j in i:
# 		j = (j[0] + j[1] + j[2]) / 3
#
# plt.imshow(fotka2)
# plt.show()
#
# for i in fotka3:
# 	for j in i:
# 		j = j[0] * 0.21 + j[1] * 0.72 + j[2] * 0.07
#
# plt.imshow(fotka3)
# plt.show()
#
# n, bin, patches = plt.hist(fotka[:,:,0].ravel(), bins=256)
# plt.show()
#
# n, bin, patches = plt.hist(fotka1[:,:,0].ravel(), bins=16)
# plt.show()
#
# n, bin, patches = plt.hist(fotka2[:,:,0].ravel(), bins=16)
# plt.show()
#
# n, bin, patches = plt.hist(fotka3[:,:,0].ravel(), bins=16)
# plt.show()


# 4. Binaryzacja

foteczka = plt.imread('gradient.jpg')
plt.imshow(foteczka)
plt.show()
for i in foteczka:
    for j in i:
        jas = (np.max(j)+np.min(j))/2
        j[0] = j[1] = j[2] = jas
plt.imshow(foteczka)
plt.show()
n,bin,patches=plt.hist(foteczka[:,:,0].ravel(),bins=256)
plt.show()
for i in foteczka:
    for j in i:
        jas = (np.max(j)+np.min(j))/2
        if jas < 0.8:
            jas = 0
        else:
            jas = 1
        j[0] = j[1] = j[2] = jas
plt.imshow(foteczka)
plt.show()