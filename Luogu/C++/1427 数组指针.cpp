#include <iostream>
using namespace std;
int a[101], c;
int* p = a;//����һ��int���͵�ָ��,ָ�����鲻��ȡַ��
int main() {
	while (true)
	{
		cin >> c;
		if (c == 0) break;
		p++;
		*p = c;
	}
	while (p!=a)
	{
		cout << *p << " ";
		p--;
	}
	return 0;
}