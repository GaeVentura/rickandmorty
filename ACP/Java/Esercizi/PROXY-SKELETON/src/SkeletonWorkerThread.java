import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;

public class SkeletonWorkerThread extends Thread{

    private Socket skt;
    private IDispatcher dispatcher;

    public SkeletonWorkerThread(Socket s, IDispatcher d){
        skt = s;
        dispatcher = d;
    }



    public void run(){

        try {
            DataInputStream fromClient = new DataInputStream(skt.getInputStream());
            DataOutputStream toClient = new DataOutputStream(skt.getOutputStream());

            String st = fromClient.readUTF();

            if (st.equalsIgnoreCase("sendCmd")){

                int i = fromClient.readInt();
                
                dispatcher.sendCmd(i);
           
            } else if (st.equalsIgnoreCase("getCmd")){

                toClient.writeInt(dispatcher.getCmd());
            } else {

                toClient.writeUTF("metodo non riconosciuto");

            }
            toClient.flush();

            fromClient.close();
            toClient.close();
            skt.close();
            
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }



    }
    
}
