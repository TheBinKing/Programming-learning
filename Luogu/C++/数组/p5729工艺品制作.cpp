#include <iostream>
using namespace std;
int main() {
	int a[23][23][23] = { 0 };
	int L, W, H;
	int L2, W2, H2;
	int L3, W3, H3;
	cin >> L >> W >> H;
	for (int i = 1;i <= L;i++) {
		for (int j = 1;j <= W;j++) {
			for (int k = 1;k <= H;k++) {
				a[i][j][k] = 1;
			}
		}
	}
	int num;
	cin >> num;
	for (int n = 0;n < num;n++) {
		cin >> L3 >> W3 >> H3;
		cin >> L2 >> W2 >> H2;
		for (int i = L3;i <= L2;i++) {
			for (int j = W3;j <= W2;j++) {
				for (int k = H3;k <= H2;k++) {
					a[i][j][k] = 0;
				}
			}
		}
	}
	int count = 0;
	for (int i = 1;i <= L;i++) {
		for (int j = 1;j <= W;j++) {
			for (int k = 1;k <= H;k++) {
				if (a[i][j][k] == 1)
					count++;
			}
		}
	}
	cout << count<<endl;
}