#include<bits/stdc++.h>
#include <iostream> 
#include <list> 
#include <iterator> 
#include <set>
#define int long long int
#define rdj ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);

using namespace std;

signed main()
{
    rdj
    int t,x=0;
    cin>>t;
    while(t--)
    {
        x++;
        int n;
        cin>>n;
        int m[n][n],m_t[n][n],i,j,r=0,c=0,k=0;
        list <int> lalista;
        for(i=0;i<n;i++)
        {   
            for(j=0;j<n;j++)
            {
                cin>>m[i][j];
                m_t[j][i]=m[i][j];
               
                if(i==j){
                    k+=m[i][j];
                }
            }      
        }
        
            for(i=0;i<n;i++){
                list <int> lalista1;
                list <int> lalista2;         
            for(j=0;j<n;j++){
                lalista1.push_back(m[i][j]);
                lalista2.push_back(m_t[i][j]);
               
                }
       

            int aux=0;
            
            lalista1.unique();
            lalista2.unique();

            if (lalista1.size()!=n){
            r=r+1;    
            }

            if (lalista2.size()!=n){
            c=c+1;    
            }
            }

         cout<<"Case #"<<x<<": "<<k<<" "<<r<<" "<<c<<endl;

        }
       return 0;
    }
    
