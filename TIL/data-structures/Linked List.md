# Linked List
Leetcode 2. Add Two Numbers


### Key Points
1. `->` 指向運算子，用於在結構中指向其結構體的成員，
`cur_1->val`等同`(*cur_1).val`，在鏈表中第二種寫法容易失誤且不值觀，所以用第一個
2. `ListNode* dummy = new ListNode(0);` 這個是虛擬頭節點，不這方法做的話，每次回圈都要先初始化head，然後才能串接，會很麻煩，還多了if判斷
3. 接第二點，return 時要 `dummy-> next` 才能把第一個虛擬頭拋棄

```
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:

    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* cur_1 = l1;
        ListNode* cur_2 = l2;

        //放結果的鏈
        ListNode* dummy = new ListNode(0);
        ListNode* temp_pointer = dummy;

        int carry = 0 ; //存進位

        while(cur_1!=nullptr || cur_2 != nullptr||carry !=0 ){

            int v1 = (cur_1 != nullptr) ? cur_1 -> val : 0; //利用三元運算子，快速指向或0
            int v2 = (cur_2 != nullptr) ? cur_2 -> val : 0;
    
            int sum = v1 + v2 + carry; // 這邊先存著，因為要算進位

        
            carry = sum / 10 ; //進位
            int digit =  sum % 10 ;  //這次要寫入鏈的

            temp_pointer->next = new ListNode(digit); //再創鏈
            temp_pointer = temp_pointer -> next;      //移動到下一個鏈

            if (cur_1 != nullptr) cur_1 = cur_1 -> next;; //為安全移動，要這樣寫
            if (cur_2 != nullptr) cur_2 = cur_2 -> next;;

        }

        return dummy-> next;
    }
};
```