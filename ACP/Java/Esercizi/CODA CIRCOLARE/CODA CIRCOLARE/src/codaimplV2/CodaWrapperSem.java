import java.util.concurrent.Semaphore;

public class CodaWrapperSem extends CodaWrapper{


    private Semaphore prod_sem;
    private Semaphore cons_sem;

    public CodaWrapperSem(Coda c){

        super(c);

        prod_sem = new Semaphore(coda.getSize());
        cons_sem = new Semaphore(0);

    }
    

    public void inserisci(int i){
        prod_sem.acquire();

        synchronized(coda){
            coda.inserisci(i);
        }

        cons_sem.release();

        
        
    }
}
