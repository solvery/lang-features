
enum Gender 
{
	MALE("male"),FEMALE("female");
	private String name;
	/// public Gender(String name) 
	// enum only private 
	private Gender(String name)
	{
		this.name = name;
	}
	public String getName()
	{
		 return this.name;
	}
}

public class enum_3 {
    public static void main(String[] args) {
		Gender g = Enum.valueOf(Gender.class, "FEMALE");
		System.out.println(g + " means " + g.getName());
    }
}


