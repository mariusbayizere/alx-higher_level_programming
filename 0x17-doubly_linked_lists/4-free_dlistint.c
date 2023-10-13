#include "lists.h"

/**
 * free_dlistint - delete a dlistint_t list.
 * @head: pointer to the list.
 */
void free_dlistint(dlistint_t *head)
{
	dlistint_t *temp;
	dlistint_t *ptr;

	if (head)
	{
		temp = head;
		ptr = head->next;
		while (ptr)
		{
			free(temp);
			temp = ptr;
			ptr = ptr->next;
		}
		free(temp);
	}
}
