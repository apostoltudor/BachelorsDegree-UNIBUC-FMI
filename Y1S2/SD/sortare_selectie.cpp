#include <iostream>

enum TipSortare{
    SORT_ASC,
    SORT_DESC,
    SORT_NUM
}

int ComparatorCrescator (const void *a, const void *b)
{

}

void SortareSelectie(void *arr, int n, size_t size, int (*cmp)(const void *a, const void *b))
{

}

void AfisareVector(int *v, int n)
{
    printf("Vectorul: ")
    for(int i = 0; i < n; i++)
    {
        printf("%d", v[i])
    }
    printf("\n---\n");
}

int main()
{
    int v[]={3,8,0,2,7,1,6,5,4};
    int n = sizeof(v)/sizeof(v[0]);

    //afisare inainte de sortare
    AfisareVector(v,n);

    //sortare vector
    int tipsortareInt;
    while (true)
    {    
        std::cout<<"introduceti tipul sortarii:\n[0] - ascendent\n[1] - descendent\n";
        std::cin>> tipsortareInt;
        if()
    }
    
    SortareSelectie(v,n, sizeof(v[0]), ComparatorCrescator)

    return 0;


}