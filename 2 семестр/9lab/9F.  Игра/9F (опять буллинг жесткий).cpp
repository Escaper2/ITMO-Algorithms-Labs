#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <stack>
std::ifstream fin("game.in");
std::ofstream fout("game.out");

enum color {
    white,
    gray,
    black
};

class Point {
public:
    Point();
    color pointColor;
    int cnt;
    std::vector<int> v;
};

void BFS(Point arr[], Point* p);

void BFSSecondPart(std::vector<Point*>& vector, Point arr[]);

void minFind(int countOfEdges, Point mass[], int& min);

void Print(int min);





int main()
{
    int countOfVertices, countOfEdges, chip;

    int f, s;

    int min = 10000;

    fin >> countOfVertices >> countOfEdges >> chip;

    Point* mass = new Point[countOfVertices];

    for (int i = 0; i < countOfEdges; i++) {
        fin >> f >> s;
        mass[f - 1].v.push_back(s - 1);
    }

    for (int i = 0; i < countOfVertices; i++) {
        mass[i].cnt = 1000000;
        mass[i].pointColor = white;
    }

    BFS(mass, &mass[chip - 1]);

    minFind(countOfVertices, mass, min);

    return 0;
}


void minFind(int countOfVertices, Point mass[], int& min) {
    for (int i = 0; i < countOfVertices; i++) {

        if (mass[i].v.size() == 0 && mass[i].pointColor != white) {

            if (min > mass[i].cnt) {
                min = mass[i].cnt;
            }
        }
    }
    Print(min);

}

void Print(int min) {

    if (min % 2 == 0) {
        fout << "Second player wins";
    }
    else {
        fout << "First player wins";
    }


}

void BFS(Point arr[], Point* p) {
    p->cnt = 0;
    std::vector<Point*> vector;
    vector.push_back(p);
    while (!vector.empty()) {

        BFSSecondPart(vector, arr);
    }
}



void BFSSecondPart(std::vector<Point*>& vector, Point arr[]) {

    Point* vertex = vector.front();
    vector.erase(vector.begin());
    vertex->pointColor = gray;
    for (int i = 0; i < vertex->v.size(); i++)
    {
        if (arr[vertex->v[i]].pointColor == white)
        {
            arr[vertex->v[i]].cnt = vertex->cnt + 1;
            vector.push_back(&arr[vertex->v[i]]);
            vector.back()->pointColor = gray;
        }
    }

}


Point::Point()
{
    pointColor = white;
    cnt = 1000;
}
