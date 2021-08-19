/*指针在stl里又叫迭代器*/
#include <iostream>
#include <vector>
using namespace std;
vector<int> a;
int c;
int main() {
	while (true)
	{
		cin >> c;
		if (c == 0)break;
		a.push_back(c);
	}
	for (vector<int>::iterator it = a.end() - 1;it >= a.begin();it--) {
		cout << *it << " ";
	}
	return 0;
}