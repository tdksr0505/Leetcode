<h1>724. Find Pivot Index</h1>

<h3>題目:</h3>
給一個數字陣列，找到一個index使得此index的左邊總和=右邊總和(若有多個index符合此條件，回傳最左邊的)<br>
若沒有這個index，則回傳-1

<h3>Solution:</h3>
<法1>
暴力解法，計算每個index的左右兩邊和<br>
<法2>
先全部相加得出sum。再定義一個sum2 = 0跑迴圈，讓原先的sum依序扣掉index的值看會不會等於第二次迴圈的sum2。


