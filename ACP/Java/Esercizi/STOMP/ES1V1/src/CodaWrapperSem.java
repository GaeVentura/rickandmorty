
import java.util.concurrent.Semaphore;

public class CodaWrapperSem extends CodaWrapper{


    private Semaphore prod_sem;
    private Semaphore cons_sem;

    public CodaWrapperSem(Coda c){

        super(c);

        prod_sem = new Semaphore(coda.getSize());
        cons_sem = new Semaphore(0);
        System.out.println(coda.getSize());


    }
    

    public void inserisci(int i){
        try {
            
            prod_sem.acquire();

            System.out.println("HO SUPERATO IL SEMAFORO");
        } catch (InterruptedException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }

        synchronized(coda){
            coda.inserisci(i);
        }

        cons_sem.release();

        
        
    }

    public int preleva(){
        int i = 0;
        try {
            cons_sem.acquire();
        } catch (InterruptedException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        
        synchronized(coda){

            i = coda.preleva();
            System.out.println(i);
            
        }

        prod_sem.release();

        return i;
    }
}
