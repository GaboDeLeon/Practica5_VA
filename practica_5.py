import cv2
import numpy as np

img = cv2.imread('libro.jpg',cv2.IMREAD_GRAYSCALE)

#threshold binary
retval_binary, threshold_binary = cv2.threshold(img,12,255, cv2.THRESH_BINARY)

#binary_inv
retval_binary_inv, threshold_binary_inv = cv2.threshold(img,12,255, cv2.THRESH_BINARY_INV)

#Trunc
retval_trunc, threshold_trunc = cv2.threshold(img,12,255,cv2.THRESH_TRUNC)

#To Zero
retval_tozero, threshold_tozero = cv2.threshold(img,12,255,cv2.THRESH_TOZERO)

#To Zero_inv
retval_tozero_inv, threshold_tozero_inv = cv2.threshold(img,12,255,cv2.THRESH_TOZERO_INV)

#Mean
mean = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,115,1)

#Gaus
gaus= cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

#otsu
retval_otsu,otsu = cv2.threshold(img,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('original',img)
cv2.imshow('threshold_binary', threshold_binary)
cv2.imshow('threshold_binary_inv', threshold_binary_inv)
cv2.imshow('threshold_trunc', threshold_trunc)
cv2.imshow('threshold_tozero', threshold_tozero)
cv2.imshow('threshold_tozero_inv', threshold_tozero_inv)
cv2.imshow('mean', mean)
cv2.imshow('gaus', gaus)
cv2.imshow('otsu', otsu)

cv2.waitKey(0)
cv2.destroyAllWindows()
