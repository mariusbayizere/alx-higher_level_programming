#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - Inserts a new node with a given number into a sorted linked list.             
 * @head: A pointer to a pointer to the head of the linked list.
 * @number: The integer value to be insert into the list.
 * Return: A pointer to the newly created node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *genel;

	genel = malloc(sizeof(listint_t));
	if (genel == NULL)
		return (NULL);
	genel->n = number;
	if (node == NULL || node->n >= number)
	{
		genel->next = node;
		*head = genel;
		return (genel);
	}
	while (node && node->next && node->next->n < number)
		node = node->next;
	genel->next = node->next;
	node->next = genel;
	return (genel);
}
