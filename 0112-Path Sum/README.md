<h1> 112. Path Sum</h1>

<h3>題目:</h3>
給一個二元樹的root，跟一個sum，判斷是否有一條root到leaf的路徑總和剛好等於sum<br>
Note : leaf為沒有children的node<br>
<h3>Solution:</h3>
利用遞迴來解，如果sum剛好等於此節點的值，又剛好是leaf，就回傳true。<br>
否則就繼續往左右節點繼續走。
