package src.Dispatcher;

import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.net.UnknownHostException;

import src.Magazzino.iMagazzino;

public class DispatcherProxy  implements iMagazzino{

    public String host;
    public int port;

    public DispatcherProxy(String host, int port){

        this.host = host;
        this.port = port;
        
    }

    public void deposita(int i){

        try {
            Socket socket = new Socket(host, port);
            DataOutputStream out = new DataOutputStream(new BufferedOutputStream(socket.getOutputStream()));

            out.writeUTF("deposita");
            out.flush();

            out.writeInt(i);
            out.flush();

            out.close();
            
            socket.close();


        } catch (UnknownHostException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }

        
    }

    public int preleva(){

        Integer i = 0;

        try{

            Socket socket = new Socket(host,port);
            DataOutputStream out = new DataOutputStream(new BufferedOutputStream(socket.getOutputStream()));
            DataInputStream in = new DataInputStream(new BufferedInputStream(socket.getInputStream()));

            out.writeUTF("preleva");

            i = in.readInt();

            System.out.println("[PROXY] HO PRELEVATO " + i.toString());

            socket.close();
        } catch (IOException e){
            e.printStackTrace();
        } 

        return i;
    }
    
}
