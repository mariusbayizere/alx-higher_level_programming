#include "lists.h"

/**
 * dlistint_len - Counts the number of elements in a doubly linked list.
 * @h: A pointer to the head of the doubly linked list.
 * Return: The number of elements in the doubly linked list.
 */
size_t dlistint_len(const dlistint_t *h)
{
	const dlistint_t *head = h;
	size_t temp = 0;

	while (head)
	{
		temp++;
		head = head->next;
	}

	return (temp);
}
