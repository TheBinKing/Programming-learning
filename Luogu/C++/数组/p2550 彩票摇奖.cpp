#include <iostream>
using namespace std;



int main() {
	int num;
	int result[8] = { 0 };
	int Z[300][8];
	cin >> num;
	for (int i = 0;i <= num;i++) {
		cin >> Z[i][0] >> Z[i][1] >> Z[i][2] >> Z[i][3] >> Z[i][4] >> Z[i][5] >> Z[i][6];
	}
	for (int i = 1;i <= num;i++) {
		int in_num = 0;
		for (int j = 0;j < 7;j++) {
			for (int h = 0;h < 7;h++) {
				if (Z[i][h] == Z[0][j])
				{
					in_num++;
					//Z[i][h] = -1;
					break;
				}
					
			}
		}
		result[7 - in_num]+= 1;
	}

	for (int i = 0;i < 7;i++) {
		cout << result[i] << ' ';
}
	
}