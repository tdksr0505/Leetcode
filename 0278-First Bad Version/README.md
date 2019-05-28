<h1>278. First Bad Version</h1>

<h3>題目:</h3>
每一個version都是基於前一個version所開發，所以當有一個version是bad version時，後面的都會是bad version，
題目給n個version，利用isBadVersion(version)來找出第一個bad version。<br>
ps: 盡可能減少呼叫isBadVersion()的次數。<br>
<h3>Solution:</h3>
若直接從頭找到尾會TLE，因此用二元搜尋法。
