#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle
 * @list: a pointer to the head of the linked list
 * Return:
 * 1 if a cycle is detected, 0 otherwise.
 */
int check_cycle(listint_t *list)
{
	listint_t *burlnely = list;
	listint_t *sleep = list;

	if (!list)
		return (0);

	while (burlnely && sleep && sleep->next)
	{
		burlnely = burlnely->next;
		sleep = sleep->next->next;
		if (burlnely == sleep)
			return (1);
	}

	return (0);
}
