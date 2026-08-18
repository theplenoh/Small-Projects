#include <iostream>
#include <string>
using namespace std;

class Savings
{
    private:
        int id;
        string name;
        float balance;
        float interestRate;
        bool validId(int) const;

    public:
        Savings();
        void openAccount();
        void changeName(int, string);
        void addInterest();
        void deposit(int, float);
        void withdraw(int, float);
        void closeAccount(int);
        float getBalance() const;
};

Savings::Savings()
{
    name = "";
    id = 0;
    balance = 0.0;
    interestRate = 0.0;
}

void Savings::openAccount()
{
    std::cout << "Account name: ";
    std::getline(std::cin, name, '\n');
    std::cout << "Account ID: ";
    std::cin >> id;
    std::cout << "Initial balance: $";
    std::cin >> balance;
    std::cout << "Annual interest rate percentage: %";
    std::cin >> interestRate;
}

bool Savings::validId(int ident) const
{
    if (id == ident)
        return true;
    else
    {
        std::cerr << "Error - ID's do not match!";
        return false;
    }
}

void Savings::changeName(int ident, string na)
{
    if (validId(ident))
    {
        name = na;
        std::cout << "Changing account name to " << na << std::endl;
    }
    else
    {
        std::cerr << "Reject name change request." << std::endl;
    }
}

void Savings::addInterest()
{
}

int main()
{
}
