/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        cout << "addTwoNumbers" << endl;

        int sum = l1->val + l2->val;
        int carry = sum / 10;
        sum = sum % 10;

        ListNode * head = new ListNode(sum);
        ListNode * currentNode = head;

        l1 = l1->next;
        l2 = l2->next;

        while (l1 != NULL || l2 != NULL || carry == 1) {
            int sum = 0;

            if (l1 == NULL && l2 != NULL)
            {
                sum = l2->val + carry;
                l2 = l2->next;
            }

            else if (l2 == NULL && l1 != NULL)
            {
                sum = l1->val + carry;
                l1 = l1->next;
            }

            else if (l1 != NULL && l2 != NULL)
            {
                sum = l1->val +l2->val + carry;
                l1 = l1->next;
                l2 = l2->next;
            }

            else
            {
                sum = carry;
            }

            if (sum >= 10)
            {
                sum %= 10;
                carry = 1;
            }

            else
            {
                carry = 0;
            }

            ListNode * newNode = new ListNode(sum);
            currentNode->next = newNode;
            currentNode = newNode;
        }

        return head;
    }
};
