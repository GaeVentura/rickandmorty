

public class CodaCircolare implements Coda {

    private int data[];
    private int head;
    private int tail;
    private int nElem;
    private int size;
    


    public CodaCircolare(int s){

        data = new int[s];
        size = s;
        head=tail=nElem=0;

    }

    public void inserisci(int i){
        System.out.print(tail);
        data[tail] = i;
        tail = (tail+1) % size;
        nElem = nElem + 1;


    }


    public int preleva(){
        
        int i = data[head];

        head = (head+1) %size;
        nElem = nElem - 1;

        return i;
        
    }

    public boolean empty(){

        if (nElem == size){
            return false;
        } else {
            return true;
        }
    }
    public boolean full(){

        if (nElem == size){
            return true;
        } else {
            return false;
        }
    }

    public int getSize(){

        return size;
    }
}
