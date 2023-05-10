#include "lists.h"
#include <stdlib.h>

/**
 * insert_node: use two listint_t and number
 * @created - set its n field with number, and its next field to NULL after memory alocation
 * @mem - set temporal pointer and interate to fix @created
 * @formal - hold the memory of the head
 *
 * Return - @created
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *mem, *created, *formal = NULL;

	if (!head)
		return (NULL);

	created = malloc(sizeof(listint_t));
	if (!created)
		return (NULL);

	created->n = number;
	created->next = NULL;

	mem = *head;
	while (mem && created->n > mem->n)
	{
		formal = mem;
		mem = mem->next;
	}
	if (mem && created->n == mem->n)
	{
		created->next = mem;
		formal->next = created;
	}
	else if (!formal)
	{
		created->next = *head;
		*head = created;
	}
	else
	{
		created->next = formal->next;
		formal->next = created;
	}

	return (created);
}
