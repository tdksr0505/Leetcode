<h1>231. Power of Two</h1>

<h3>題目:</h3>
給一個數字n，判斷n是否為2的次方<br>

<h3>Solution:</h3>
將n一直除2，如果中間遇到n不能被2整除就return false<br>
如果一直除到n=2那就return true<br>
但如果n一開始就是1，也是return true
