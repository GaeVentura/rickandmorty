package src.Magazzino;


import java.util.concurrent.locks.*;


public class MagazzinoImpl extends MagazzinoSkeleton {

    private CodaCircolare coda;
    private Lock lock;
    
    private Condition prodCond;
    private Condition consCond;

    public MagazzinoImpl(CodaCircolare coda, int port){
        super(port);
        this.coda = coda;

        lock = new ReentrantLock();

        prodCond = lock.newCondition();
        consCond = lock.newCondition();

    }


    public void deposita(int i){

        lock.lock();

        try{

            while (!coda.empty()){
                prodCond.await();
            }

            coda.deposita(i);
        } catch (InterruptedException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }finally {
            
            consCond.signal();
        }
        lock.unlock();
    }

    public int preleva(){

        lock.lock();
        int i =0;
        try{


            while(!coda.full()){
                consCond.wait();
            }
            
            i = coda.preleva();
            
        } catch (InterruptedException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } finally{

            prodCond.signal();
            lock.unlock();
        } 

        return i;
    }


    
}
