package codaimpl;

import coda.Coda;

public class CodaCircolare implements Coda{

    private int data[];
    private int size;
    private int elem;
    private int tail;
    private int head;

    public CodaCircolare(int s){
        size = s;
        data = new int[size];
        elem = 0;
        tail = 0;
        head = 0;
    }
    


    public void inserisci(int i){

        data[tail%size] = i;
            
        try {
            Thread.sleep(101);
        } catch (InterruptedException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }

        elem = elem+1;
        tail = tail+1;
        System.out.println("ho inserito "+ i );

    }

    public int preleva(){
        int i = data[head%size];

        try {
            Thread.sleep(101);
        } catch (InterruptedException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }

        elem = elem -1;
        head = head +1;
        return i;

    }


    public boolean empty(){
        if (elem == 0)
            return true;

        return false;

    }

    public boolean full(){
        if ( elem == size )
            return true;
        
        return false;
    }

    public int getSize(){
        return elem;
    }
}
