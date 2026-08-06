 

### 字串迴圈
- **傳統寫法:**  for (int i=0; i < s.size();i++){}  <br> 太繁瑣了
- **更改寫法:** for (char c : s){...} 

#### e.g. 
```
    for(char c : line){
        
        std::cout << c;
    }
```


### 數字反轉
- **Note:**  只靠數學式
```
while(x > rever_num ){
    rever_num = rever_num * 10  + (x % 10);
    x /= 10;     
}
```