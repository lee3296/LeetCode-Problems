/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* swapPairs(struct ListNode* head){
    
    struct ListNode* track = head;
    struct ListNode* prev = NULL;
    struct ListNode* curr = NULL;
    struct ListNode* swap = NULL;
    struct ListNode* prev_inc = NULL;
    int count = 0;
    
    if (head == NULL) {
        return NULL;
    }
    
    if (head->next == NULL) {
        return head;
    } else {
        head = head->next;
    }
    
    while (track->next != NULL) {
        
        prev = track;
        curr = track->next;
        
        if (track->next->next == NULL) {
            track = curr;
            track->next = prev;
            prev->next = NULL;
            if (prev_inc != NULL) {
                prev_inc->next = curr;
            }
            
            break;
        }
        
        
        swap = track->next->next;
        track = curr;
        track->next = prev;
        prev->next = swap;
        
        if (count != 0) {
            prev_inc->next = curr;
        }
        
        prev_inc = prev;
        
        
        
        track = swap;
        count++;
    }
    
    return head;
}
