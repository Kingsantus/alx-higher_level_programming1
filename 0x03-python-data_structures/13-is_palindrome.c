#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - checks if a singly-linked list is a palindrome
 *
 * @head: pointer to address of first node on the list
 * while loop tranverse the node using next and add 1
 * Return: 1 if list is a palindrome, otherwise 0
*/
int is_palindrome(listint_t **head)
{
	listint_t *ephem;
	int list_len = 0;

	if (!*head)
		return (1);

	ephem = *head;
	while (ephem)
	{
		list_len++;
		ephem = ephem->next;
	}
	if (list_len % 2 != 0)
		return (0);

	return (1);
}
