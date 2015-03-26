/*
Reads in a character (not whitespace) from std in one at a time via scanf and appends the character
to a memory location (which is to be interpreted as a string). Each time a character is read in
(whether it is appended or not) the string is printed to output. When the string has maxed out
a call to realloc is made and the string size is doubled.

*/


#include <stdio.h>
#include <stdlib.h>
#include <string.h>


char * resize_string_array(char * current_buffer, int old_length, int new_length);
int my_strlen(char *s);

int main()
{
	int max_len = 4;
	char *str_start = (char *) malloc((size_t) (sizeof(char) * max_len + 1));
	str_start[max_len] = '\0';
	
	
	char current_character;
	int str_index = 0; // points to last element in the string
	while(1)
	{
		scanf("%c", &current_character);
		if (strlen(str_start) == max_len)
		{
			resize_string_array(str_start, max_len, max_len * 2);
			max_len = max_len * 2;
		}
		
		if (str_index == 0 && strlen(str_start) == 0 && !isspace(current_character))
		{
			str_start[0] = current_character;
		}
		else if (current_character != '\n')
		{
			str_start[++str_index] = current_character;
		}
		
		printf("%s", str_start);
		printf("\n");
	}
	
	return 0;
}

char * resize_string_array(char * current_buffer, int old_length, int new_length)
{
	char * new_address;
	new_address = (char *) realloc(current_buffer, (size_t) new_length);
	new_address[new_length] = '\0';
	return new_address;
}

int my_strlen(char *s){
	int n;
	for (n = 0; *s != '\0'; s++)
		n++;
	return n;
}