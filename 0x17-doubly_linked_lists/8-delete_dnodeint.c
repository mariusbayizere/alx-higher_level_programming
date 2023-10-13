#include "lists.h"

/**
 * delete_dnodeint_at_index - Deletes a node at a specified index in a doubly linked list.
 * @head: A pointer to a pointer to the head of the doubly linked list.
 * @index: The index of the node to be deleted (0-based).
 * Return: 1 if the node was successfully deleted.
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *temp = *head;
	dlistint_t *tail = *head;
	unsigned int args;
	unsigned int demo = 0;
	
	if (!(*head))
		return (-1);
	if (index == 0)
	{
		*head = tail->next;
		free(tail);
		if (*head)
			(*head)->prev = NULL;
		return (1);
	}
	args = index - 1;
	while (temp && demo != args)
	{
		demo++;
		temp = temp->next;
	}
	if (demo == args && temp)
	{
		tail = temp->next;
		if (tail->next)
		tail->next->prev = temp;
		temp->next = tail->next;
		free(tail);
		return (1);
	}

	return (-1);
}
