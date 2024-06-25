package Sensor;

import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.UnsupportedEncodingException;

public class TExecutor extends Thread{

    private CodaCircolareMon coda;

    public TExecutor(CodaCircolareMon coda){

        this.coda = coda;
    }


    public void run(){


        try {
            Thread.sleep(10000);
        } catch (InterruptedException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }

        String[] codaPrelevata = coda.takeAll();
        try{
            FileWriter fileWriter = new FileWriter("fileName.txt");
            PrintWriter writer = new PrintWriter(fileWriter);
            for(int i = 0; i < coda.getSize(); i++){
            

                writer.println(codaPrelevata[i]);

            }
            writer.close();
        } catch (NullPointerException e){
                System.out.print("HO TROVATO UNO SPAZIO VUOTO");
        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (UnsupportedEncodingException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        
        


    }
}
