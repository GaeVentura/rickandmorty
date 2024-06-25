package src.Magazzino;

import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.net.Socket;

public class MagazzinoThread extends Thread {

    private iMagazzino mag;
    private Socket socket;

    public MagazzinoThread(iMagazzino mag, Socket skt ){

        this.mag = mag;

        this.socket = skt;
    }
    

    public void run(){
        try{
            DataOutputStream out = new DataOutputStream(new BufferedOutputStream(socket.getOutputStream()));
            DataInputStream in = new DataInputStream(new BufferedInputStream(socket.getInputStream()));

            String message = in.readUTF();

            if (message.equalsIgnoreCase("deposita")){

                int x = in.readInt();

                mag.deposita(x);

                out.writeUTF("messaggio depositato");
            } else {

                out.writeInt(mag.preleva());
            }

            out.flush();

            in.close();
            out.close();

        
        } catch(Exception e){
            e.printStackTrace();
        }
    }

}
