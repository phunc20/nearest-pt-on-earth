# Origin
There is this user **Clark Chen** who posted an interesting question on Python Taiwan, a Facebook group:

抱歉想請教更有效率的寫法。
假設我有10000個地點（10000個經緯度座標），我想要找出「每一個地點離他最近的地點」，並取出這個最短距離。
我目前只能想到用兩個套在一起的迴圈，裡面的迴圈用geopy算某一個地點自己和其他所有地點的距離，取出最小值，然後外面的迴圈重複10000次算所有的點。但試跑了一下覺得執行好久，而且總覺得資源吃超凶怕crash...
想請問有經驗的大大們不知道有沒有更有效率的做法？或是給我幾個關鍵字讓我自己去搜尋也可以。
先行謝過，感激不盡～

## Proposed Solutions
Other people have suggested:
01. [`rtree`](https://gis.stackexchange.com/questions/22082/how-can-i-use-r-tree-to-find-points-within-a-distance-in-spatialite)
02. kdtree (e.g. from [`scipy.spatial`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.KDTree.html))
03. [geoSearch (mongoDB)](https://docs.mongodb.com/manual/reference/command/geoSearch/)
04. [quad tree](http://homepage.divms.uiowa.edu/~kvaradar/sp2012/daa/ann.pdf)

## Misunderstanding
At first I did not read carefully, misunderstanding that the distance concerned was Euclidean distance (instead of geodesic on an ellipsoid/sphere). But this misunderstood question has its own merit:
> Prove or disprove that on 2D, manhanttan distance **gives the same order** of distance pairs as Euclidean distance. That is, given points $A, B, C$, we have $d_{2}(A,C) > d_{2}(A,B) \iff d_{1}(A,C) > d_{1}(A,B)$, where $d_{1}, d_{2}$ denotes the Manhattan and Euclidean distances, respectively. A stronger statement to prove would be $\lVert\mathbf{x}\rVert_{2} > \lVert\mathbf{y}\rVert_{2} \iff \lVert\mathbf{x}\rVert_{1} > \lVert\mathbf{y}\rVert_{1}\quad\forall\; \mathbf{a}, \mathbf{b} \in \mathbb{R}^{2}.$ Moreover, if this is provable, extend the proof to $\mathbb{R}^{n}$ and **arbitrary _equivalent_ pair of norms**.

**Proof.**<br>
We shall use (without proving) a basic and famous theorem about **finite-dimensional normed vector space**. That is, in such a space, all norms are **_equivalent_**. (Recall that two norms $`\lVert\cdot\rVert_{1}, \lVert\cdot\rVert_{2}`$ on a vector space $`V`$ are said to be **_equivalent_** if $`\exists\, a, b > 0\;`$ s.t. $`\;a\lVert\mathbf{x}\rVert_{1} < \lVert\mathbf{x}\rVert_{2} < b\lVert\mathbf{x}\rVert_{1}\quad \forall\; \mathbf{x} \in V.\,`$)



