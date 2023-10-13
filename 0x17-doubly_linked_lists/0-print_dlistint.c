#include "lists.h"

/**
 * print_dlistint - Prints all elements of a doubly linked list.
 * @h: A pointer to the head of the doubly linked list.
 * Return: The number of elements in the doubly linked list.
 */
size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *head = h;
	size_t temp = 0;

	while (head)
	{
		printf("%i\n", head->n);
		temp++;
		head = head->next;
	}

	return (temp);
}
