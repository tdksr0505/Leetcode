# 26. Remove Duplicates from Sorted Array

<h3>題目:</h3>
給一個數字陣列，陣列內容都是雙雙成對和一個單獨數字，回傳那一個單獨數字。
<h3>Solution:</h3>
一開始想法是先sort陣列再找出那個單獨數字，但sort會花費太多時間。後來參考別人寫法是直接用xor。陣列全部xor完之後，最後的值就是單獨的數字，
