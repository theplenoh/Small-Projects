#include <iostream>
#include <climits>
using namespace std;

class Counter
{
    private:
        // Attributes
        int count;
        int maxValue;

    public:
        // Constructors && Destructors
        Counter()
        {
            count = 0;
            maxValue = INT_MAX;
        }
        Counter(int mVal)
        {
            count = 0;
            maxValue = mVal;
        }
        ~Counter()
        {
            cout << "Destructor Called." << endl;
        }

        // Main Methods
        void increment()
        {
            if (count < maxValue)
                count+=1;
            else
                cout << "Counter overflow. Increment ignored." << endl;
        }
        void decrement()
        {
            if (count > 0)
                count-=1;
            else
                cout << "Counter underflow. Decrement ignored." << endl;
        }

        // Modifiers
        void setCount(int val)
        {
            if (0 <= val&&val <= maxValue)
                count = val;
            else
                cout << "New value is out of range. Value not changed." << endl;
        }
        void setMaxValue(int val)
        {
            if (0 <= val&&val <= INT_MAX)
                maxValue = val;
            else
                cout << "New maxValue is out of range -- not changed." << endl;
        }

        // Accessors
        int getCount() const
        {
            return count;
        }
        int getMaxValue() const
        {
            return maxValue;
        }

        // PrintStatus
        void printStatus()
        {
            cout <<"------------------------------"<<endl;
            cout <<"count: "<<count<< endl;
            cout <<"maxValue: "<<maxValue<< endl;
            cout <<"------------------------------"<<endl;
        }
};

int main()
{
    Counter c1(3);

    c1.increment();
    c1.printStatus();

    c1.increment();
    c1.printStatus();

    c1.increment();
    c1.printStatus();

    c1.increment();
    c1.printStatus();

    c1.increment();
    c1.printStatus();

    c1.setMaxValue(12);

    c1.decrement();
    c1.printStatus();

    c1.decrement();
    c1.printStatus();

    return 0;
}
