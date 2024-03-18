#include "lists.h"

/**
* flip_list - Reverses the order of nodes in a linked list
* @head: Pointer to the first node in the list
*
* Return: Void
*/
void flip_list(listint_t **head)
{
listint_t *previous = NULL;
listint_t *current = *head;
listint_t *upcoming = NULL;

while (current)
{
upcoming = current->next;
current->next = previous;
previous = current;
current = upcoming;
}

*head = previous;
}

/**
* is_palindrome - Checks if a linked list is a palindrome
* @head: Double pointer to the linked list
*
* Return: 1 if it is, 0 if not
*/
int is_palindrome(listint_t **head)
{
listint_t *slow = *head, *fast = *head, *temp = *head, *copy = NULL;

if (*head == NULL || (*head)->next == NULL)
return (1);

while (1)
{
fast = fast->next->next;
if (!fast)
{
copy = slow->next;
break;
}
if (!fast->next)
{
copy = slow->next->next;
break;
}
slow = slow->next;
}

flip_list(&copy);

while (copy && temp)
{
if (temp->n == copy->n)
{
copy = copy->next;
temp = temp->next;
}
else
return (0);
}

if (!copy)
return (1);

return (0);
}
