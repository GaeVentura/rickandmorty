public class CodaCircolare implements icoda {

    private int data[];
    private int head;
    private int tail;
    private int nElem;
    private int size;
    


    public CodaCircolare(int s){

        data = new int[size];
        size = s;
        head=tail=nElem=0;

    }

    public void inserisci(int i){

        data[tail] = i;
        tail = (tail+1) % size;
        nElem = nElem + 1;


    }


    public int preleva(){
        
        int i = data[head];

        head = head+1 %size;
        nElem = nElem - 1;

        
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

        return nElem;
    }
}
