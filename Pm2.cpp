#include<iostream>
using namespace std;
#include<vector>
#include<string>
#include<string.h>

char var[7]={'A','B','C'};
char sign[3]={'+','-'};

int main(){
	char A[100];
	cout<<"WhenEver You complete and wanna check press 1"<<endl;
	cout<<"Start"<<endl;
	cin>>A;
	if(!strcmp(A,"Begin")==0){
		cout<<"Syantactic Error"<<endl;
		exit(-1);
	}
	vector <string> V1;
	int i=0;
	char B[10];
	while(!strcmp(B,"1")==0){
		cin>>B;
		V1.push_back(B);
		i++;
	}
	int c=V1.size();
	cout<<c<<endl;
	string C;
	V1.pop_back();
	C=V1.back();
	// cout<<C<<endl;
	if(C!="End"){
		cout<<"Syantax Error"<<endl;
		exit(-1);
	}
	int bye=0;
	while(c-2){
		int a=0,b=0,d=0;
		V1.pop_back();
		C=V1.back();
		// cout<<C<<endl;
		int num=C.size();
		if(num<7){
			for(int j=0;j<num;j=j+2){
				int count=0;
				for(int k=0;k<3;k++){
					if(C[j]==var[k]){
						continue;
					}
					else{
						count++;
					}
				}
				if(count==3){
					cout<<"1.Syantax Error at line "<<c-1<<endl;
					a++;
					bye++;
				}
			}
			if(num>5){
				for(int j=0;j<2;j++){
					if(C[3]==sign[j]){
						continue;
					}
					else{
						b++;					
					}
				}
			}
			if(b==2){
				cout<<"2.Syanatx Error at line"<<c-1<<endl;
			}
			if(C[1]!='='){
				cout<<"3.Syantax Error at line "<<c-1<<endl;
				b++;
				bye++;
			}
			if(C[num-1]!=';'){
				cout<<"4.Syantax Error at line"<<c-1<<endl;
				d++;
				bye++;
			}
		}		
		else{
			if(num>7||a!=0||b!=0||c!=0){
				cout<<"Syantax Error \n";
				bye++;
			}
		}
		c--;
	}
	if(bye==0){
		cout<<"Alright ...Grammer has no error"<<endl;
	}
	return 0;
}

