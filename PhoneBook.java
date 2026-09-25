class PhoneBookEntry
{
    String name;
    String phoneNumber;

    public PhoneBookEntry(String name, String phoneNum)
    {
        this.name = name;
        this.phoneNumber = phoneNum;
    }
}

class PhoneBook
{
    private static final int RECORD_SZ = 30;

    public static void main(String[] args)
    {
        PhoneBookEntry[] myPhoneBook = new PhoneBookEntry[RECORD_SZ];
    }
}
