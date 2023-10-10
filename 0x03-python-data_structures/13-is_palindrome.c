#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t *exchange_list(listint_t **tails);
int is_palindrome(listint_t **head);
/**
 * exchange_list - Reverses a linked list and updates the tail pointers.
 * @tails: A pointer to a pointer to the tail of the original list.
 * Return: A pointer to the head of the reversed list.
 */
listint_t *exchange_list(listint_t **tails)
{
	listint_t *prev = NULL;
	listint_t *next;
	listint_t *node = *tails;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*tails = prev;
	return (*tails);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to a pointer to the head of the linked list.
 * Return: 1 if the list is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp, *rev, *mid;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	tmp = *head;
	while (tmp)
	{
		size++;
		tmp = tmp->next;
	}

	tmp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		tmp = tmp->next;

	if ((size % 2) == 0 && tmp->n != tmp->next->n)
		return (0);

	tmp = tmp->next->next;
	rev = exchange_list(&tmp);
	mid = rev;

	tmp = *head;
	while (rev)
	{
		if (tmp->n != rev->n)
			return (0);
		tmp = tmp->next;
		rev = rev->next;
	}
	exchange_list(&mid);

	return (1);
}


