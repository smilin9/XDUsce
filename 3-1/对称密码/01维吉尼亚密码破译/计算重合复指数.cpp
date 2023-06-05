// created by: smilin9
// time: 2022-12-03 18:46:16

#include <stdio.h>
#include <string.h>
void GetMIc(char *string1, char *string2, int length1, int length2)
{ //计算MIc
	int letter[26] = {0};
	int i = 0;
	for (i = 0; i < 26; i++)
		letter[i] = i + 97;
	i = 0;
	while (i < 26)
	{
		int Mul_fifj = 0;
		int sum = 0;
		float MIc = 0;
		int j = 0;
		while (j < 26)
		{
			int fi = 0, fj = 0;
			for (int k = 0; k < length1; k++)
				if (*(string1 + k) == letter[j])
					fi++;
			for (int k = 0; k < length2; k++)
				if (*(string2 + k) == letter[(j - i + 26) % 26])
					fj++;
			Mul_fifj = fi * fj;
			sum = sum + Mul_fifj;
			j++;
		}
		MIc = sum * 1.0 / (length1 * length2);
		if (MIc - 0.065 < 0.015 && MIc - 0.065 > -0.015)
		{
			printf("%d ", i);
			break;
		}
		i++;
	}
}
void DevideAndGetOffSet(char *string, int d, int length)
{
	char a[100][1000];
	int len[100];
	int i, j;
	int c = 0;
	for (i = 0; i < d; i++)
	{
		int k = 0;
		for (j = c; j < length; j = j + d)
		{
			a[i][k] = *(string + j);
			k++;
		}
		len[i] = k;
		c++;
	}
	for (i = 0; i < d; i++)
		for (j = i + 1; j < d; j++)
			GetMIc(a[i], a[j], len[i], len[j]);
}
int main()
{
	char Ciphertext[1000];
	printf("请输入密文：");
	gets(Ciphertext);
	int len = strlen(Ciphertext);
	DevideAndGetOffSet(Ciphertext, 5, len);
	return 0;
}