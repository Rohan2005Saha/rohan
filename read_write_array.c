#include<stdio.h>
int main()
{
    int a[50],i,n;
    printf("Enter the no of elements :");
    scanf("%d",&n);
    printf("Enter the elements  of array :");
    for (i=0;i<=n-1;i++)
    {
      scanf("%d",&a[i]);
    }
    printf("The array is :");
    for(i=0;i<=n-1;i++)
    {
      printf("%d ",a[i]);
    }
}