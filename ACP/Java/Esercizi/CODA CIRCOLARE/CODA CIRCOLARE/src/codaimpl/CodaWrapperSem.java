package codaimpl;

import java.util.concurrent.Semaphore;

import coda.Coda;
import coda.CodaWrapper;
public class CodaWrapperSem extends CodaWrapper {
    
 
    private Semaphore prod_sem;
    private Semaphore cons_sem;

    public CodaWrapperSem(Coda c){
        super(c);

        prod_sem = new Semaphore(coda.getSize());
        cons_sem = new Semaphore(0);

    }

    public void inserisci(int i){

        try {
            prod_sem.acquire();
            
            try {
                synchronized(coda){
                coda.inserisci(i);      
                }          
            } finally {
                
                cons_sem.release();
            }

            

        } catch (InterruptedException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }
    

    public int preleva(){
        
        int i = 0;
        try {
            cons_sem.acquire();
            try{
                synchronized(coda){
                    i = coda.preleva();
                }   
                } finally {
                    prod_sem.release();
                    
                }
            
        } catch (InterruptedException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }

        return i;
    }


}
