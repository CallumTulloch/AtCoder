"""問題
正整数 
A,B が与えられます。

あなたは、
A=B になるまで以下の操作を繰り返します。

A,B の大小関係に応じて、次の 
2 個のうちどちらかの処理を行う。
A>B ならば、
A を 
A−B で置き換える。
A<B ならば、
B を 
B−A で置き換える。
"""

#include<bits/stdc++.h>
using namespace std;
int main() {
  long long a,b;
  cin>>a>>b;
  long long ans=0;
  if(a<b) swap(a,b);
  while(b>0){
    ans+=a/b;
    a%=b;
    swap(a,b);
  }
  cout<<ans-1<<endl;
}