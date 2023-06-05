// created by: smilin9
// time: 2022-12-03 18:46:16

#include <stdio.h>
#include <string.h>
float GetIc(char *string, int length)
{ // 计算Ic
	int letter[26];
	int letter_num[26] = {0};
	float Ic = 0;
	for (int i = 0; i < 26; i++)
	{
		int c = 0;
		letter[i] = i + 97;
		for (int j = 0; j < length; j++)
			if (letter[i] == *(string + j))
			{
				++c;
				letter_num[i] = c;
			}
	}
	for (int i = 0; i < 26; i++)
		Ic = Ic + (letter_num[i] * (letter_num[i] - 1)) * 1.0 / (length * (length - 1));
	return Ic;
}
void DevideAndGetIc(char *string, int d, int length)
{ // 分组并计算平均Ic
	char a[100][1000];
	int i, j;
	int c = 0;
	float sum = 0;
	for (i = 0; i < d; i++)
	{
		int k = 0;
		for (j = c; j < length; j = j + d)
		{
			a[i][k] = *(string + j);
			k++;
		}
		float s = GetIc(a[i], k);
		sum = sum + s;
		c++;
	}
	printf("d = %d avarage: %f\n", d, sum / d);
}
int main()
{
	char Ciphertext[1000];
	printf("请输入密文：");
	gets(Ciphertext);
	int len = strlen(Ciphertext);
	for (int i = 2; i < 10; i++)
		DevideAndGetIc(Ciphertext, i, len);
	return 0;
}
