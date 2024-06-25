package Sensor;

public class CodaCircolare {

    private String data[];
    private int size;
    private int nElem;
    private int head;
    private int tail;


    public CodaCircolare(int size){

        this.size = size;
        data = new String[size];
        nElem = head = tail = 0;



    }


    public void put(String comando){
        
        data[tail] = comando;

        nElem++;
        tail = (tail+1)%size;

    }

    public String take(){

        String comando;

        comando = new String(data[head]);

        nElem--;

        head = (head+1)%size;

        return comando;


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
