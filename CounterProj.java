class Counter
{
    // Attributes
    private int count;
    private int maxValue;

    // Constructors
    public Counter()
    {
        count = 0;
        maxValue = Integer.MAX_VALUE;
    }
    public Counter(int mVal)
    {
        count = 0;
        maxValue = mVal;
    }

    // Main methods
    public void increment()
    {
        if (count < maxValue)
            count++;
        else
            System.out.println("Counter overflow. Increment ignored.");
    }
    public void decrement()
    {
        if (count > 0)
            count--;
        else
            System.out.println("Counter underflow. Decrement ignored.");
    }

    // Modifiers
    public void setCount(int val)
    {
        if (0 <= val && val <= maxValue)
            count = val;
        else
            System.out.println("New value is out of range. Value not changed.");
    }
    public void setMaxValue(int val)
    {
        if (0 <= val && val <= Integer.MAX_VALUE)
            maxValue = val;
        else
            System.out.println("New maxValue is out of range -- not changed.");
    }

    // Accesors
    public int getCount()
    {
        return count;
    }
    public int getMaxValue()
    {
        return maxValue;
    }

    // PrintStates
    public void printStates()
    {
        System.out.println("-----------------------------");
        System.out.println("count: "+count);
        System.out.println("maxValue: "+maxValue);
        System.out.println("-----------------------------");
    }
}

class CounterProj
{
    public static void main(String[] args)
    {
        Counter c1 = new Counter(3);

        c1.increment();
        c1.printStates();

        c1.increment();
        c1.printStates();

        c1.increment();
        c1.printStates();

        c1.increment();
        c1.printStates();

        c1.increment();
        c1.printStates();

        c1.setMaxValue(12);

        c1.decrement();
        c1.printStates();

        c1.decrement();
        c1.printStates();
    }
}
