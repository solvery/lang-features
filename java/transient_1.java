// transient with data serialization.

import java.io.*;

class Person implements java.io.Serializable {
	public String name;
	public transient int age;

	public Person(String name , int age) {
		this.name = name;
		this.age = age;
	}
}

public class transient_1 {
	public static void main(String[] args) {
		ObjectOutputStream oos = null;
		ObjectInputStream ois = null;
		try {
			oos = new ObjectOutputStream(
					new FileOutputStream("transient.txt"));
			Person p1 = new Person("John", 20);
			oos.writeObject(p1);
			System.out.println(p1.age);

			ois = new ObjectInputStream(
					new FileInputStream("transient.txt"));
			Person p2 = (Person)ois.readObject();
			System.out.println(p2.age);
		}
		catch (Exception ex) {
			ex.printStackTrace();
		}
		finally {
			try {
				if (ois != null)
					ois.close();
				if (oos != null)
					oos.close();
			}
			catch (IOException ex) {
				ex.printStackTrace();
			}
		}
	}
}

