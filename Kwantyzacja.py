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

gray_value1 = np.zeros((len(img), len(img[0])))
# Wyznaczenie jasności piksela
print("\nWyznaczenie jasności piksela")
for x in range(0, len(img)):
    for y in range(0, len(img[0])):
        gray_value1[x, y] = ((max(img[x, y, 0], img[x, y, 1], img[x, y, 2]) + min(img[x, y, 0], img[x, y, 1], img[x, y, 2])) / 2)
gray1.imshow(gray_value1, cmap='gray')
gray1.set_title('Wyznaczenie jasności piksela')
hist1, bin_edges1 = np.histogram(gray_value1)  # Histogram 1 (Zad 5)
print("Tablica histogramu dla wyznaczenia jasności piksela:\n", hist1, "\n")

# Uśrednienie wartości piksela
gray_value2 = (img[:, :, 0] + img[:, :, 1] + img[:, :, 2]) / 3
gray2.imshow(gray_value2, cmap='gray')
gray2.set_title('Uśrednienie wartości piksela')
hist2, bin_edges2 = np.histogram(gray_value2)  # Histogram 2 (Zad 5)
print("Tablica histogramu dla uśrednienia wartości piksela\n", hist2, "\n")

# Wyznaczenie luminacji piksela
gray_value3 = 0.21 * img[:, :, 0] + 0.72 * img[:, :, 1] + 0.07 * img[:, :, 2]
gray3.imshow(gray_value3, cmap='gray')
gray3.set_title('Wyznaczenie luminacji piksela')
hist3, bin_edges3 = np.histogram(gray_value3)  # Histogram 3 (Zad 5)
plt.show()
print("Tablica histogramu dla wyznaczenia luminacji piksela:\n", hist3)


# Histogramy
fig, (HisF1, HisF2, HisF3) = plt.subplots(3)
HisF1.set_title("Histogram - obrazek przekszałcony za pomocą wyznaczenia jasności piksela")
HisF1.hist(gray_value1.ravel(), bins=16)

HisF2.set_title("Histogram - obrazek przekszałcony za pomocą uśrednienia wartości piksela")
HisF2.hist(gray_value2.ravel(), bins=16)

HisF3.set_title("Histogram - obrazek przekszałcony za pomocą wyznaczenia luminacji piksela")
HisF3.hist(gray_value3.ravel(), bins=16)

fig.tight_layout()
plt.show()
