# BinarySearch
Leetcode 26. Remove Duplicates from Sorted Array

雙指針，原本設想用雙指針從左右縮回，把匹配不對的數字丟到後面，左右側指針交互後跳出迴圈，但失敗了。

正確是，快慢指針，不管連續的數字，去抓不匹配的數字後，讓慢子真前進一步，然後替代


## Correct Solution
class Solution {
public:

    int removeDuplicates(vector<int>& nums) {
        int slowpi = 0;
        for(int quickpi =1 ; quickpi < nums.size(); ++quickpi ){
            if(nums[quickpi] != nums[slowpi]){
                slowpi++; //先前進
                nums[slowpi] = nums[quickpi];
            }
        }
        return slowpi+1; //慢指針+回來
    }
    
};

##  [x] Incorrect Solution
```
class Solution {
public:
    void exchange(vector<int>& nums,int left, int right){
        int pilot = right ;

        return swap(nums[left], nums[right]);
    }
    int iterator(vector<int>& nums,int left , int right){
        while(left != right){
            if (nums[left] == nums[left+1]){
                exchange(nums , left+1 , right);
                right --;
            }
            if(nums[left+1]>nums[left+2]){
                exchange(nums,left+1,left+2);
            }
        return right;
        }


    }
    int removeDuplicates(vector<int>& nums) {
        int right = nums.size();
        int left = 0 ;
        int k;
        k = iterator(nums , left , right-1);
    return k;
    }
    
};
```