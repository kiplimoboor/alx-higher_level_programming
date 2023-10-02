#include "lists.h"

/**
 * check_cycle - checks for cycle in list
 *
 * @list: list to be checked
 *
 * Return: (1) if there is cycle, (0) if there isn't
 */

int check_cycle(listint_t *list)
{
	listint_t *slowPointer = list;
	listint_t *fastPointer = list;

	if (list == NULL)
		return (0);

	while (slowPointer && fastPointer && fastPointer->next)
	{
		slowPointer = slowPointer->next;
		fastPointer = fastPointer->next->next;

		if (slowPointer == fastPointer)
			return (1);
	}

	return (0);
}
