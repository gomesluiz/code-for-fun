#include "iostream"

using namespace std;

int main(int argc, char *argv[])
{
    if (argc > 2)
    {
        cout << "Hello " << argv[1] << " and " << argv[2] << "\n";
        cout << "Goodbye " << argv[2] << " and " << argv[1] << "\n";
    }
    else
    {
        cout << "Usage: HelloGoodbye name-1 name-2\n";
    }
}