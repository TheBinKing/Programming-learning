#include <iostream>
#include<cstdio>
#include<cstring>
using namespace std;


int main() {
	char a[20];
	int count = 0;

	while (cin >> a) {   //ע����Ҫ�����������пո���������Ҫ��һ��ѭ���������룬��ֹ�������ݵ��µ���ֹ�������
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