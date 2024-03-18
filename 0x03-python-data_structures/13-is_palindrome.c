#include "lists.h"

/**
* reverse_list - Reverses a singly linked list
* @head: Pointer to the head of the list
*
* Return: Pointer to the new head of the reversed list
*/
listint_t *reverse_list(listint_t **head)
{
listint_t *prev = NULL, *curr = *head, *next = NULL;

while (curr != NULL)
{
next = curr->next;
curr->next = prev;
prev = curr;
curr = next;
}

*head = prev;
return (*head);
}

/**
* is_palindrome - Checks if a singly linked list is a palindrome
* @head: Pointer to a pointer to the head of the list
*
* Return: 1 if the list is a palindrome, 0 otherwise
*/
int is_palindrome(listint_t **head)
{
listint_t *slow = *head, *fast = *head, *prev_slow = *head;
listint_t *second_half, *mid = NULL;
int is_palindrome = 1;

if (*head == NULL || (*head)->next == NULL)
return (1);

/* Find the middle node using the slow and fast pointers */
while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;
prev_slow = slow;
slow = slow->next;
}

/* If the list has an odd number of nodes, skip the middle node */
if (fast != NULL)
{
mid = slow;
slow = slow->next;
}

/* Reverse the second half of the list */
second_half = reverse_list(&slow);

/* Compare the first and second halves of the list */
while (second_half != NULL)
{
if (prev_slow->n != second_half->n)
{
is_palindrome = 0;
break;
}
prev_slow = prev_slow->next;
second_half = second_half->next;
}

/* Restore the original list by reversing the second half again */
reverse_list(&slow);

/* If there was a middle node, restore the next pointer of the node before the middle */
if (mid != NULL)
prev_slow->next = mid;

return (is_palindrome);
}
