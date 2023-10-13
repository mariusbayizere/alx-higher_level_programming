#include "lists.h"

/**
 * sum_dlistint - Computes the sum of integer values in a doubly linked list.
 * @head: A pointer to head of the doubly linked list.
 * Return: The sum of integer values .
 */
int sum_dlistint(dlistint_t *head)
{
	int sum = 0;
	dlistint_t *temmp = head;

	while (temmp)
	{
		sum += temmp->n;
		temmp = temmp->next;
	}

	return (sum);
}
