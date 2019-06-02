<h1>389. Find the Difference</h1>

<h3>題目:</h3>
給兩個字串s,t。<br>
t字串為s字串內容打亂之後再隨機位子新增一個字元<br>
回傳那個新增的字元<br>
<h3>Solution:</h3>
<法1><br>
找出那個字元的index，使用substring相加的方式來移除此字元。<br>
<法2><br>
先將t轉成StringBuilder類型，可以使用deleteCharAt()來刪除字元。<br><br>

substring相加會花費較久時間


