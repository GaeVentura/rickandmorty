package src.Magazzino;

public class CodaCircolare {

    private int head;
    private int tail;
    private int nElem;
    private int size;
    private int data[];

    public CodaCircolare(int size){
        head = tail = nElem = 0;
        this.size = size;
    }
    

    public void deposita(int i){
        data[tail] = i;
        tail = tail + 1 % size;
        nElem = nElem +1;
    }

    public int preleva(){

        int i = data[head];
        head = head+1 %size;
        nElem = nElem -1 ;
        return i;
    }

    public boolean empty(){

        if (nElem == size){
            return false;
        } else  {
            return true;
        }
    }

    public boolean full(){

        if (nElem == size){
            return true;
        } else  {
            return false;
        }
    }

    
}

