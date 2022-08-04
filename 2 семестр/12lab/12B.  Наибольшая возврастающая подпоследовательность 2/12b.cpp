// 12b.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//
#include <iostream>
#include <vector>
#include <stdio.h>
#include <cmath>



//void bins() {
//
//	long long right = countOfSubsequence;
//	
//	long long left = 0;
//
//
//
//}

int main()
{

	

	long long INF = std::pow(10, 9);

	long long countOfSubsequence;

	std::cin >> countOfSubsequence;

	//long long* arrayOfLen = new long long [countOfSubsequence + 1];

	std::vector <long long>  arrayOfLen;

	long long* arrayOfParents = new long long[countOfSubsequence + 1];

	long long* arrayOfInd = new long long[countOfSubsequence + 1];

	long long* arrayOfSubsequence = new long long[countOfSubsequence];

	for (long long i = 0; i < countOfSubsequence; i++) {

		std::cin >> arrayOfSubsequence[i];

		arrayOfParents[i] = INF;

		arrayOfInd[i] = INF;

		arrayOfLen.push_back(INF);


	}

	//arrayOfLen[countOfSubsequence] = INF;

	arrayOfLen.push_back(INF);

	arrayOfInd[countOfSubsequence] = INF;

	arrayOfParents[countOfSubsequence] = INF;

	arrayOfLen[0] = -INF;

	arrayOfInd[0] = -1;

	long long lens = 0;

	for (long long i = 0; i < countOfSubsequence; i++) {
		
		auto  bb = std::lower_bound(arrayOfLen.begin(), arrayOfLen.end(), arrayOfSubsequence[i]);
		
		auto j = std::distance(arrayOfLen.begin(), bb);

		

		if ((arrayOfLen[j - 1] >= arrayOfSubsequence[i]) || (arrayOfSubsequence[i] >= arrayOfLen[j])) {

			continue;
		}

		if (j > lens) {

			lens = j;
		}
		arrayOfLen[j] = arrayOfSubsequence[i];

		arrayOfInd[j] = i;

		arrayOfParents[i] = arrayOfInd[j - 1];

	}


	long long pos = arrayOfInd[lens];

	std::vector<long long> path;

	while (pos != -1) {

		path.push_back(arrayOfSubsequence[pos]);

		pos = arrayOfParents[pos];

	}

	std::cout << lens << std::endl;

	for (long long i = path.size()-1; i >= 0; i--) {

		std::cout << path[i] << " ";
	}

}


// Запуск программы: CTRL+F5 или меню "Отладка" > "Запуск без отладки"
// Отладка программы: F5 или меню "Отладка" > "Запустить отладку"

// Советы по началу работы 
//   1. В окне обозревателя решений можно добавлять файлы и управлять ими.
//   2. В окне Team Explorer можно подключиться к системе управления версиями.
//   3. В окне "Выходные данные" можно просматривать выходные данные сборки и другие сообщения.
//   4. В окне "Список ошибок" можно просматривать ошибки.
//   5. Последовательно выберите пункты меню "Проект" > "Добавить новый элемент", чтобы создать файлы кода, или "Проект" > "Добавить существующий элемент", чтобы добавить в проект существующие файлы кода.
//   6. Чтобы снова открыть этот проект позже, выберите пункты меню "Файл" > "Открыть" > "Проект" и выберите SLN-файл.
