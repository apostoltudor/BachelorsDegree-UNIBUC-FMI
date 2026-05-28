//ex 1

//#include <iostream>
//#include <stack>
//using namespace std;
//
//int main()
//{
//    int n, v[100005], st[10005], dr[10005];
//    stack<int> w;
//    cin>>n;
//    for(int i=1;i<=n;i++)
//    {
//        cin>>v[i];
//        dr[i]=n+1;
//        while(!w.empty() and v[w.top()]<v[i])
//        {
//            dr[w.top()]=i;
//            w.pop();
//        }
//        if(!w.empty())
//            st[i]=w.top();
//        w.push(i);
//    }
//
//    return 0;
//}

//ex 2

#include <iostream>
#include<stack>
using namespace std;

int merge(int i, int j)
{
    int mij;
    if(i>=j)
        mij=(i+j)/2;
    return mij;
}

int main()
{
    int n;
    cin>>n;
    int v1[n+1], v2[n+1],rez[n+1];
    for(int i=1;i<=n/2;i++)
    {
        cin>>v1[i];
    }
    for(int i=n/2+1;i<=n;i++)
    {
        cin>>v2[i-n/2];
    }
    stack<int>stack;

    //sortez cei 2 vectori

    int i=1,j=1,nr=1;

    while(nr<=n)
    {
        if(v1[i]<=v2[j])
        {
            rez[nr]=v1[i];
            i++;
        }
        else
        {
            rez[nr]=v2[j];
            j++;
        }
        nr++;
    }

    for(int q=1;q<=n;q++)
        cout<<rez[q]<<" ";


    return 0;
}