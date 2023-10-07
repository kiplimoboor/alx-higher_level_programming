#include "lists.h"

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
    int items[50];
    listint_t *temp = *head;

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

    return (1);
}
