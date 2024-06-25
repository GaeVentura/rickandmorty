package Sensor;

import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class CodaCircolareMon {

    private CodaCircolare coda;
    private Lock lock;
    private Condition prod_cond;
    private Condition cons_cond;

    
    public CodaCircolareMon(CodaCircolare codaCircolare){

        coda = codaCircolare;
        lock = new ReentrantLock();
        prod_cond = lock.newCondition();
        cons_cond = lock.newCondition();
    }


    public void put(String comando){

        System.out.println("SONO FERMO AL LOCK");
        lock.lock();
        System.out.println("SONO FERMO AL LOCK");


        while( ! coda.empty()){

            try {
                prod_cond.await();
            } catch (InterruptedException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
        }

        coda.put(comando);

        System.out.println("[SERVER] HO INSERITO NELLA CODA IL COMANDO :" + comando);

        cons_cond.signal();

        lock.unlock();
    }

    public String[] takeAll(){

        lock.lock();

        while(! coda.full()){

            try{
                cons_cond.wait();
            } catch( InterruptedException e){

                e.printStackTrace();

            }
        }

        String[] copiaCoda = new String[coda.getSize()];

        for(int i = 0; i < coda.getSize(); i++){

            copiaCoda[i] = coda.take();

            System.out.println("[SERVER] HO PRELEVATO DALLA CODA IL COMANDO "+copiaCoda[i]);
        }


        prod_cond.signalAll();

        lock.unlock();

        return copiaCoda;

    }

    public int getSize(){
        return coda.getSize();
    }
    
}
