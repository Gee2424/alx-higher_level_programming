#include "lists.h"
#include <stdlib.h>

/**
* is_palindrome - checks if a singly linked list is a palindrome
* @head: double pointer to the head of the list
* Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
listint_t *current = *head;
int array[2048]; 
int i = 0, start = 0, end;

if (!head || !*head || !(*head)->next) 
return (1);

while (current != NULL)
{
array[i++] = current->n;
current = current->next;
}
end = i - 1;


while (start < end)
{
if (array[start] != array[end])
return (0);
start++;
end--;
}

return (1);
}
