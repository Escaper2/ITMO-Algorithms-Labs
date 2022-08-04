#include <iostream>
#include <vector>
#include <fstream>


std::vector<int> Colors;

std::ifstream input("bipartite.in");
std::ofstream out("bipartite.out");

std::vector<int> temp;


bool flag = true;


int cycleNumber = -1;

int prevCycleNumber = -1;

struct adjencyList {

    std::vector<int> list;

    int prevNumber;

    int bipartite;
    
    adjencyList() {

        prevNumber = -1;

        bipartite = 0;

    }

};


std::vector<adjencyList> alist;


void DFS(int i, int j) {


    Colors[i] = 1;

    

    alist[i].prevNumber = j;

    alist[i].bipartite = j;


    for (int k = 0; k < alist[i].list.size() && cycleNumber == -1; k++) {


        if (Colors[alist[i].list[k]] == 0) {

            if (j == 1) {

                DFS(alist[i].list[k], 2);
            }

            else {

                DFS(alist[i].list[k], 1);
            }

        }
        else if (Colors[alist[i].list[k]] == 1 && alist[alist[i].list[k]].bipartite == j) {

            cycleNumber = alist[i].list[k];

            prevCycleNumber = i;

            flag = false;




         

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


    //if (countOfVertices < 2 || countOfEdges < 1) {

    //    out << "NO";

    //    exit(0);


    //}


    int a, b;

    for (int i = 0; i < countOfEdges; i++) {

        input >> a >> b;

        if (a == b) {

            out << "NO";
            exit(0);
        }

        alist[a - 1].list.push_back(b - 1);

        alist[b - 1].list.push_back(a - 1);

    }

    for (int i = 0; i < countOfVertices; i++) {

        if (Colors[i] == 0) {

            DFS(i, 1);

        }

    }



    if (flag) {

        out << "YES";

    }
    else {

        out << "NO";
    }

}