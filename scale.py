import cv2  

img = cv2.imread("C:\\Users\\vigne\\OneDrive\\Desktop\\explor\\flower.png")      # image load
if img is not None:
    grey = cv2.cvtColor(img, cv2.COLOR_BAYER_BG2RGB)  # convert to grayscale
    cv2.imshow("window display", grey)      # image show
    cv2.waitKey(0)                # wait for key press
    cv2.destroyAllWindows()  
    cv2.imwrite("tittle.png", grey)  # save the grayscale image
else: 
    print("Failed to load image.")
