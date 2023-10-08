#include "lists.h"
#include <stdlib.h>

void reverse(listint_t **head);

/**
 * is_palindrome - checks if linked list is palindrome
 *
 * @head: the linked list
 *
 * Return: (1) if it is, (0) if it isn't
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;

	if (!(*head))
		return (1);

	while (fast->next && fast->next->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	slow = slow->next;
	fast = *head;

	reverse(&slow);

	while (slow)
	{
		if (slow->n != fast->n)
		{
			return (0);
		}
		slow = slow->next;
		fast = fast->next;
	}

	return (1);
}

/**
 * reverse - reverses a linked list
 *
 * @head: pointer to the list
 */

void reverse(listint_t **head)
{
	listint_t *previous = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = previous;
		previous = current;
		current = next;
	}

	*head = previous;
}
