There is this user **Clark Chen** who posted an interesting question on Python Taiwan:

抱歉想請教更有效率的寫法。
假設我有10000個地點（10000個經緯度座標），我想要找出「每一個地點離他最近的地點」，並取出這個最短距離。
我目前只能想到用兩個套在一起的迴圈，裡面的迴圈用geopy算某一個地點自己和其他所有地點的距離，取出最小值，然後外面的迴圈重複10000次算所有的點。但試跑了一下覺得執行好久，而且總覺得資源吃超凶怕crash...
想請問有經驗的大大們不知道有沒有更有效率的做法？或是給我幾個關鍵字讓我自己去搜尋也可以。
先行謝過，感激不盡～


Other people have suggested him:
01. [`rtree`](https://gis.stackexchange.com/questions/22082/how-can-i-use-r-tree-to-find-points-within-a-distance-in-spatialite)
02. kdtree (e.g. from `scipy.spatial`)
03. [geoSearch (mongoDB)](https://docs.mongodb.com/manual/reference/command/geoSearch/)
04. [quad tree](http://homepage.divms.uiowa.edu/~kvaradar/sp2012/daa/ann.pdf)

## Misunderstanding
At first I did read carefully, misunderstanding that the distance concerned was Euclidean distance (instead of geodesic on an ellipsoid). But this misunderstood question has its own merit:

> Prove that on 2D, manhanttan distance gives the same order as Euclidean distance.


