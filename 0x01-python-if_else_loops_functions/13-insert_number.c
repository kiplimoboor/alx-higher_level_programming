#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a node in a sorted list
 *
 * @head: the liked list
 * @number: data of the node
 *
 * Return: new node, NULL if failed
 */


listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *temp = *head;

	if (!new || !head)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (!head || number < (*head)->n)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		while (temp->next && temp->next->n < number)
			temp = temp->next;
		new->next = temp->next;
		temp->next = new;
	}
	return (new);
}
