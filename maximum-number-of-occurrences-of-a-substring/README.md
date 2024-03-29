[Discussion Post (created on 18/3/2021 at 10:48)](https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/submissions/)  
<h2>1297. Maximum Number of Occurrences of a Substring</h2><h3>Medium</h3><hr><div><p>Given a string <code>s</code>, return the maximum number of ocurrences of <strong>any</strong> substring&nbsp;under the following rules:</p>

<ul>
	<li>The number of unique characters in the substring must be less than or equal to <code>maxLetters</code>.</li>
	<li>The substring size must be between <code>minSize</code> and <code>maxSize</code>&nbsp;inclusive.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
<strong>Output:</strong> 2
<strong>Explanation:</strong> Substring "aab" has 2 ocurrences in the original string.
It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> Substring "aaa" occur 2 times in the string. It can overlap.
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3
<strong>Output:</strong> 3
</pre>

<p><strong>Example 4:</strong></p>

<pre><strong>Input:</strong> s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10^5</code></li>
	<li><code>1 &lt;= maxLetters &lt;= 26</code></li>
	<li><code>1 &lt;= minSize &lt;= maxSize &lt;= min(26, s.length)</code></li>
	<li><code>s</code> only contains lowercase English letters.</li>
</ul></div>