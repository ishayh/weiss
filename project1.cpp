#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

int main(){

	int N;
	int k;
	int M;
	int s;
	bool stop;

	cout << "Please enter the size of the total population,";
	cout << " the number of zombies each simulation will begin with,";
	cout <<" the number of simulations, and the seed value." << endl;
	cin >> N >> k >> M >> s;
	cout << endl;
	
	int hold_N = N;
	int hold_k = k;

	int* sims = NULL;
	sims = new int[M];

	if (k > N){
	cout << "Error! The zombie population must not ";
	cout << "be greater than the total population." << endl;
	stop = true;
	}
	else if ( N <= 0 || k <= 0 || M <= 0){
	cout << "Error! Please enter only positive numbers." << endl;
	stop = true;
	}

	if (stop == false){
		for (int sim_number = M - 1; sim_number >= 0; sim_number--){
			N = hold_N;
			k = hold_k;
			int number_of_days = 0;
			srand(s * (sim_number + 1) * (number_of_days + 1));
			int x = k;
			while(k<N){
				x = k;
				++number_of_days;
				while(x>0 && k<N){
					--x;
					if(rand() % N >= k){
						++k;
					}
				}
			}
			sims[sim_number] = number_of_days;
		}
		for (int i = 0; i < M; ++i){
			cout << sims[i] << " ";
		}
		cout << endl;

		double avg = 0.0;
		double sum = 0.0;
		for (int avg_loop = 0; avg_loop < M; ++avg_loop){
			sum += sims[avg_loop];
		}
		avg = sum / M;
		cout << "The average number of days is " << avg << endl;
		int max = 0;
		for (int max_loop = 0; max_loop < M; ++max_loop){
			if (sims[max_loop] > max){
				max = sims[max_loop];
			}
		}
		cout << "The maximum number of days is " << max << endl;
		int min = max;
		for (int min_loop = 0; min_loop < M; ++min_loop){
			if (sims[min_loop] < min){
				min = sims[min_loop];
			}
		}
		cout << "The minimum number of days is " << min << endl;
	}
	delete [] sims;
	sims = NULL;
	cout << endl;
	return 0;
}