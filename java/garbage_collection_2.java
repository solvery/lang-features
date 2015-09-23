
import java.lang.ref.*;

public class garbage_collection_2 {
    public static void main(String[] args) throws Exception {
		String s1 = new String("hello");
		ReferenceQueue rq = new ReferenceQueue();
		PhantomReference pr = new PhantomReference(s1, rq);
		WeakReference	wr = new WeakReference(s1);

		s1 = null;
		System.out.println(pr.get());
		System.out.println(wr.get());

		System.gc();
		System.runFinalization();
		System.out.println(rq.poll() == pr);
		System.out.println(pr.get());
		System.out.println(wr.get());
    }
}



