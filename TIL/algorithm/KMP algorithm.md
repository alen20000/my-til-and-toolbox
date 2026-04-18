# KMP algorithm
Leetcode 28. Find the Index of the First Occurrence in a String


KMP解法:於字串搜尋，遍歷過的元素，不會再重複。
```
class Solution {
public:
    vector<int> LSP(string needle){
        int m =needle.size();
        // build next 跳表，從0開始
        vector<int> next(m,0);
        int j = 0;  //這是來放匹配前綴的
        for(int i = 1 ; i < m ; i ++){ //i 拿來放後綴
            while(j > 0 && needle[i] != needle[j]){
                j = next[j-1];
            }
            if (needle[i] == needle [j]) {
                j ++ ;
            }
            next[i] = j;
        }

        return next;

    }

    int strStr(string haystack, string needle) {
        int m = haystack.size();
        int n = needle.size();
        //filter
        if(n>m) return -1;

        vector<int> next = LSP(needle);
        int j =0 ; //給j的指標

        for(int i=0; i < m ;i++){
            while(j > 0 && haystack[i] != needle[j] ){
                j = next[j-1];
            }
            if (haystack[i] == needle[j]){
                j++;
            }
            if (j == n){
                return i - n  + 1;
            }
        }
        return -1;
    }
};
```

原本的暴力解，但有優化一些，不知道為什麼成績也在T1。
```
class Solution {
public:
    int matching(string haystack, string needle,int i){
        int m = needle.size();
        for(int j = 0; j < m ; j++){
            if(haystack[i+j] !=needle[j]){
                return -1;
            }
            
        }
        return 0;
    }
    int strStr(string haystack, string needle) {
        
        int hay_len = haystack.size() ;
        int ne_len = needle.size();
        int mix_count = hay_len - ne_len + 1;
        int result;
        for(int i = 0 ; i <= mix_count ; ++i){
            if(haystack[i] == needle[0]){
                result = matching(haystack,needle,i);
            }
            if(result == 0) return i;
        }
        return -1;
    }
};
```