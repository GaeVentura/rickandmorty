import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public abstract class DispatcherSkeleton implements IDispatcher {


    private int port;
    
    public DispatcherSkeleton(int p){

        port = p;
    }


    public void run_skeleton(){

        try {
            ServerSocket s = new ServerSocket(port);
                while (true){

                    Socket skt = s.accept();

                    SkeletonWorkerThread t = new SkeletonWorkerThread(skt, this);

                    t.start();
                    



            }
    
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }




    }


}
