<img src="assets/magicleap.png" width="240">

### SuperPoint：
part1 paper Introduction
Full paper PDF: SuperPoint: Self-Supervised Interest Point Detection and Description
OpenCV python = 4.7.0
torch version = 2.0.1
matplotlib version = 3.7.1
numpy version = 1.24.3

part2 out experiments result
A. directory of images, such as .png or .jpg
B. video file, such as .mp4 or .avi
C. USB Webcam


part3 Match Point (Compare with SIFT)


### sift_demo 目前進度：
part1 

生出有綠線連接的組圖

目前在想如何把線變少點讓圖片清楚一點不會被全部遮掉
par2

前面部分砍掉，換程式用 

使用方法

在裝有cv2 matplotlib 套件下環境

進入terminal

cd 到SIFT資料夾內

輸入 python SIFT_feature_matching.py DJI_0060.jpg DJI_0062.jpg

part 2

學校部分matching結果 (在sift 資料夾內)

有修改code 提高 good matching的門檻 讓線可以少一點

在Spyder console內執行輸入指令

ex：

run SIFT_feature_matching.py assets/6-1.jpg assets/6-2.jpg

輸出：

b

A

C:\Users\lang\Desktop\SuperPointPretrainedNetwork-master\DEMO\SIFT\SIFT_feature_matching.py:65: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
  plt.imshow(img3), plt.show()
  - good matches: 301
  - total features: 22321
  - percentage: 0.0135
0.01
----------------------------
配對其他圖的指令

m.distance < 0.3*n.distance

run SIFT_feature_matching.py assets/1-1.jpg assets/1-2.jpg

m.distance < 0.3*n.distance

run SIFT_feature_matching.py assets/3-1.jpg assets/3-4.jpg

m.distance < 0.3*n.distance

run SIFT_feature_matching.py assets/4-1.jpg assets/4-3.jpg

m.distance < 0.7*n.distance

run SIFT_feature_matching.py assets/5-1.jpg assets/5-2.jpg

m.distance < 0.3*n.distance

run SIFT_feature_matching.py assets/6-1.jpg assets/6-2.jpg
