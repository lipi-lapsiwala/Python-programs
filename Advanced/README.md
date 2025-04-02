# Problem Statements

## 1. Maximum Vowel Substring

### Problem Statement
Given a string `s` and an integer `k`, determine the substring of length `k` that contains the maximum number of vowels (`a, e, i, o, u`). If multiple substrings have the same maximum vowel count, return the first one. If no vowels are found, return `Not Found!`.

### Constraints:
- `1 <= len(s) <= 2 * 10^5`
- `1 <= k <= len(s)`

### Example:
#### Input:
```plaintext
s = 'caberqiitefg'
k = 5
```
#### Output:
```plaintext
erqii
```

#### Explanation:
- The substrings of length `5` are: `caber`, `aberq`, `berqi`, `erqii`, `rqiit`, `qiite`, `iitef`, `itefg`.
- The substring `erqii` has the most vowels (`3`), so it is returned.

---

## 2. Parallel Processing

### Problem Statement
You are given a list of files that need to be executed on a computer with multiple cores. Each file has a certain number of lines of code, and the execution time of a file is equal to the number of lines it contains. If the number of lines in a file is **divisible** by the number of cores, the file can be executed **in parallel**, reducing its execution time to **(lines of code) / (number of cores)**. However, there is a **limit** on how many files can be executed in parallel at the same time.

Write a function to find the **minimum total execution time** required to execute all the files.

### Constraints:
- `1 <= n <= 10^5` (Number of files)
- `1 <= files[i] <= 10^9` (Lines of code in each file)
- `1 <= numCores <= 10^9` (Number of cores)
- `1 <= limit <= 10^9` (Parallel execution limit)

### Example:
#### Input:
```plaintext
files = [4, 1, 3, 2, 8] numCores = 4 limit = 1
```
#### Output:
```plaintext
12
```


#### Explanation:
- Files `[4, 8]` can be parallelized, but only **1 file** (limit) can be executed in parallel.
- We choose **8**, reducing its execution time to `8/4 = 2`.
- The remaining files are executed sequentially: `4 + 1 + 3 + 2 = 10`.
- **Total Execution Time = 12**.

This is a **greedy optimization problem** that requires **efficient selection of parallelizable files** to minimize total execution time.


