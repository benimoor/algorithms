#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

int *binary_search(int *lst, int lst_size, int x)
{
    int start = 0;
    int end = lst_size - 1;
    int mid;
    int n = 0;
    int *res = malloc(sizeof(int) * 2);
    while(start <= end)
    {
        n++;
        mid = (start + end) / 2;
        printf("==================\n");
        printf("lst[mid] is %d\nN is %d\n", lst[mid], n);
        if (lst[mid] == x)
        {
            res[0] = lst[mid];
            res[1] = n;
            return res;
        }
        else if (x > lst[mid])
            start = mid + 1;
        else if (x < lst[mid])
            end = mid - 1;
    }
    return NULL;
}

int main(int ac, char **av)
{
    int *lst = malloc(100 * sizeof(int));
    for (int i = 0; i < 100; i++)
        lst[i] = i;
    int *finded_lst = binary_search(lst, 100, atoi(av[1]));
    printf("==================\n");
    printf("The x is %d\nWalk Count is %d", finded_lst[0], finded_lst[1]);
    free(lst);
    free(finded_lst);
    return 0;
}
