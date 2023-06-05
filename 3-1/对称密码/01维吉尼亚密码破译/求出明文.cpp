// created by: smilin9
// time: 2022-12-03 18:46:16

#include <stdio.h>
#include <string.h>
int main()
{
	char Ciphertext[1000];
	char Plaintext[1000];
	int letter[26] = {0};
	printf("请输入密文：");
	gets(Ciphertext);
	int i, j, k = 0;
	int len = strlen(Ciphertext);
	for (i = 0; i < 26; i++)
	{
		letter[i] = i + 97;
	}
	while (k < 26)
	{
		for (i = 0; i < len; i = i + 5)
			for (j = 0; j < 26; j++)
				if (Ciphertext[i] == letter[j])
					Plaintext[i] = letter[(j + 26 - k) % 26];
		for (i = 1; i < len; i = i + 5)
			for (j = 0; j < 26; j++)
				if (Ciphertext[i] == letter[j])
					Plaintext[i] = letter[(j + 26 - k + 11) % 26];
		for (i = 2; i < len; i = i + 5)
			for (j = 0; j < 26; j++)
				if (Ciphertext[i] == letter[j])
					Plaintext[i] = letter[(j + 26 - k + 4) % 26];
		for (i = 3; i < len; i = i + 5)
			for (j = 0; j < 26; j++)
				if (Ciphertext[i] == letter[j])
					Plaintext[i] = letter[(j + 26 - k + 13) % 26];
		for (i = 4; i < len; i = i + 5)
			for (j = 0; j < 26; j++)
				if (Ciphertext[i] == letter[j])
					Plaintext[i] = letter[(j + 26 - k + 9) % 26];
		printf("Key：%c%c%c%c%c\n", letter[k], letter[(k + 26 - 11) % 26], letter[(k + 26 - 4) % 26], letter[(k + 26 - 13) % 26], letter[(k + 26 - 9) % 26]);
		printf("明文为：");
		for (i = 0; i < len; i++)
			printf("%c", Plaintext[i]);
		printf("\n");
		printf("\n");
		k++;
	}
	return 0;
}