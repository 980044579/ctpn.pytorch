import cv2

img = cv2.imread('./detection_test/202916101_00963.jpg')
print(img.shape)

# 383.5 415.5 399.5 463.5.
cv2.line(img,(384,416),(400,464),255)
# 528,918;863,88
cv2.imwrite('./ttest.jpg', img)


# gtbox = []
# with open("./testlabel.txt") as f:
#     for line in f.readlines():
#         cont = line.strip('\n').split('\t')
#         #self.img_names.append(cont[0])
#         tmp = []
#         for i in range(1, len(cont),2):
#             # for (x,y,w,h) format
#             point1, point2 = cont[i].split(';')
#             x1 = int(point1.split(',')[0])
#             y1 = int(point1.split(',')[1])
#             w = int(point2.split(',')[0])
#             h = int(point2.split(',')[1])

#             for i in range(0,w,16):
#                 tmp.append([x1+i, y1, x1+i+16, h+y1])
#         gtbox.append(tmp)    

# print(gtbox[0])
                    