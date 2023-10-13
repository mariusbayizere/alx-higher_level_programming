#include "lists.h"

/**
 * insert_dnodeint_at_index - Inserts a new node at a specified index in a doubly linked list.
 * @h: A pointer to a pointer to the head of the doubly linked list.
 * @idx: The index at which to insert the new node (0-based).
 * @n: The integer value to be stored in the new node.
 * Return: A pointer to the newly inserted node.
 */
dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
	dlistint_t *tail = *h, *after;
	unsigned int show, sum = 0;
	
	after = malloc(sizeof(dlistint_t));
	if (after == NULL)
		return (NULL);
	after->n = n;
	if (idx == 0)
	{
		after->prev = NULL;
		after->next = *h;
		if (*h)
			(*h)->prev = after;
		*h = after;
		return (*h);
	}

	show = idx - 1;
	while (tail && sum != show)
	{
		sum++;
		tail = tail->next;
	}
	if (sum == show && tail)
	{
		after->prev = tail;
		after->next = tail->next;
		if (tail->next)
			tail->next->prev = after;
		tail->next = after;
		return (after);
	}
	free(after);
	return (NULL);
}
