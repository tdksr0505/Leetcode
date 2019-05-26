<h1> 100. Same Tree</h1>

<h3>題目:</h3>
製作一個有getMin()方法的stack<br>
<h3>Solution:</h3>
此題目重點在getMin。我有寫兩個版本，一個是用Array來做，一個是直接用Stack。<br>
<h4>Array 版本</h4>
本來是想直接定義一個int mi，若push進來的值小於min，則此值等於min。後來發現若是min被pop掉，那min就會換人當。
所以Array 版本的getMin()我是直接用迴圈讓他找，不過這樣的作法時間上似乎有點慢。
<br>
<h4>Stack 版本</h4>
Stack版本的getMin()我是直接把stack轉成array，在排序過後直接回傳最小值。但這樣比上面的array版本還花時間，後來發現可以在另外創一個stack專門
放最小值，若是剛好min被pop掉的話，專門放最小值的stack也跟著pop，這樣在呼叫getMin()的時候，就可以直接回傳最小值stack的peek。

