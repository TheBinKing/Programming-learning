#include <iostream>
#include <math.h>
using namespace std;


bool IsPrime(int num) {
	if (num==0||num == 1) return 0;
	if (num == 2 || num == 3) return 1;
	for (int i = 3;i < (sqrt(num) + 1);i++) {
		if (num % i == 0) return 0;
	}
	return 1;
}
int main() {
	char a[9999];
	int b[26] = { 0 };
	int max1=-1, min1=999;
	cin >> a;
	for (int i = 0;a[i];i++) {
		if(a[i]>='a'&&a[i]<='z')
		b[a[i] - 'a']++;
	}

	for (int i = 0;i < 26;i++) {
		if (b[i] != 0) {
			if (b[i] > max1)
				max1 = b[i];
			if (b[i] < min1)
				min1 = b[i];
		}
	}

	int z = max1 - min1;
	if (IsPrime(z)) cout << "Lucky Word" << "\n" << z;
	else cout << "No Answer" << "\n" << z;
	return 0;
}