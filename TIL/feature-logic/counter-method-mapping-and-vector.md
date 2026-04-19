* [Problem Link](https://www.codeabbey.com/index/task_view/array-counters)
 
note: 這題解的時候想太多，提交後發現好像用不到雜湊，有點過渡了。<br> 主要重點，容器空間要分配；hash表的C++語法，只要判斷有沒有在就好，不是像python用 `==`去做比較容器與元素。

```
#include <iostream>
#include <unordered_set>
#include <vector>

int main(){
    int total ;
    int total_element_in_array;
    std::cin >> total ;
    std::cin >> total_element_in_array;
    //用hash 表做
    std::unordered_set<int> hash_table ;
    
    for(int i = 1; i <= total_element_in_array ; ++i){
        
         hash_table.insert(i);
    }
    
    int element ;
    //儲存器
    std::vector<int> counter(total_element_in_array, 0) ;  //要分配vector空間，否則是空的，運行會溢出
    
    for(int i = 0; i < total;++i ){
        std::cin >> element ;
        if(hash_table.find(element)!= hash_table.end()){  // 這是C++20前的寫法，判斷是否元素在雜湊表內，C++20以後可以用 contains 方法 
            counter[element - 1] += 1;
        }
        
    }
    for(int i : counter){
        std::cout << i << " ";
    }




    
}
```