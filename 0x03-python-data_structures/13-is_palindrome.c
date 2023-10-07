#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - checks if linked list is palindrome
 *
 * @head: the linked list
 *
 * Return: (1) if it is, (0) if it isn't
 */

int is_palindrome(listint_t **head)
{
    int i = 0, j = 0;
    int *items;
    listint_t *temp = *head;

    while (temp)
    {
        temp = temp->next;
        i++;
    }

    items = malloc(sizeof(int) * i);
    temp = *head;
    i = 0;

    while (temp)
    {
        items[i] = temp->n;
        temp = temp->next;
        i++;
    }

    i--;

    while (j <= i)
    {
        if (items[j] != items[i])
        {
            return (0);
        }
        j++;
        i--;
    }

    free(items);
    return (1);
}
