#include <iostream>
#include <vector>
#include <fstream>


std::vector<int> Colors;

std::ifstream input("cycle.in");
std::ofstream out("cycle.out");

std::vector<int> temp;


int cycleNumber = -1;

int prevCycleNumber = -1;

struct adjencyList {

    std::vector<int> list;

    int prevNumber;

    std::vector<int> reverseList;

    adjencyList() {

        prevNumber = -1;
    }

};


std::vector<adjencyList> alist;


void DFS(int i, int j) {


    Colors[i] = 1;

    alist[i].prevNumber = j;


    for (int k = 0; k < alist[i].list.size() && cycleNumber == -1; k++) {


        if (Colors[alist[i].list[k]] == 0) {

            DFS(alist[i].list[k], i);

        }
        else if (Colors[alist[i].list[k]] == 1) {

            cycleNumber = alist[i].list[k];

            prevCycleNumber = i;


        }


    }


    Colors[i] = 2;

}


void print(int i) {

    if (i != cycleNumber) {

        temp.push_back(i);

        print(alist[i].prevNumber);

    }
}



int main()
{
    if (!input.is_open()) {

        return -1;
    }

    int countOfVertices; int countOfEdges;

    input >> countOfVertices >> countOfEdges;

    for (int i = 0; i < countOfVertices; i++) {

        Colors.push_back(0);

        adjencyList c;
        alist.push_back(c);
    }

    int a, b;

    for (int i = 0; i < countOfEdges; i++) {

        input >> a >> b;

        alist[a - 1].list.push_back(b - 1);

        alist[b - 1].reverseList.push_back(a - 1);

    }

    for (int i = 0; i < countOfVertices; i++) {

        if (Colors[i] == 0) {

            DFS(i, -1);

        }

    }

    if (cycleNumber == -1) {

        out << "NO";
    }

    else {

        out << "YES" << "\n";
        print(prevCycleNumber);


        out << cycleNumber + 1 << " ";
        for (int i = temp.size() - 1; i >= 0; i--) {

            out << temp[i] + 1 << " ";
        }

    }
}