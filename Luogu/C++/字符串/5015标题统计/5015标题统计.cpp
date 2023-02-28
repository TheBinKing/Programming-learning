#include <iostream>
#include<cstdio>
#include<cstring>
using namespace std;


int main() {
	char a[20];
	int count = 0;

	while (cin >> a) {   //注意需要考虑输入中有空格等情况，需要用一个循环不断输入，防止输入内容导致的终止情况发送
		for (int i = 0;a[i];i++) {
			if ((a[i] >= 'a' && a[i] <= 'z')
				||
				(a[i] >= 'A' && a[i] <= 'Z')
				||
				(a[i] >= '0' && a[i] <= '9'))
				count++;
		}
	}
	cout << count;
}