#include "lists.h"

/**
 * get_dnodeint_at_index - Gets the node at a specified index in a doubly linked list.
 *
 * @head: A pointer to the head of the doubly linked list.
 * @index: The index of the node to retrieve (0-based).
 * Return: A pointer to the node at the specified index.
 */
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	dlistint_t *ptr = head;
	unsigned int temp = 0;

	while (ptr && temp != index)
	{
		temp++;
		ptr = ptr->next;
	}
	if (ptr && temp == index)
		return (ptr);
	return (NULL);
}
