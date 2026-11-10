import cv2

img = cv2.imread("C:\\Users\\vigne\\OneDrive\\Desktop\\explor\\flower.png")      # image load
if img is not None:
    cv2.imshow("window display", img)      # image show
    cv2.waitKey(0)                # wait for key press
    cv2.destroyAllWindows()       # close window
else: 
    print("Failed to load image.")

print("Image shape:", img.shape)  # print image shape