#include<iostream>
using namespace std;
#include<list>
#include<string>
#include<string.h>

int main(){
	char A[100];
	cout<<"Start"<<endl;
	cin>>A;
	if(!strcmp(A,"Begin")==0){
		cout<<"Syantactic Error"<<endl;
		exit(-1);
	}
	list <string> V1;
	int i=0;
	char B[10];
	while(!strcmp(B,"End")==0){
		cin>>B;
		V1.push_back(B);
		i++;
	}
	string C;
	C=V1.front();
	cout<<C;
	int size=C.size();
	cout<<size<<endl;
}

