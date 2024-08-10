import java.util.concurrent.TimeUnit;

class Elevator
{
    private int destFloor;
    private int currFloor;
    private boolean doorState;

    public Elevator()
    {
        this.destFloor = 1;
        this.currFloor = 1;
        this.doorState = false;
    }

    public void setFloor(int f)
    {
        this.currFloor = f;
    }
    public int getFloor()
    {
        return this.currFloor;
    }

    public void moveToFloor(int callingFloor)
    {
        int tmpFloor = this.currFloor;
        if (callingFloor > currFloor)
        {
            while (tmpFloor < callingFloor)
            {
                System.out.println("UP "+tmpFloor);
                try
                {
                    Thread.sleep(1000);
                }
                catch(InterruptedException ex)
                {
                    Thread.currentThread().interrupt();
                }
                tmpFloor++;
            }
            this.currFloor = callingFloor;
            System.out.println("Now the elevator has reached Floor "+callingFloor+".");
        }
        else if (callingFloor < this.currFloor)
        {
            while (tmpFloor > callingFloor)
            {
                System.out.println("DOWN "+tmpFloor);
                try
                {
                    Thread.sleep(1000);
                }
                catch(InterruptedException ex)
                {
                    Thread.currentThread().interrupt();
                }
                tmpFloor--;
            }
            this.currFloor = callingFloor;
            System.out.println("Now the elevator has reached Floor "+callingFloor+".");
        }
        else
        {
            System.out.println("The elevator is already on the floor.");
        }
    }
    public void openDoor()
    {
        doorState = true;
        System.out.println("The door has opened.");
    }
    public void closeDoor()
    {
        doorState = false;
        System.out.println("The door has closed.");
    }
}

class ElevatorProj
{
    public static void main(String[] args)
    {
        Elevator elev = new Elevator();
        System.out.println(elev.getFloor());
        elev.moveToFloor(4);
        elev.moveToFloor(10);
        elev.moveToFloor(1);

        elev.openDoor();
        elev.closeDoor();

        elev.moveToFloor(14);
    }
}
