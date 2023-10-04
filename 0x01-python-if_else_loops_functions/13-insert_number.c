#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a new node into a sorted linked
 * list
 *
 * @head: the linked list
 * @number: the data to the list
 *
 * Return: the newly inserted node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *temp;

	if (!new)
	{
		return (NULL);
	}

	new->n = number;
	new->next = NULL;

	if ((*head) == NULL || number < (*head)->n)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		temp = *head;
		while (temp->next && temp->next->n < number)
			temp = temp->next;
		new->next = temp->next;
		temp->next = new;
	}

	return (new);
}
