package src.Magazzino;

import java.io.IOException;
import java.net.*;

public abstract class MagazzinoSkeleton implements iMagazzino {

    protected int port;


    public MagazzinoSkeleton(int p){

        port = p;
    }

    @SuppressWarnings("resource")
    public void run_skeleton(){
        

        try{
            
            ServerSocket skt = new ServerSocket(port);

    

            while (true){

                Socket socket = skt.accept();

                MagazzinoThread t = new MagazzinoThread(this, socket);

                t.start();

            }
        } catch (IOException e){
            e.printStackTrace();
 
        } finally{


        }
    }


    
}
