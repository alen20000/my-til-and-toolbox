# QuickSort

* [Problem Link](https://www.codeabbey.com/index/task_view/median-of-three)

TS:
O(n2)~ O(nlogn) ; Ave:O(nlogn)

SC:
O(n2)~ O(logn)  ; Pilot 選的不均，效果就不好

```
#include <iostream>
#include <vector>
#include <algorithm>
//傳餐進來的是位置(列序)
int partition(std::vector<int>& nums,int left, int right){
    int pilot = nums[right];
    int i = left-1;
    
    for (int j = left ; j < right; j++){
        if(nums[j] < pilot){
            i++;
            std::swap(nums[i],nums[j]);  
        }

    }
    std::swap(nums[i+1],nums[right]);
    
    //將中點給回去
    return i+1;
}

void SortArray(std::vector<int>& nums,int left, int right){
    // 兩邊等於就會退出
    if(left < right){
        int pi = partition(nums,left ,right);
        
        SortArray(nums, left, pi-1);
        SortArray(nums, pi+1, right);
        
    }
    
}



// print fuction
// void printNums(const std::vector<int>& nums){
//     for (int n : nums) std::cout<< n << ' ';
// }

int main(){
        int count;
        std::cin >> count;
        
        while(count--){
            
            std::vector<int> nums(3);
            std::cin >> nums[0];
            std::cin >> nums[1];
            std::cin >> nums[2];
            // array lenght
            int n = nums.size();
            
            SortArray(nums,0,n-1);
            
            std::cout<< nums[1] << ' ';
            
        }
    
    }


```