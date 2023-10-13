#include "lists.h"

/**
 * add_dnodeint_end - Adds a new node at the end of a doubly linked list.
 *
 * @head: A pointer to a pointer to the head of the doubly linked list.
 * @n: The integer value to be stored in the new node.
 * Return: A pointer to the newly added node.
 */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *temp, *ptr = *head;

	temp = malloc(sizeof(dlistint_t));
	if (temp == NULL)
		return (NULL);
	temp->n = n;
	temp->next = NULL;

	if (ptr)
	{
		while (ptr->next)
			ptr = ptr->next;
		temp->prev = ptr;
		ptr->next = temp;
	}
	else
	{
		*head = temp;
		temp->prev = NULL;
	}

	return (temp);
}
