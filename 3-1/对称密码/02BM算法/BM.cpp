// created by: smilin9
// time: 2022-12-03 18:46:16

#include <memory.h>
#include <stdio.h>
#define max 100
int next(int i, int a[], int f[])
{
    if (i == 0)
        return a[i];
    else
    {
        int d = a[i], j;
        j = 1;
        while (j <= i)
        {
            d = d ^ (f[j] * a[i - j]);
            j++;
        }
        return d;
    }
}
int main()
{
    int n, a[max], i, j, q, l = 0, m = -1, d;
    int t[max] = {0}, f[max] = {0}, b[max] = {0};
    t[0] = 1;
    f[0] = 1;
    b[0] = 1;
    printf("输入的n为:\n");
    scanf("%d", &n);
    printf("输入的n长序列为:\n");
    for (i = 0; i < n; i++)
        scanf("%d", &a[i]);
    for (i = 0; i < n; i++)
    {
        d = next(i, a, f);
        if (d == 1)
        {
            for (q = 0; q <= n; q++) // t<-f
                t[q] = f[q];
            for (j = 0; j <= n; j++)
                if (b[j] == 1)
                    f[j + i - m] = (f[j + i - m] + 1) % 2;
            if (l <= i / 2)
            {
                l = i + 1 - l;
                m = i;
                for (q = 0; q <= n; q++) // b<-t
                    b[q] = t[q];
            }
        }
    }
    printf("%d", f[0]);
    for (i = 1; i <= n; i++)
        if (f[i] != 0)
            printf("+x^%d", i);
    printf("\n");
    return 0;
}
