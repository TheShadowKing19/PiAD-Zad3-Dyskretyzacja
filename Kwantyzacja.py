import numpy as np
import matplotlib.pyplot as plt

print("Wczytuje obrazek")
img = plt.imread('ikona.png')

print("Rozdzielczość/wymiar obrazka:")
print(np.shape(img))

print("Iloma wartościami jest opisywany pojedynczy piksel")
print(np.size(img[1, 1]))


fig, (gray1, gray2, gray3) = plt.subplots(3)
fig.tight_layout()

gray = np.zeros((len(img), len(img[0])))
# Wyznaczenie jasności piksela
print("\nWyznaczenie jasności piksela")
for x in range(0, len(img)):
    for y in range(0, len(img[0])):
        gray[x, y] = ((max(img[x, y, 0], img[x, y, 1], img[x, y, 2]) + min(img[x, y, 0], img[x, y, 1], img[x, y, 2])) / 2)
gray1.imshow(gray, cmap='gray')
gray1.set_title('Wyznaczenie jasności piksela')
hist1, bin_edges1 = np.histogram(gray)

# Uśrednienie wartości piksela
gray = (img[:, :, 0] + img[:, :, 1] + img[:, :, 2]) / 3
gray2.imshow(gray, cmap='gray')
gray2.set_title('Uśrednienie wartości piksela')
hist2, bin_edges2 = np.histogram(gray)

# Wyznaczenie luminacji piksela
gray = 0.21 * img[:, :, 0] + 0.72 * img[:, :, 1] + 0.07 * img[:, :, 2]
gray3.imshow(gray, cmap='gray')
gray3.set_title('Wyznaczenie luminacji piksela')
hist3, bin_edges3 = np.histogram(gray)
plt.show()


# Histogramy

